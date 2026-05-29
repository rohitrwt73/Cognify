

# Import necessary libraries
import os, re
from langchain_community.vectorstores import FAISS

from langchain.chains import ConversationalRetrievalChain
from flask import Flask, render_template, request, redirect
from PyPDF2 import PdfReader

from groq import Groq
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

from langchain.text_splitter import CharacterTextSplitter

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


start_greeting = ["hi","hello"]
end_greeting = ["bye"]
way_greeting = ["who are you?"]

#Using this folder for storing the uploaded docs. Creates the folder at runtime if not present
DATA_DIR = "__data__"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

#Flask App
app = Flask(__name__)

vectorstore = None
conversation_chain = None
chat_history = []
rubric_text = ""
groq_client = Groq(
    api_key=GROQ_API_KEY
)

class HumanMessage:
    def __init__(self, content):
        self.content = content
    
    def __repr__(self):
        return f'HumanMessage(content={self.content})'

class AIMessage:
    def __init__(self, content):
        self.content = content
    
    def __repr__(self):
        return f'AIMessage(content={self.content})'


def get_pdf_text(pdf_docs):
    text = ""
    pdf_txt = ""
    for pdf in pdf_docs:
        filename = os.path.join(DATA_DIR,pdf.filename)
        pdf_txt = ""
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            page_text = page.extract_text() or ""
            text += page_text
            pdf_txt += page_text

        with (open(filename, "w", encoding="utf-8")) as op_file:
            op_file.write(pdf_txt)

    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_texts(
        texts=text_chunks,
        embedding=embeddings
    )

    return vectorstore


def get_conversation_chain(vectorstore):
    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True
    )
    
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    return conversation_chain
def _grade_essay(essay):
    messages = [
        {"role": "system",
        "content": "You are a Chinese bot, you are supposed to carefully grade the essay based on the given rubric and respond in Chinese only." + rubric_text}
    ]
    essay = "ESSAY : " + essay

    messages.append({'role': 'user','content':essay})
    response = groq_client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    temperature=0.4,
    max_tokens=1500
)
    
    data = response.choices[0].message.content

    data = re.sub(r'\n', '<br>', data)

    return data


@app.route('/')
def home():
    return render_template('new_home.html')


@app.route('/process', methods=['POST'])
def process_documents():
    global vectorstore, conversation_chain
    pdf_docs = request.files.getlist('pdf_docs')
    raw_text = get_pdf_text(pdf_docs)
    text_chunks = get_text_chunks(raw_text)
    vectorstore = get_vectorstore(text_chunks)
    conversation_chain = get_conversation_chain(vectorstore)
    return redirect('/chat')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    global vectorstore, conversation_chain, chat_history
    msgs = []
    
    if request.method == 'POST':
        user_question = request.form['user_question']
        
        response = conversation_chain({'question': user_question})
        chat_history = response['chat_history']
        
    return render_template('new_chat.html', chat_history=chat_history)

@app.route('/pdf_chat', methods=['GET', 'POST'])
def pdf_chat():
    return render_template('new_pdf_chat.html')

@app.route('/essay_grading', methods=['GET', 'POST'])
def essay_grading():
    result = None
    if request.method == 'POST':
        if request.form.get('essay_rubric', False):
            global rubric_text
            rubric_text = request.form.get('essay_rubric')

            return render_template('new_essay_grading.html')
        
        if len(request.files['file'].filename) > 0:
            pdf_file = request.files['file']
            text = extract_text_from_pdf(pdf_file)
            result = _grade_essay(text)
        else:
            text = request.form.get('essay_text')
            result = _grade_essay(text)
    
    return render_template('new_essay_grading.html', result=result, input_text=text)
    
@app.route('/essay_rubric', methods=['GET', 'POST'])
def essay_rubric():
    return render_template('new_essay_rubric.html')

def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
