#!/usr/bin/env python3
import argparse
import pathlib
import requests
import urllib.request

parser = argparse.ArgumentParser(description='GoComics Comic Image Grabber')
parser.add_argument("-u", "--url", help="Use a single URL")
parser.add_argument("-us", "--urls", nargs="+", help="Use multiple URLs")
parser.add_argument("-ti", "--txtin", help="Use a text file with URLs")
parser.add_argument("-to", "--txtout", help="Put the image URLs in a text file")
parser.add_argument("-s", "--save", default=False, action="store_true", help="Save the images")
parser.add_argument("-d", "--directory", help="Directory to store images if saving them")
args = parser.parse_args()

notCheckedIfOK = True

def getResponse(url):
    global notCheckedIfOK
    if args.txtout != None and args.txtin != None and notCheckedIfOK:
        if args.txtin == args.txtout:
            notCheckedIfOK = False
            print("Input and output text files can not be the same! Ignoring...")

    response = requests.get(url=url).text

    start = response.find('https://assets.amuniversal.com')
    link = response[start:].partition('"')[0]
    print(f'Image URL for {url} is {link}')

    # I don't really know a better way to do this
    fn = link[link.find('m/') + 2:]
    
    if args.txtout != None:
        if args.txtin != args.txtout:
            with open(args.txtout, 'a') as file:
                file.write(f'{url}: {link}\n')
    
    if args.save:
        if args.directory != None:
            path = pathlib.Path(args.directory)
            path.mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(link, f'{args.directory}/{fn}.gif')
        else:
            urllib.request.urlretrieve(link, f'{fn}.gif')


if args.url != None:
    getResponse(args.url)
elif args.urls != None:
    for url in args.urls:
        getResponse(url)
elif args.txtin != None:
    with open(args.txtin) as file:
        lines = file.readlines()
        for line in lines:
            url = line.rstrip('\n')
            getResponse(url)
        
        file.close()
else:
    print(parser.print_help())