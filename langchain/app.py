from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from ice_breaker import linkedin_summary_agent

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


@app.route("/process", methods=["POST"])
def process():
    name = request.json().get("name")
    summary, profile_pic_link = linkedin_summary_agent(name)
    return jsonify(
        {
            "summary": summary, 
            "profile_pic_link": profile_pic_link
        }
    )


if __name__ == "__main__":

    app.run(port=8001, debug=True)
