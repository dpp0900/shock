from flask import Flask, request, redirect, render_template, jsonify, make_response
import os
import random
import docker
import datetime

app = Flask(__name__)

try:
    FLAG = open('./prob/flag.txt', 'r').read()
except:
    FLAG = 'ㅍㅡㄹㄹㅐㄱㅡzz'

def remove_old_containers(age_limit_hours):
    client = docker.from_env()

    age_limit = datetime.timedelta(hours=age_limit_hours)
    age_limit_seconds = age_limit.total_seconds()

    containers = client.containers.list(all=True)

    for container in containers:
        start_time_str = container.attrs['Created']
        start_time = datetime.datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M:%S.%fZ')

        age = (datetime.datetime.utcnow() - start_time).total_seconds()

        if age > age_limit_seconds:
            container.stop()
            container.remove()

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", hint=0)
    if request.method == "POST":
        if request.form.get("flag") == FLAG:
            return "<script>alert(\"Correct!!\");location.href=\"portf\";</script>"
        else:
            return "<script>alert(\"Wrong!!\");history.back(-1);</script>"
@app.route("/hint")
def hint():
    return render_template("index.html", pf="pf")

@app.route("/portf")
def portf():
    with open("./templates/pf.pdf", "rb") as pdf:
        binary_pdf = pdf.read()
    response = make_response(binary_pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = \
        'inline; filename=portfolio.pdf'
    return response

@app.route("/prob")
def prob():
    port = random.randint(49152,65535)
    os.popen(f"docker run --rm -p {port}:80 shock")
    return render_template("index.html", link="http://localhost:" + str(port))

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port="80")
