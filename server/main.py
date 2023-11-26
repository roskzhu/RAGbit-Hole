from flask import Flask, jsonify
from serp import SerpGenerator
from flask import Flask, request
from flask_cors import CORS
from google.cloud import storage
import time
import generate_questions as questions

import cohere_sample as bot

app = Flask(__name__)
# CORS(app, resources={r"/download_mp3": {"origins": "*"}, r"/get_question": {"origins": "*"}, r"/feedback": {"origins": "*"}})

# Initialize the Google Cloud Storage client
# storage_client = storage.Client()

# Create a transcriber object.

documents = None


@app.route('/', methods=['GET', 'POST'])
def welcome():
    print("Hello Cohere!")
    return jsonify({"response": "Hello Cohere!"})


@app.route('/initialize', methods=['GET', 'POST'])
def initialize():
    """
    # Step 1: Scrape Links
    serp = SerpGenerator()
    print("Initialized SERP Generator, launching search")
    results = serp.generate(request.args["query"])
    print("Scraping links")
    links = serp.get_links(results)
    print(links)
    """
    links = [{'title': 'Autonomous Agent - an overview | ScienceDirect Topics', 'url': 'https://www.sciencedirect.com/topics/computer-science/autonomous-agent'}, {'title': 'Which of the following is an example of artificial intelligent agent ... - Brainly', 'url': 'https://brainly.com/question/30143257'}, {'title': 'autonomous agency Definition | Law Insider', 'url': 'https://www.lawinsider.com/dictionary/autonomous-agency'}, {'title': 'Autonomous versus automated: What each means and why it matters', 'url': 'https://www.techrepublic.com/article/autonomous-versus-automated-what-each-means-and-why-it-matters/'}, {'title': 'Autonomous agent', 'url': 'https://en.wikipedia.org/wiki/Autonomous_agent'}, {'title': 'Autonomous Agent - an overview', 'url': 'https://www.sciencedirect.com/topics/computer-science/autonomous-agent'}, {'title': 'The Complete Beginners Guide To Autonomous Agents', 'url': 'https://www.mattprd.com/p/the-complete-beginners-guide-to-autonomous-agents'}, {'title': "Insight: Race towards 'autonomous' AI agents grips Silicon ...",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        'url': 'https://www.reuters.com/technology/race-towards-autonomous-ai-agents-grips-silicon-valley-2023-07-17/'}, {'title': 'ChatGPT, Next Level: Meet 10 Autonomous AI Agents ...', 'url': 'https://medium.com/the-generator/chatgpts-next-level-is-agent-ai-auto-gpt-babyagi-agentgpt-microsoft-jarvis-friends-d354aa18f21'}, {'title': 'Why You Need To Know About Autonomous AI Agents', 'url': 'https://www.kdnuggets.com/2023/06/need-know-autonomous-ai-agents.html'}, {'title': 'Autonomous Agents and Multi-Agent Systems', 'url': 'https://www.worldscientific.com/worldscibooks/10.1142/4399'}, {'title': 'An Introduction to Autonomous Agents', 'url': 'https://developer.salesforce.com/blogs/2023/10/an-introduction-to-autonomous-agents'}, {'title': 'What Are Autonomous Agents? And why are they the next ...', 'url': 'https://medium.com/geekculture/what-are-autonomous-agents-and-why-are-they-the-next-ai-wave-after-chatgpt-8e6dc651d2a'}, {'title': 'Autonomous Agents and Multi-Agent Systems | Home', 'url': 'https://www.springer.com/journal/10458'}]
    # Step 2: Embed Everything
    bot.initDocuments(links)
    # should just return success
    return jsonify({"response": "success"})


@app.route('/get_questions', methods=['GET', 'POST'])
def get_questions():
    initial_question = request.args["question"]
    print("Getting questions")
    response = questions.get_questions(initial_question)
    return jsonify({"response": response})


@app.route('/get_response', methods=['POST'])
def get_response():
    message = request.args["message"]
    response = bot.getResponse(message)
    # print("Chatbot:")
    # flag = False
    # for event in response:
    #     # Text
    #     if event.event_type == "text-generation":
    #         print(event.text, end="")

    #     # Citations
    #     if event.event_type == "citation-generation":
    #         if not flag:
    #             print("\n\nCITATIONS:")
    #             flag = True
    #         print(event.citations)

    # print(f"\n{'-'*100}\n")

    ret = {
        "text": response.text,
        "citations": response.citations,
        "documents": response.documents,
    }

    return ret


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=105)
