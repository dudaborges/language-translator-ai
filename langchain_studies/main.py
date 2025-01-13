import os

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
os.getenv('OPENAI_API_KEY')

messages = [
    SystemMessage('Traduza o texto a seguir para o Inglês'),
    HumanMessage('Olá, mundo!'),
]

model = ChatOpenAI(model='gpt-4o-mini')
parser = StrOutputParser()

template_message = ChatPromptTemplate.from_messages(
    [
        ('system', 'Translate the text to {language}'),
        ('user', '{text}'),
    ]
)

chain = template_message | model | parser
