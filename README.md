# PDF_TO_CLI_CHATBOT
## Overview

This project implements a console-based AI chatbot leveraging generative AI techniques to provide accurate, informative responses while mitigating hallucinations. The chatbot utilizes external PDF documents and a vector database for enhanced reliability.

Interact with any PDF file from the terminal without using Langchain or LlamaIndex. At times you do not need frameworks like Langchain, this is a demo of how you can build a simple CLI chatbot without relying on LLM frameworks.

For any textual knowledge base (in our case, PDFs), we first need to extract text snippets from the knowledge base and use an embedding model to create a vector store representing the semantic content of the snippets. When a question is asked, we estimate its embedding and find relevant snippets using an efficient similarity search from vector stores. After extracting the snippets, we engineer a prompt and generate an answer using the LLM generation model. The prompt can be tuned based on the specific LLM used.

# Tech stack Implemented

1. Python Argparse for CLI
2. ChromaDB as vector database
3. OpenAI gpt-4
# Chatbot Project

## Features

- **Generative AI:** Utilizes OpenAI's GPT-4 Turbo model for generating responses.
- **Document Handling:** Integrates a PDF parser to extract text from external PDF documents.
- **Vector Database Integration:** Uses ChromaDB as a vector database to store and retrieve information efficiently.
- **Hallucination Mitigation:** Implements strategies to cross-reference responses with the knowledge base to verify information.
- **Console-Based Interaction:** Provides a simple console-based interface for user interaction.

## Prerequisites:
1. Python (Version 3.7 or later)
2. Git (Optional but recommended)
## Steps:
### Clone the Repository:

### 1. Clone the Repository


1) git clone <repository-url>

If you don't have Git installed, you can download the repository as a ZIP file from the repository's webpage and extract it to a local folder.

### Navigate to the Project Directory:

Change your current working directory to the project folder:




2) cd pdf-processing-chatbot


### Create a Virtual Environment:

It's a good practice to use a virtual environment to manage dependencies. Create a virtual environment:





3) python -m venv venv

### Activate the Virtual Environment:

Activate the virtual environment:




4) .\venv\Scripts\activate


### Install Dependencies:

Install the required Python packages using pip:




5) pip install -r requirements.txt

### Set Up OpenAI API Key:

Obtain an API key from OpenAI and replace <OPENAI-API-KEY> in the code with your actual API key.

### Run the Streamlit App:

Run the following command to launch the Streamlit app:




6) streamlit run app.py

This will start a local development server, and you can view the app by visiting the provided URL (usually http://localhost:8501) in your web browser.

### Interact with the App:

Upload a PDF file using the provided file uploader.
Set the word limit for text chunks and ask a question.
Click the "Process" button to trigger the chatbot's actions.
