import os 
import sys
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool 
from langchain.agents import (
    create_react_agent, 
    AgentExecutor
)
from langchain import hub

from tools.tools import get_profile_url_tavily



load_dotenv()


def lookup(name: str, place: str) -> str:
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    
    template = """given the full_name {name_of_person} and place {place}I want you to get me a link of their Linkedin profile page. 
    Your answer should contain only a URL"""
    
    template_prompt = PromptTemplate(template=template,input_variables=["name_of_person", "place"])
    
    tools_for_agent = [Tool(name="Crawl Goolge 4 linkedin profile page", func=get_profile_url_tavily, description="useful for when need you to get Linkedin page URL")]
    
    react_prompt = hub.pull("hwchase17/react")
    
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    
    result = agent_executor.invoke(input={"input":template_prompt.format_prompt(name_of_person=name, place=place)})
    
    linkedin_url = result["output"]
    
    return linkedin_url 


if __name__ == "__main__":
    
   
    linkedin_url = lookup(name="Nithin Vadekkapat", place="India")
    print(linkedin_url)