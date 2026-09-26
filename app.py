import streamlit as st
import tempfile

from agent import GenAIAgent
from rag import extract_text_from_pdf, split_text


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="GenAI Study & Career Assistant",
    page_icon="🤖",
    layout="centered"
)


# ---------------- TITLE ----------------

st.title("🤖 GenAI Study & Career Assistant")

st.write(
    "An AI assistant powered by Gemini with "
    "RAG, tools, memory and agent-based workflows."
)


# ---------------- AGENT ----------------

if "agent" not in st.session_state:

    try:
        st.session_state.agent = GenAIAgent()

    except Exception as e:
        st.error(f"Agent initialization failed: {e}")
        st.stop()


# ---------------- CHAT MEMORY ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------- PDF UPLOAD ----------------

st.sidebar.header("📚 Upload Study Material")

uploaded_file = st.sidebar.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)


if uploaded_file:

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(
                uploaded_file.getvalue()
            )

            pdf_path = temp_file.name

        text = extract_text_from_pdf(
            pdf_path
        )

        chunks = split_text(text)

        st.session_state.agent.set_document(
            chunks
        )

        st.sidebar.success(
            "PDF loaded successfully! ✅"
        )

        st.sidebar.write(
            f"📄 Text chunks: {len(chunks)}"
        )

    except Exception as e:

        st.sidebar.error(
            f"Could not process PDF: {e}"
        )


# ---------------- DISPLAY CHAT ----------------

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


# ---------------- USER INPUT ----------------

user_input = st.chat_input(
    "Ask your AI assistant..."
)


if user_input:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner(
            "AI Agent is thinking..."
        ):

            try:

                response = (
                    st.session_state.agent.ask(
                        user_input
                    )
                )

                st.write(response)

                # Store assistant response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )