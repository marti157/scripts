# Web Servers
Two web servers written in Python and Javascript using Flask and Node (express.js) respectively.

## Their Operation
Both servers are to be run locally on any device with Python.

If you send a POST request to them (only POST, not GET), they return a random number from 1 to 10.

## Setup
I am assuming that you have access to the command line and Python installed on your device. If not, do some research and get that set up.

If you don't have Node.js also installed, go [here](https://nodejs.org/en/download/) to download and install it.

Next, clone this repository if you haven't already and "cd" into "WebServers/node/". Then, install the express module by executing:
```
$ npm install express --save
```
This will create a bunch of files in the "node/" directory, but you can ignore them.

## Running
To run the Python Flask web server, "cd" into "flask/" from "WebServers/" and run:
```
$ python app.py
```
And if you want to run the Javascript Node web server, "cd" into "node/" from "WebServers/" and execute:
```
$ node app.js
```
Just a reminder, you can only run one of the servers at once as they both use the same port!

## Sending Requests
When you have one of the web servers running, you can visit them in any browser at "localhost:5000". You will get the message:
```
Try sending a POST request!
```
As the servers only return a number if you send a request using the POST method.


To get a random number from 1 to 10, you can use the command "curl" (as shown below) or apps like Postman (wich works very well).
"Curl" comes installed on Linux and Mac, to send a POST request use a new command line window and run:
```
$ curl -X POST localhost:5000
```
The output will be a random number, as expected.
