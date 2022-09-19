from flask import (
    Flask,
    request
)

app = Flask(__name__)

from app.database import data_type

RESPONSE = {
    "status": "ok"
}

@app.get("/data_types")
def index():
    response = RESPONSE
    response["data_types"] = data_type.scan()
    return response

@app.get("/data_types/integers")
def integers():
    response = RESPONSE
    response["data_type"] = data_type.select_by_type(name="Integers")
    return response

@app.get("/data_types/floats")
def floats():
    response = RESPONSE
    response["data_type"] = data_type.select_by_type(name="Float")
    return response

@app.get("/data_types/strings")
def strings():
    response = RESPONSE
    response["data_type"] = data_type.select_by_type(name="Strings")
    return response

@app.get("/data_types/booleans")
def bools():
    response = RESPONSE
    response["data_type"] = data_type.select_by_type(name="Boolean")
    return response

@app.get("/data_types/lists")
def lists():
    response = RESPONSE
    response["data_type"] = data_type.select_by_type(name="List")
    return response

@app.get("/data_types/dictionary")
def dictionary():
    response = RESPONSE
    response["data_type"] = data_type.select_by_type(name="Dictionary")
    return response

@app.get("/data_types/tuple")
def tuple():
    response = RESPONSE
    response["data_type"] = data_type.select_by_type(name="Tuple")
    return response


@app.post("/data_types")#to post new records to /
def create_data_type():
    dt_body = request.json
    data_types.create(dt_body)
    return "",204  #204 reprents a successful operation

@app.put("/data_types/<int:pk>")
def update_data_type(pk):
    dt_body = request.json
    data_types.update(dt_body, pk)
    return "", 204

@app.delete("/data_types/<int:pk>")
def delete_data_type(pk):
    data_types.delete(pk)
    return "", 204