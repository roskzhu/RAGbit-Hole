from flask import Flask, jsonify
import cohere
from flask import Flask, request
from flask_cors import CORS
from google.cloud import storage
import time

app = Flask(__name__)
#CORS(app, resources={r"/download_mp3": {"origins": "*"}, r"/get_question": {"origins": "*"}, r"/feedback": {"origins": "*"}})

question_spawned = ""
feedback_master=""

# Initialize the Google Cloud Storage client
storage_client = storage.Client()

# Create a transcriber object.
transcriber = aai.Transcriber()

@app.route('/', methods=['GET', 'POST'])
def welcome():
    print("Hello Cohere!")
    global feedback_master
    feedback_master="initialized"
    print(f"feedback_master: {feedback_master}")
    return "Hello Cohere!"


if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=105)