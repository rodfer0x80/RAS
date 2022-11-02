from flask import Flask, Blueprint, render_template, request, redirect


# Main
app = Flask(__name__)


# Paths
index_bp = Blueprint("index", __name__, template_folder='templates')
app.register_blueprint(index_bp)
@app.route("/", methods=["GET"])
def getIndex():
    return render_template("index.html")

# reads_bp = Blueprint("reads", __name__, template_folder='templates')
# app.register_blueprint(reads_bp) 
@app.route("/reads", methods=["POST"])
def postReads():
    data = request.form.get('reads')
    with open("links.txt", 'w') as f:
        for line in data.splitlines():
            f.write(f"{line}\n")
    return redirect("/model")

model_bp = Blueprint("model", __name__, template_folder='templates')
app.register_blueprint(model_bp) 
@app.route("/model", methods=["GET"])
def getModel():
    return render_template("model.html")  

links_bp = Blueprint("links", __name__, template_folder='templates')
app.register_blueprint(links_bp) 
@app.route("/links", methods=["GET"])
def getLinks():
    f = open("links.txt", 'r')
    content = f.read()
    f.close()
    return content

question_bp = Blueprint("questions", __name__, template_folder='templates')
app.register_blueprint(question_bp) 
@app.route("/questions", methods=["GET"])
def getQuestions():
    f = open("questions.txt", 'r')
    content = f.read()
    f.close()
    return content
@app.route("/question", methods=["POST"])
def postQuestion():
    data = request.form.get('question')
    with open("questions.txt", 'a') as f:
        for line in data.splitlines():
            f.write(f"{line}\n")
    return redirect("/model")