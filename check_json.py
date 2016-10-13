#!/usr/bin/env python
import json
import sys

filename = sys.argv[1]
with open(filename) as f:
	data = f.read()
	json.loads(data)
	print "%s is a correct json file" % filename
