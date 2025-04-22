import os
import sys
from dotenv import load_dotenv
from agents.linkedin_lookup_agent import lookup
from third_parties.linkedin import scrape_linkedin_data

load_dotenv()
data = scrape_linkedin_data(
    url="https://www.linkedin.com/in/nithin-vadekkapat-7a089824/"
)
print(data)


# lookup(name="Nithin Vadekkapat", place="India")
