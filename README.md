# GCImageGrabber
A simple program written in Python to give you the image URL of a comic on GoComics.

# Usage
Running is simple, but first you need the following libraries. They're all installable through pip.
```
argparse
requests
```

After all of that, all you need to do is run the app and supply the URL to the comic. \
`./GCImageGrabber.py --url https://gocomics.com/comic/date`

Or, if you have multiple, you can use more than one too. \
`./GCImageGrabber.py --urls https://gocomics.com/comic/date https://gocomics.com/another-comic/date`

Or, if you even want, use a .txt file! \
`./GCImageGrabber.py --txtin path/to/list.txt`

Want to save the URLs in a .txt file? You can do that. \
`./GCImageGrabber.py --txtout path/to/output-list.txt`

Want to save the pictures? You can do that too. \
`./GCImageGrabber.py --url https://gocomics.com/comic/date --save`

.. As well as to a certain directory. \
`./GCImageGrabber.py --url https://gocomics.com/comic/date --save --directory path/to/save/to`

# Legal
If it's needed, if GoComics wants this taken down for whatever reason, I'm not gonna fight it. This app is free, open source, and non-profitable, however, and licensed under GPLv3.
