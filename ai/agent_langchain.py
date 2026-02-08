from json import load
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from django.conf import settings
from abc import abstractmethod
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

class BaseAgent(ABC):
    llm =  ChatOpenAI(model_name="gpt-4.1-mini")
    language: str = "pt-br"

    @abstractmethod
    def _prompt(self):
        pass

    @abstractmethod
    def run(self):
        pass