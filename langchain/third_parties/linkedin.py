import os
import requests
from dotenv import load_dotenv


def scrap_linkedin_data(url: str, mock: bool = False) -> str:

    if mock:
        url = "https://gist.githubusercontent.com/nv-mldev/70816c80a61eb7cc4bde51e5657505cf/raw/7da3b8ee12f1bc1720a9765cbd3c2d502e46b764/nithin.json"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            return "Error: Unable to fetch data"
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "api_key": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": url,
        }
        response = requests.get(api_endpoint, params=params, timeout=10)

        data = response.json().get("person")

        return data


if __name__ == "__main__":
    load_dotenv()
    data = scrap_linkedin_data(
        url="https://www.linkedin.com/in/nithin-vadekkapat-7a089824/"
    )
    print(data)
