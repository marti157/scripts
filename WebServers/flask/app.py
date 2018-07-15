""" By Marti157 (on GitHub) """

# Import the necessary libraries for flask and for creating random numbers
from flask import Flask, request
import random

# Create the flask app
app = Flask(__name__)

# Define the app route at home ("/") and allow GET and POST request methods
@app.route('/', methods=["GET", "POST"])
def index():
	# Set the text to the default message but change it to a random number if the method is POST
	text = "Try sending a POST request!"
	if request.method == "POST":
		text = str(random.randint(1, 10))
	return text

# Run the app only after including the libraries
if __name__ == '__main__':
    app.run()
