import requests

from flask import (
    Flask,
    render_template,
    request)

app = Flask(__name__)

BACKEND_URL = "http://127.0.0.1:5000/data_types"

@app.get("/")
def index():
    response = requests.get(BACKEND_URL)
    scan_data = response.json().get("data_types")
    return render_template("data_type.html", data_types = scan_data)

@app.get("/integer")
def integer():
    url = "%s/%s" % (BACKEND_URL, "integers")
    response = requests.get(url)
    integer_data = response.json().get("data_type")
    return render_template("data_type.html", data_types = integer_data[0])

@app.get("/floats")
def floats():
    url = "%s/%s" % (BACKEND_URL, "floats")
    response = requests.get(url)
    float_data = response.json().get("data_type")
    return render_template("data_type.html", data_types = float_data[0])


@app.get("/booleans")
def booleans():
    url = "%s/%s" % (BACKEND_URL, "booleans")
    response = requests.get(url)
    booleans_data = response.json().get("data_type")
    return render_template("data_type.html", data_types = booleans_data[0])

@app.get("/strings")
def string():
    url = "%s/%s" % (BACKEND_URL, "strings")
    response = requests.get(url)
    strings_data = response.json().get("data_type")
    return render_template("data_type.html", data_types = strings_data[0])

@app.get("/lists")
def lists():
    url = "%s/%s" % (BACKEND_URL, "lists")
    response = requests.get(url)
    lists_data = response.json().get("data_type")
    return render_template("data_type.html", data_types = lists_data[0])

@app.get("/dictionary")
def dictionary():
    url = "%s/%s" % (BACKEND_URL, "dictionary")
    response = requests.get(url)
    dictionaries_data = response.json().get("data_type")
    return render_template("data_type.html", data_types = dictionaries_data[0])

@app.get("/tuple")
def tuple():
    url = "%s/%s" % (BACKEND_URL, "tuples")
    response = requests.get(url)
    tuples_data = response.json().get("data_type")
    return render_template("data_type.html", data_types = tuples_data[0])

@app.get("/table")
def table():
    return render_template("table.html")  

@app.get("/about")
def about():
    return render_template("about.html")  

@app.get("/create/data_types")
def get_data_type_form():
    return render_template("new.html")

@app.post("/create/data_types")
def create_data_type():
    form_data = requests.form
    new_dt = {
        "name": form_data.get("name"),
        "summary": form_data.get("summary"),
        "description": form_data.get("description")
    }
    response = requests.post(BACKEND_URL, json=new_dt)
    if response.status_code == 204:
        return render_template("new_success.html")
    else:
        return render_template("failed.html")