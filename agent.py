import os

from crewai import Agent, Task, Crew, Process, LLM

from tools import calculator, current_time
from memory import create_memory


# --------------------------------------------------
# GROQ LLM
# --------------------------------------------------

groq_llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)


# --------------------------------------------------
# MEMORY
# --------------------------------------------------

study_memory = create_memory()


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

    task = Task(

        description=f"""
        You are helping a student with their studies.

        Student level:
        {difficulty}

        Student question:
        {question}

        Follow these instructions:

        1. Answer the student's question directly.

        2. Adapt your explanation to the student's
           selected difficulty level.

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

        agents=[
            study_tutor
        ],

        tasks=[
            task
        ],

        process=Process.sequential,

        memory=study_memory,

        verbose=False
    )


    # --------------------------------------------------
    # RUN CREW
    # --------------------------------------------------

    result = crew.kickoff()


    return str(result)
