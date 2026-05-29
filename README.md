# Unlocking Knowledge and Empowering Students with AI (Cognify)

## Problem Statement:

In today's digital age, students are inundated with information from textbooks, research papers, and online resources. Navigating this vast sea of knowledge and extracting meaningful insights can be overwhelming. Cognify addresses this challenge by providing an AI-powered platform that simplifies academic learning and enhances the writing process.
Context:
Leveraging the power of machine learning, natural language & Gen AI, this tool automates the traditionally manual insurance claim processing procedure.
• Implementation of AI and Generative AI will enhance data analysis and predictive capabilities.
• AI will provide deeper insights, improve accuracy, and streamline reporting processes.
• Predictive features will enable proactive decision-making based on anticipated impact fluctuations.

## Objective:

Cognify is an AI-powered academic research and essay evaluation platform designed to help students and educators interact with educational content more effectively.

### Primary Objectives

**1. Academic Research and Understanding**

Cognify provides clear and context-aware answers, summaries, and explanations based on the content of uploaded documents. Students can ask questions in natural language and receive responses grounded in the uploaded material.

**2. Essay Grading and Rubric-Based Evaluation**

Teachers and instructors can create or upload custom grading rubrics to personalize essay evaluation and ensure alignment with specific academic requirements and assessment standards.

### How It Works

**1. Document Upload and Processing**

Users upload PDF documents, and Cognify extracts and processes the textual content for analysis.

**2. Text Embedding and Semantic Search**

The extracted text is divided into meaningful chunks and converted into vector embeddings using Hugging Face Sentence Transformers. These embeddings are indexed using FAISS, enabling efficient semantic search and retrieval of relevant information.

**3. Intelligent Question Answering**

When a student submits a question, Cognify performs semantic retrieval to identify the most relevant document content and generates a context-aware response using Groq-powered Llama 3 large language models.

**4. Essay Grading and Feedback Generation**

* **Rubric Selection:** Students can select predefined rubrics such as IELTS or TOEFL, or upload custom rubrics provided by instructors.
* **Essay Evaluation:** The system analyzes the essay against the selected rubric criteria using AI-powered assessment.
* **Feedback Generation:** Cognify provides detailed feedback, highlighting strengths, weaknesses, and areas for improvement while aligning comments with the rubric requirements.

### Core Technologies

* Groq API (Llama 3 Models)
* Hugging Face Sentence Transformers
* FAISS Vector Database
* LangChain
* Python
* Flask
* Natural Language Processing (NLP)

### Key Inputs

#### Cognify Document Assistant

* Upload one or more PDF documents.
* Ask questions related to the uploaded content.
* Receive context-aware answers generated from the document knowledge base.

#### Essay Grading Module

* Select a predefined rubric (IELTS, TOEFL, etc.) or upload a custom rubric.
* Submit an essay for evaluation.
* Receive AI-generated scoring, feedback, and improvement suggestions based on the chosen rubric.


## Architecture:

![image](https://github.com/user-attachments/assets/2d9220ce-9573-4a09-9aa5-85d26747750e)

-### Step 1: Document Upload and Processing

Once a document is uploaded, Cognify automatically extracts the textual content from the PDF and processes it into smaller, manageable text chunks. This chunking process improves information retrieval efficiency and enables accurate context-based responses.

### Step 2: Embedding Generation and Semantic Indexing

The processed text chunks are converted into vector embeddings using Hugging Face Sentence Transformer models. These embeddings capture the semantic meaning and relationships within the text. The generated vectors are then stored and indexed using FAISS, enabling fast and efficient semantic search across the document content.

### Step 3: Query Processing and Response Generation

When a user submits a query, Cognify performs semantic search on the FAISS index to retrieve the most relevant document context. The retrieved context, along with the user's question, is then passed to a Groq-powered Llama 3 Large Language Model (LLM), which generates a context-aware and comprehensive response based on the document content.


## Product Demo:

![image](https://github.com/user-attachments/assets/00381e40-4305-4cf5-afad-3a6881d6b262)

![image](https://github.com/user-attachments/assets/05f9aa99-447e-444e-9e9e-45455eafda61)

## Product Report:

Cognify represents a significant step towards leveraging AI to create a more engaging and effective learning experience for students, empowering them to excel in their academic pursuits.
