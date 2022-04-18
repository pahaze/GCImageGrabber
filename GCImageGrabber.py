#!/usr/bin/env python3
import argparse
import json
import requests
import html_to_json

parser = argparse.ArgumentParser(description='Garfield Comic Image Grabber')
parser.add_argument("--url", help="URL to use")
args = parser.parse_args()

url = args.url
response = requests.get(url=url)
json_string = html_to_json.convert(response.text)

json_obj = json.dumps(json_string)

startThing = json_obj.find('https://assets.amuniversal.com')
endThing = 0
for x in range(100):
	if endThing == 0:
		endThing = startThing
	if json_obj[endThing] != '"':
		endThing += 1

print(json_obj[startThing:endThing])
