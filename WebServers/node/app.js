/* By Marti157 (on GitHub) */

// Create express app (node framework, using it to better handle requests)
const express = require('express')
const app = express()

// Handle GET requests. Log to console and return default text
app.get("/", function (req, res) {
	console.log('127.0.0.1:5000 - "GET / HTTP/1.1" 200')
	res.send("Try sending a POST request!")
})

// Handle the POST request. Log to console and return a random number (from 1 to 10)
app.post("/", function (req, res) {
	console.log('127.0.0.1:5000 - "POST / HTTP/1.1" 200')
	num = Math.floor(Math.random() * 10 + 1)
	res.send(num.toString())
})

// Start app on port 5000 and log a welcome message to the console
app.listen(5000, () => console.log(" * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)"))