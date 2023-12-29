from flask import Flask, request, render_template

HR = Flask(__name__)

@HR.route("/")
def main():
	return render_template("index.html") + "HR wants access to Marketing department "

if __name__ == "__main__":
     HR.run(host="0.0.0.0", port=5000)
