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
#parser.add_argument("-c", "--cookies", action="store", help="Provide cookie (PEM chain) file for authentication (Required for HTTPS)")
args = parser.parse_args()

notCheckedIfOK = True

def getResponse(url):
    global notCheckedIfOK
    if args.txtout != None and args.txtin != None and notCheckedIfOK:
        if args.txtin == args.txtout:
            notCheckedIfOK = False
            print("Input and output text files can not be the same! Ignoring...")

    headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:145.0) Gecko/20100101 Firefox/145.0", 
    "accept-language": "en-US,en;q=0.5",
    #"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    #"accept-encoding": "gzip, deflate, zstd", 
    #"sec-gpc": "1", 
    #"connection": "keep-alive", 
    #"upgrade-insecure-requests": "1", 
    #"sec-fetch-dest": "document", 
    #"sec-fetch-mode": "navigate", 
    #"sec-fetch-site": "none", 
    #"sec-fetch-user": "?1", 
    #"priority": "u=0, i", 
    #"te": "trailers"
    }

    with requests.Session() as s:
        #s.verify = args.cookies
        response = requests.get(url=url, headers=headers)
        start = response.text.find('https://featureassets.gocomics.com/assets/')
        link = response.text[start:].partition('"')[0]
        print(f'Image URL for {url} is {link}')

        # I don't really know a better way to do this
        fn = link[link.find('.com/') + 5:]
        
    if args.txtout != None:
        if args.txtin != args.txtout:
            with open(args.txtout, 'a') as file:
                file.write(f'{url}: {link}\n')
    
    if args.save:
        if args.directory == None:
            args.directory = '.'
        path = pathlib.Path(f'{args.directory}/assets')
        path.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(link, f'{args.directory}/{fn}.gif')

#if args.cookies == None:
#    print("A cookie file is required to access HTTPS URLs. Attempting anyway...")
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
