#!/usr/bin/env python3
import argparse
import json
import requests

parser = argparse.ArgumentParser(description='GoComics Comic Image Grabber')
parser.add_argument("--url", help="URL to use")
args = parser.parse_args()

if args.url != None:
    url = args.url
    response = requests.get(url=url).text

    start = response.find('https://assets.amuniversal.com')
    print(response[start:].partition('"')[0])
else:
    print(parser.print_help())