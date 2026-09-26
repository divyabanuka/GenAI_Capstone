# 🤖 GenAI Study & Career Assistant

An AI-powered Study & Career Assistant built using Python, Streamlit, Google Gemini API, RAG, tools, memory, and agent-based workflows.

The application helps students ask questions, analyze uploaded study material, generate study plans, perform calculations, and get AI-powered assistance through an interactive interface.

## 🌐 Live Demo

🔗 https://genaicapstone-tkco4ug4rgpt6llsygszgv.streamlit.app/

## 💻 GitHub Repository

🔗 https://github.com/divyabanuka/GenAI_Capstone

## 🚀 Features

- 🤖 AI-powered study and career assistant
- 📄 Upload and analyze PDF study material
- 🔎 Retrieval-Augmented Generation (RAG)
- 🧠 Conversation memory
- 🛠️ Tool-based task execution
- 📚 Study plan generator
- 🧮 Calculator tool
- 🕒 Current date and time tool
- 💬 Natural language interaction
- 🖥️ Interactive Streamlit interface
- 🔐 Secure Gemini API key management using Streamlit Secrets

## 📄 RAG – Study Material

Users can upload a PDF containing study material.

The application:

1. Accepts the PDF
2. Extracts text from the document
3. Splits the content into text chunks
4. Retrieves relevant information
5. Uses the retrieved information as context
6. Generates an answer using Google Gemini

Example:

What is the main topic of the uploaded PDF?

The assistant uses the uploaded document to provide a relevant answer.

## 🛠️ AI Tools

### 🧮 Calculator

The calculator tool performs mathematical calculations.

Example:

calculate 125*48

Result:

6000

### 📚 Study Plan Generator

Creates a study plan based on the subject and available study time.

Example:

Create a study plan for Machine Learning for 2 hours

Example result:

- 45 minutes - Learn concepts
- 45 minutes - Practice problems
- 30 minutes - Revision and notes

### 🕒 Current Time

Provides the current date and time.

Example:

What is the current time?

## 🧠 Agent Workflow

The project follows an agent-based workflow:

Understand Task
       ↓
Decide Action
       ↓
Use Tool / Retrieve Information
       ↓
Process Result
       ↓
Generate Response
       ↓
Respond to User

This demonstrates how an AI agent can understand a user's request, select an appropriate action, use tools or retrieved information, and generate a response.

## 🔎 RAG Workflow

Upload PDF
     ↓
Extract Text
     ↓
Create Text Chunks
     ↓
Retrieve Relevant Information
     ↓
Send Context to Gemini
     ↓
Generate Answer

## 🧠 Memory

The assistant maintains conversation context during the session to provide more relevant responses.

This allows users to continue asking related questions without repeating all the previous information.

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- PyPDF
- Retrieval-Augmented Generation (RAG)
- Git
- GitHub

## 📁 Project Structure

GenAI_Capstone/
│
├── app.py
├── agent.py
├── rag.py
├── tools.py
├── requirements.txt
├── .gitignore
│
├── data/
│
└── .streamlit/
    └── secrets.toml

## 📦 Installation

Clone the repository:

git clone https://github.com/divyabanuka/GenAI_Capstone.git

Move into the project directory:

cd GenAI_Capstone

Install the required packages:

pip install -r requirements.txt

## 🔑 API Key Configuration

Create the following file:

.streamlit/secrets.toml

Add your Gemini API key:

GEMINI_API_KEY = "YOUR_API_KEY"

⚠️ Never upload or share your actual API key publicly.

The secrets.toml file is excluded from GitHub using .gitignore.

## ▶️ Run the Application

Run the Streamlit application:

python -m streamlit run app.py

The application will open in your browser.

## ☁️ Deployment

The application is deployed using Streamlit Community Cloud.

### Live Application

https://genaicapstone-tkco4ug4rgpt6llsygszgv.streamlit.app/

## 🎯 Project Objectives

This project demonstrates practical understanding of:

- AI Agents
- Agent workflows
- Tool usage
- Function-based actions
- Retrieval-Augmented Generation
- State and memory management
- LLM integration
- PDF document processing
- AI-powered automation
- Streamlit application development
- Secure API key management

## 🎓 Codomax Digital – Module 6

This project was developed as part of Module 6 – GenAI Capstone Project of the Codomax Digital internship.

The project integrates:

- LLM API
- Prompt Engineering
- RAG
- Tools
- Agent workflow
- Memory
- Streamlit deployment

## 🔐 Safety and Limitations

- API keys are stored using Streamlit Secrets.
- Sensitive credentials should never be committed to GitHub.
- AI-generated responses may occasionally contain incorrect information.
- Important information should be verified before relying on it.
- Uploaded documents should not contain sensitive personal information.

## 👩‍💻 Author

Divya Banuka

Artificial Intelligence & Machine Learning (AIML)

## ⭐ Project Links

Live Demo:
https://genaicapstone-tkco4ug4rgpt6llsygszgv.streamlit.app/

GitHub:
https://github.com/divyabanuka/GenAI_Capstone