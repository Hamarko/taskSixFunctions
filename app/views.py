from app import app
from flask import  jsonify, request
from .functions import constructor

@app.route('/start', methods=["GET"])
def index():
    json_data = request.json    
    data = json_data["data"]
    rule = json_data["rule"]
    result = []
    i = 0 
    for n in data:
        result.append(constructor (rule[i],n))
        i+=1
        if i == len(rule): i = 0
    return jsonify (result= result)