import cohere_sample as bot
from flask import Flask, jsonify
from serp import SerpGenerator
from flask import Flask, request
from flask_cors import CORS
# from google.cloud import storage
import time
import generate_questions as questions
# import assemblyai as aai
import os
import json
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

CORS(app, resources={r"/get_questions": {"origins": ""},
     r"/initialize": {"origins": ""}, r"/get_response": {"origins": "*"}})

# CORS(app, resources={r"/download_mp3": {"origins": "*"}, r"/get_question": {"origins": "*"}, r"/feedback": {"origins": "*"}})

# Initialize the Google Cloud Storage client
# storage_client = storage.Client()

# yapping_sources = []

# Create a transcriber object.

# aai.settings.api_key = os.environ["AAI_API_KEY"]

# Create a transcriber object.

documents = None


@app.route('/', methods=['GET', 'POST'])
def welcome():
    print("Hello Cohere!")
    return jsonify({"response": "Hello Cohere!"})


@app.route('/initialize', methods=['GET', 'POST'])
def initialize():
    # global yapping_sources

    # Step 1: Scrape Links
    serp = SerpGenerator()
    print("Initialized SERP Generator, launching search")
    results = serp.generate(request.args["query"])
    print("Scraping links")
    links = serp.get_links(results)
    # links.append(yapping_sources)
    print(links)
    # links = [{'title': 'Autonomous Agent - an overview | ScienceDirect Topics', 'url': 'https://www.sciencedirect.com/topics/computer-science/autonomous-agent'}, {'title': 'Which of the following is an example of artificial intelligent agent ... - Brainly', 'url': 'https://brainly.com/question/30143257'}, {'title': 'autonomous agency Definition | Law Insider', 'url': 'https://www.lawinsider.com/dictionary/autonomous-agency'}, {'title': 'Autonomous versus automated: What each means and why it matters', 'url': 'https://www.techrepublic.com/article/autonomous-versus-automated-what-each-means-and-why-it-matters/'}, {'title': 'Autonomous agent', 'url': 'https://en.wikipedia.org/wiki/Autonomous_agent'}, {'title': 'Autonomous Agent - an overview', 'url': 'https://www.sciencedirect.com/topics/computer-science/autonomous-agent'}, {'title': 'The Complete Beginners Guide To Autonomous Agents', 'url': 'https://www.mattprd.com/p/the-complete-beginners-guide-to-autonomous-agents'}, {'title': "Insight: Race towards 'autonomous' AI agents grips Silicon ...",
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


# @app.route('/download_mp3', methods=['POST'])
# def download_mp3():
#     transcriber = aai.Transcriber()
#     bucket_name = "rabbithole-406318.appspot.com"
#     blob_name = "audio.webm"
#     # Get the bucket and blob
#     print("getting bucket")
#     bucket = storage_client.get_bucket(bucket_name)
#     print(f"got bucket: {bucket}, getting blob")
#     blob = bucket.blob(blob_name)
#     print(f"got blob: {blob}, getting webm")
#     print("getting aai")
#     transcript = transcriber.transcribe(
#         "https://storage.cloud.google.com/rabbithole-406318.appspot.com/audio.webm")
#     print(f"got response, getting text, {transcript}")
#     text = transcript.text
#     print(f"text: {text}")

#     epoch_time = str(int(time.time()))
#     new_blob_name = f'audio_{epoch_time}.webm'
#     print(f"renaming file to {new_blob_name}")
#     bucket.rename_blob(blob, new_blob_name)
#     # INSERT APPENDING TO GLOBAL SOURCES
#     transcribed = {
#         "title": f"User-Recorded File TRANSCRIPT: {text}",
#         "url": f"https://storage.cloud.google.com/rabbithole-406318.appspot.com/audio.webm"
#     }
#     global yapping_sources
#     yapping_sources.append(transcribed)
#     return jsonify({"response": text})


# @app.route('/see_user_inputs', methods=['GET', 'POST'])
# def see_user_inputs():
#     global yapping_sources
#     return jsonify({"response": yapping_sources})


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=105)
