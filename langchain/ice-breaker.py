import os
import sys
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_data
from agents.linkedin_lookup_agent import lookup

if __name__ == "__main__":
    load_dotenv()
    print("Hello Langchain")

    summary_template = """ given the information{information} about a person i want to create :
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    parser = StrOutputParser()
    chain = summary_prompt_template | llm | parser
    information = scrape_linkedin_data(url=lookup(name="nithin vadekkapat", place="India"))
    res = chain.invoke(input={"information": information})
    print(res)
