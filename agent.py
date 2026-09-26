import streamlit as st
from google import genai

from tools import (
    calculator,
    create_study_plan,
    get_current_time
)

from rag import search_chunks


class GenAIAgent:

    def __init__(self):

        # Get Gemini API key
        api_key = st.secrets["GEMINI_API_KEY"]

        # Create Gemini client
        self.client = genai.Client(
            api_key=api_key
        )

        # Gemini model
        self.model = "gemini-3.5-flash-lite"

        # Conversation memory
        self.history = []

        # RAG document chunks
        self.document_chunks = []

    def set_document(self, chunks):
        """Store document chunks for RAG."""
        self.document_chunks = chunks

    def ask_gemini(self, prompt):
        """Send a prompt to Gemini."""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text

    def ask(self, user_message):

        message = user_message.lower().strip()

        # --------------------------------
        # TOOL 1: CALCULATOR
        # --------------------------------

        if message.startswith("calculate "):

            expression = user_message[
                10:
            ].strip()

            result = calculator(
                expression
            )

            return f"🧮 Calculator Result: {result}"

        # --------------------------------
        # TOOL 2: STUDY PLAN
        # --------------------------------

        if "study plan" in message:

            subject = "General Studies"
            hours = 2

            if " for " in message:

                subject = user_message.split(
                    " for ",
                    1
                )[1]

            for number in range(1, 13):

                if f"{number} hour" in message:

                    hours = number
                    break

            result = create_study_plan(
                subject,
                hours
            )

            return result

        # --------------------------------
        # TOOL 3: CURRENT TIME
        # --------------------------------

        if (
            "current time" in message
            or "what time is it" in message
            or "current date" in message
        ):

            result = get_current_time()

            return (
                f"🕒 Current date and time: "
                f"{result}"
            )

        # --------------------------------
        # RAG
        # --------------------------------

        context = ""

        if self.document_chunks:

            relevant_chunks = search_chunks(
                self.document_chunks,
                user_message
            )

            if relevant_chunks:

                context = "\n\n".join(
                    relevant_chunks
                )

        # --------------------------------
        # MEMORY
        # --------------------------------

        self.history.append(
            f"User: {user_message}"
        )

        conversation = "\n".join(
            self.history[-10:]
        )

        # --------------------------------
        # AI PROMPT
        # --------------------------------

        prompt = f"""
You are a helpful GenAI Study and Career Assistant.

Your job is to understand the user's task,
use available information, and provide a
clear and useful response.

If document context is provided, use it
to answer the question.

If the answer is not available in the
document, clearly say so and then provide
general knowledge when appropriate.

DOCUMENT CONTEXT:
{context}

CONVERSATION:
{conversation}

USER QUESTION:
{user_message}

Give a clear, simple and accurate answer.
"""

        response = self.ask_gemini(
            prompt
        )

        # Save response to memory
        self.history.append(
            f"Assistant: {response}"
        )

        return response