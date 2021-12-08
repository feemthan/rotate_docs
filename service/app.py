import requests
import json

from flask import Flask, request, jsonify

from rotate_score  import score

app = Flask(__name__)

@app.route('/status', methods=["GET"])
def health_check():
    return jsonify(status='ok'), 200

@app.route('/rns', methods=["POST"])
def rotate():
    '''
    INPUT
    {
        'file_path': 'Path_here.jpg'
    }
    '''
    body = request.json
    file_path = body['file_path']

    if isinstance(file_path, str):
        file_path = [file_path]

    # out_path = []
    for item in file_path:
        score(item)
        # out_path.append(out_path)

    return jsonify(status='SUCCESS', input=file_path), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8010, debug=True)