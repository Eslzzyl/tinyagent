import os

from dotenv import load_dotenv
from prompt_toolkit import prompt

from src.agent import Agent
from src.client import Client
from src.tooling.tool import read, write

load_dotenv()


def main():
    client = Client(
        base_url=os.environ["OPENAI_BASE_URL"],
        api_key=os.environ["OPENAI_API_KEY"],
        model=os.environ["OPENAI_MODEL_NAME"],
    )
    agent = Agent(client=client, tools=[read, write])
    request = prompt("Your Message:")
    agent.run(request=request)


if __name__ == "__main__":
    main()
