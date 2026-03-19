from fastmcp import FastMCP
from typing import Annotated
from pydantic import Field

# Create MCP server
mcp = FastMCP("Personal Trainer MCP Server")

# The middleware will be performd in the agent
# mcp.add_middleware(RequestLoggingMiddleware())



# ---------------------------
# TOOL 1: Generate workout plan
# ---------------------------
@mcp.tool()
def generate_workout_plan(
    goal: Annotated[str, Field(description="Fitness goal (e.g. lose weight, build muscle)")],
) -> str:
    """Generates a simple weekly workout plan based on the user's goal."""

    if "lose" in goal.lower():
        return "Workout plan: Cardio 3x/week + Full body strength 2x/week"
    elif "muscle" in goal.lower():
        return "Workout plan: Strength training 4x/week + light cardio"
    else:
        return "Workout plan: Balanced training 3-4x/week"


# ---------------------------
# TOOL 2: Get daily workout
# ---------------------------
@mcp.tool()
def get_daily_workout(
    day: Annotated[str, Field(description="Day of the week")],
) -> str:
    """Returns a workout suggestion for a specific day."""

    workouts = {
        "monday": "Chest and triceps",
        "tuesday": "Back and biceps",
        "wednesday": "Rest or light cardio",
        "thursday": "Legs",
        "friday": "Full body",
        "saturday": "Cardio",
        "sunday": "Rest",
    }

    return workouts.get(day.lower(), "Rest day")


# ---------------------------
# TOOL 3: Log workout
# ---------------------------
@mcp.tool()
def log_workout(
    exercise: Annotated[str, Field(description="Exercise name")],
    reps: Annotated[int, Field(description="Number of repetitions")],
) -> str:
    """Logs a workout activity (simulated)."""

    return f"Logged workout: {exercise} with {reps} reps."


# ---------------------------
# TOOL 4: Generate meal plan
# ---------------------------
@mcp.tool()
def generate_meal_plan(
    goal: Annotated[str, Field(description="Diet goal (e.g. weight loss, muscle gain)")],
) -> str:
    """Generates a simple meal plan."""

    if "loss" in goal.lower():
        return "Meal plan: High protein, low carbs, lots of vegetables"
    elif "muscle" in goal.lower():
        return "Meal plan: High protein, balanced carbs and fats"
    else:
        return "Meal plan: Balanced diet with whole foods"


# ---------------------------
# TOOL 5: Get progress summary
# ---------------------------
@mcp.tool()
def get_progress_summary() -> str:
    """Returns a simple progress summary (simulated)."""

    return "You completed 4 workouts this week. Great job!"


# ---------------------------
# Run server
# ---------------------------
if __name__ == "__main__":
    import asyncio

    asyncio.run(
        mcp.run_http_async(
            host="0.0.0.0",
            port=8001,
        )
    )