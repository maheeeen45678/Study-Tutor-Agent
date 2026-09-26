from crewai.tools import tool
from datetime import datetime


# --------------------------------------------------
# CALCULATOR TOOL
# --------------------------------------------------

@tool("Calculator")
def calculator(expression: str) -> str:
    """
    Calculate a basic mathematical expression.

    Example:
    25 * 4
    """

    try:

        result = eval(
            expression,
            {"__builtins__": {}},
            {}
        )

        return f"The answer is {result}"

    except Exception:

        return (
            "I could not calculate this expression. "
            "Please provide a valid mathematical expression."
        )


# --------------------------------------------------
# CURRENT TIME TOOL
# --------------------------------------------------

@tool("Current Time")
def current_time() -> str:
    """
    Returns the current date and time.
    """

    return datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
