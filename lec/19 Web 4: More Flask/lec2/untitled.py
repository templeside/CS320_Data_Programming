import flask
app = flask.Flask("my application")

@app.route("/")
def home():
    print("X")
    return '<html><body><img src="example.svg"></body></html>'
    
@app.route("/example.svg")
def handler1():
    print("Y")
    return "TODO"
@app.route("/out.svg")
def handler2():
    print("Z")
    return "TODO"
if __name__ == "main":
    app.run(host ="0.0.0.0", debug = True, threaded = False)