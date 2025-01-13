from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()
os.getenv('OPENAI_API_KEY')

messages = [
    SystemMessage('Traduza o texto a seguir para o Inglês'),
    HumanMessage('Olá, mundo!')
]

model = ChatOpenAI(model='gpt-4o-mini')
parser = StrOutputParser()

template_message = ChatPromptTemplate.from_messages([
    ('system', 'Translate the text to {language}'),
    ('user', '{text}'),
])

chain = template_message | model | parser


# text_response = chain.invoke({'language': 'inglês', 'text': 'Olá, mundo!'})

# print(text_response)
