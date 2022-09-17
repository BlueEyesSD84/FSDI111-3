from flask import (
    Flask,
    request
)

app = Flask(__name__)

from app.database import data_type

@app.get("/data_types")
def index():
    out = data_type.scan()
    return out

@app.get("/data_types/integers")
def integers():
    out = data_type.select_by_type(name="Integer")
    return out

@app.get("/data_types/floats")
def floats():
    out = data_type.select_by_type(name="Float")
    return out

@app.get("/data_types/strings")
def strings():
    out = data_type.select_by_type(name="Strings")
    return out

@app.get("/data_types/booleans")
def bools():
    out = data_type.select_by_type(name="Boolean")
    return out

@app.get("/data_types/lists")
def lists():
    out = data_type.select_by_type(name="List")
    return out

@app.get("/data_types/dictionary")
def dictionary():
    out = data_type.select_by_type(name="Dictionary")
    return out

@app.get("/data_types/tuple")
def tuple():
    out = data_type.select_by_type(name="Tuple")
    return out



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