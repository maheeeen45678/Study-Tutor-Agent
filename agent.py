import os

from crewai import Agent, Task, Crew, Process, LLM

from tools import calculator, current_time
from memory import create_memory, add_to_memory, get_memory


# --------------------------------------------------
# GROQ LLM
# --------------------------------------------------

groq_llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)


# --------------------------------------------------
# STUDY TUTOR AGENT
# --------------------------------------------------

study_tutor = Agent(
    role="Study Tutor",

    goal=(
        "Help students understand academic concepts, "
        "answer questions clearly, create revision material, "
        "and adapt explanations according to the student's level."
    ),

    backstory=(
        "You are a patient and knowledgeable AI study tutor. "
        "You explain difficult concepts in simple language. "
        "You use examples when useful and help students "
        "understand concepts rather than simply memorize them."
    ),

    llm=groq_llm,

    tools=[
        calculator,
        current_time
    ],

    allow_delegation=False,

    verbose=False
)


# --------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------

def ask_study_tutor(question, difficulty="Beginner"):

    # Get previous conversation
    history = get_memory()

    previous_context = ""

    if history:
        previous_context = "\nPrevious conversation:\n"

        for item in history[-5:]:
            previous_context += (
                f"Student: {item['question']}\n"
                f"Tutor: {item['answer']}\n\n"
            )


    # --------------------------------------------------
    # CREATE TASK
    # --------------------------------------------------

    task = Task(

        description=f"""
You are helping a student with their studies.

Student level:
{difficulty}

Student question:
{question}

{previous_context}

Follow these instructions:

1. Answer the student's question directly.

2. Adapt your explanation to the selected
   difficulty level.

3. If the student is a Beginner, use simple
   language and examples.

4. Break difficult concepts into smaller parts.

5. If the question involves mathematics,
   use the Calculator tool.

6. If useful, use the Current Time tool.

7. Do not invent facts.

8. If something is uncertain, clearly state
   that it is uncertain.

9. Do not unnecessarily make the answer very long.

10. At the end, provide:

Key Revision Points:
- Point 1
- Point 2
- Point 3
""",

        expected_output=(
            "A clear and accurate educational answer "
            "appropriate for the selected student level, "
            "followed by 2-3 revision points."
        ),

        agent=study_tutor
    )


    # --------------------------------------------------
    # CREATE CREW
    # --------------------------------------------------

    crew = Crew(
        agents=[study_tutor],
        tasks=[task],
        process=Process.sequential,
        verbose=False
    )


    # --------------------------------------------------
    # RUN CREW
    # --------------------------------------------------

    result = crew.kickoff()

    answer = str(result)


    # --------------------------------------------------
    # SAVE MEMORY
    # --------------------------------------------------

    add_to_memory(question, answer)


    return answer


    
