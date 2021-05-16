from api_function import app
from flask import  jsonify, request
from api_function.functions import constructor

@app.route('/function', methods=["GET"])
def api_function():
    json_data = request.json    
    data = json_data["data"]
    rule = json_data["rule"]
    result = []
    i = 0 
    for i, x in enumerate(data):
        result.append(constructor(rule[i % len(rule)], x))    
    return jsonify(result= result)