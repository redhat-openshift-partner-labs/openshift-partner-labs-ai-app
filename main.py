"""
Simple Agno Chat AgentOS using GPT-OSS 20B model
"""
import os

from agno.agent import Agent
from agno.os import AgentOS
from agno.models.vllm import VLLM

from dotenv import load_dotenv

load_dotenv()


"""Run a simple chat agent using GPT-OSS 20B model."""

# Create an agent with GPT-OSS 20B model
agent = Agent(
    model=VLLM(base_url=os.environ.get("GPTOSS_ENDPOINT"), id="gpt-oss"),
    description="A helpful AI assistant powered by gpt-oss 20b model",
    instructions=[
        "You are a helpful AI assistant.",
        "Provide clear and concise responses to user queries.",
        "Be friendly and professional."
    ],
    markdown=True,
)

# Run the agent in interactive mode
agent_os = AgentOS(
    id="opl",
    description="OpenShift Partner Labs",
    agents=[agent]
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="main:app", reload=True)
