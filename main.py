import os

from dotenv import load_dotenv
from prompt_toolkit import prompt

from src.agent import Agent
from src.client import Client
from src.tool import read, tools, write

load_dotenv()


def main():
    client = Client(
        base_url=os.environ["OPENAI_BASE_URL"],
        api_key=os.environ["OPENAI_API_KEY"],
        model=os.environ["OPENAI_MODEL_NAME"],
    )
    agent = Agent(client=client, tools=[read, write], tool_spec_list=tools)
    request = prompt("Your Message:")
    agent.run(request=request)


if __name__ == "__main__":
    main()
