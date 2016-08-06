#! /usr/bin/env python3
import webbrowser, sys

if len(sys.argv) > 1:
	url = ''.join(sys.argv[1:])

webbrowser.open(url)

#enter full site URL, e.g. https://www.reddit.com