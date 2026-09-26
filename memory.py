# memory.py

# Simple in-memory storage for the Study Tutor
# This avoids the CrewAI Memory import compatibility issue.

conversation_history = []


def create_memory():
    return conversation_history


def add_to_memory(question, answer):
    conversation_history.append({
        "question": question,
        "answer": answer
    })


def get_memory():
    return conversation_history
