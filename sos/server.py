from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/listar_tutoriais")
def listar_tutoriais():
    return redirect(sitee.html)

@app.route("/ir_home")
def return_home():
    return redirect(SOS_solucoes.html)

app.run()