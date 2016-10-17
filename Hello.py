from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/name")
def hello2():
	return "Whats my name yo"

@app.route("/name/<name>")
def hello3(name):
	return "My name is " + name

@app.route("/firstname", methods =['GET'])
def gettest():
	var = request.args.get("firstname")
	return var

if __name__ == "__main__":
    app.run()
