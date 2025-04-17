import os
import sys
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.linkedin import scrape_linkedin_data
from agents.linkedin_lookup_agent import lookup
from output_parsers import summary_parser, Summary
from typing import Tuple, List, Dict, Any


def linkedin_summary_agent(name: str) -> Tuple[Summary, str]:

    linkedin_url = lookup(name="nithin vadekkapat")

    linkedin_data = scrape_linkedin_data(url=linkedin_url, mock=True)

    summary_template = """ given the linkedin information{linkedin_data} about a person i want to create :
    1. A short summary
    2. two interesting facts about them
    \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_data"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    chain = summary_prompt_template | llm | summary_parser
    res: Summary = chain.invoke(input={"linkedin_data": linkedin_data})

    return res, linkedin_data.get("photoUrl")


if __name__ == "__main__":
    load_dotenv()
    print("Hello Langchain")
