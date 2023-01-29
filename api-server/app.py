import json
from flask import Flask, request, jsonify, Response, render_template
from enum import Enum
import re

app = Flask(__name__)


@app.route("/patients/identifier", methods=["GET"])
def get_patient_id():
    name = request.args.get("name")
    dob = request.args.get("dob")
    gender = request.args.get("gender")

    if not validate(name) or not validate(dob) or not validate(gender):
        return Response("Input invalid", 400)

    id = identifier_formatting(name, dob, gender)

    identifier = {"identifier": id}

    return jsonify(identifier)


@app.route("/identity", methods=["POST"])
def save_identifier():
    id = request.json["identifier"]
    error = {"error": ""}
    try:
        if not validate_id(id):
            error["error"] = "Invalid input"
            return Response(json.dumps(error), 400)

        if id == "VIKO1988M" or id == "JO1997M":
            error["error"] = "The record already exists"
            return Response(json.dumps(error), 409)

    except:
        error["error"] = "Error in saving record"
        return Response(error, 500)

    return jsonify("{}")


@app.route("/identity", methods=["GET"])
def get_identifier():
    id = request.args.get("identifier")
    error = {"error": ""}

    if not validate_id(id):
        error["error"] = "Invalid input"
        return Response(json.dumps(error), 400)

    if id == "AP1989M":
        user = {"name": "Apollo", "dob": "1989", "gender": "Male"}
        return jsonify(user)

    if id == "MHDH1988M":
        user = {"name": "Mahendersingh Dhoni", "dob": "1988", "gender": "Male"}
        return jsonify(user)

    if id == "JURO1979F":
        user = {"name": "Julia Roberts", "dob": "1979", "gender": "Female"}
        return jsonify(user)

    if id == "JO1997M":
        user = {"name": "John", "dob": "1997", "gender": "Male"}
        return jsonify(user)

    if id == "VIKO1988M":
        user = {"name": "Virat Kohli", "dob": "1988", "gender": "Male"}
        return jsonify(user)

    error["error"] = "Not found"
    return Response(json.dumps(error), 404)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/searchresults")
def searchresults():
    id = request.args.get("identifier")
    error = {"error": ""}
    user = {}

    if not validate_id(id):
        error["error"] = "Invalid patient id"
        return render_template('search-results.html',err_msg=error["error"], id=id)

    if id == "AP1989M":
        user = {"name": "Apollo", "dob": "1989", "gender": "Male"}
        return render_template('search-results.html',name=user["name"],dob=user["dob"],gender=user["gender"])

    if id == "MHDH1988M":
        user = {"name": "Mahendersingh Dhoni", "dob": "1988", "gender": "Male"}
        return render_template('search-results.html',name=user["name"],dob=user["dob"],gender=user["gender"])

    if id == "JURO1979F":
        user = {"name": "Julia Roberts", "dob": "1979", "gender": "Female"}
        return render_template('search-results.html',name=user["name"],dob=user["dob"],gender=user["gender"])

    if id == "JO1997M":
        user = {"name": "John", "dob": "1997", "gender": "Male"}
        return render_template('search-results.html',name=user["name"],dob=user["dob"],gender=user["gender"])

    if id == "VIKO1988M":
        user = {"name": "Virat Kohli", "dob": "1988", "gender": "Male"}
        return render_template('search-results.html',name=user["name"],dob=user["dob"],gender=user["gender"])

    error["error"] = "No patient matches the identifier"
    return render_template('search-results.html',err_msg=error["error"], id=id)
    

def identifier_formatting(name, dob, gender):
    namearray = name.split(" ")
    id = ""
    for x in namearray:
        id = id + x[:2].upper()
    id = id + dob[:4]
    id = id + gender[:1].upper()
    return id


def validate(val: str) -> bool:
    if val is None:
        return False

    if val == "" or val == " ":
        return False

    return True


def validate_id(id: str) -> bool:
    pattern = "^[A-Z]+[0-9]{4}[M|F]{1}$"

    if len(re.findall(pattern, id)) == 0:
        return False

    return True
