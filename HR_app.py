from flask import Flask, request

HR = Flask(__name__)

@HR.route("/")
def main():
	return"HR department has access to the marketing department " + "\n"

if __name__ == "__main__":
     HR.run(host="0.0.0.0", port=5000)
