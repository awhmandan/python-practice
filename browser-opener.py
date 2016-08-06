#! /usr/bin/env python3
import webbrowser, sys

if len(sys.argv) > 1:
	url = ''.join(sys.argv[1:])

webbrowser.open(url)

#enter full site URLs as further args e.g. browser-opener.py https://www.reddit.com