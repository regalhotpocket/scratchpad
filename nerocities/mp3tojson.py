import json
import base64

input = open("03_-_Furries.mp3", "rb")
text = list(input.read())
output = open("output.js", "w")
output.write("let furries = " + json.dumps(text))