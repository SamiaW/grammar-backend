from flask import Flask
from flask import request, jsonify
from temp import description_search
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods = ['GET'])
def get_api():
    return 'get api call'

@app.route('/', methods = ['POST'])
def post_api():
    skill = request.get_json()['skills']
    job_description = request.get_json()['job_description']
    print(skill)
    retval = description_search(skill, job_description)
    return jsonify(retval)


if __name__ == '__main__':
    app.run()
