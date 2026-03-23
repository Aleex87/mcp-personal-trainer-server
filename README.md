# Personal Trainer MCP Server

This project implements a **Model Context Protocol (MCP) server** that provides fitness-related tools for an AI agent.

The server exposes multiple tools that allow an agent to:
- Generate workout plans
- Suggest daily exercises
- Provide meal plans
- Log workouts
- Track progress

---

## Features

- MCP-compliant server using `FastMCP`
- 5 structured tools with typed inputs
- Clean and simple architecture
- Ready to connect with a LangChain agent

---

## Project Structure

src/
main.py


---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/mcp-personal-trainer-server.git
cd mcp-personal-trainer-server

```

Initialize the project (if needed):

uv init 

Install dependencies:

uv sync

## Running the server

Start the MCP server:

uv run python src/main.py

The server will run at:

http://localhost:8001/mcp


## Available Tools

The MCP server exposes the following tools:

1. generate_workout_plan

Creates a weekly workout plan based on a fitness goal.

Input:

goal (string)

2. get_daily_workout

Returns a workout suggestion for a specific day.

Input:

day (string)

3. log_workout

Logs a workout activity.

Input:

exercise (string)
reps (integer)

4. generate_meal_plan

Creates a simple meal plan based on dietary goals.

Input:

goal (string)

5. get_progress_summary

Returns a basic summary of user progress.

Input:

none

## How It Works

This project follows the MCP architecture:

The MCP server exposes tools
An external agent connects via MCP client
The agent decides when to call a tool
The server executes the tool and returns results

The server itself does not contain any AI model.

## Design Considerations
All tool inputs are typed using Annotated and Field
Tools are deterministic and simple
No external APIs are used
Designed for educational purposes

## Author

Alessandro Abbate
