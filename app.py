from flask import Flask, request, redirect, render_template, jsonify, make_response
import os
import random

app = Flask(__name__)

try:
    FLAG = open('./prob/flag.txt', 'r').read()
except:
    FLAG = 'ㅍㅡㄹㄹㅐㄱㅡzz'

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
    os.popen(f"docker run --rm -p {port}:80 wargame")
    return render_template("index.html", link="http://localhost:" + str(port))

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port="80")
