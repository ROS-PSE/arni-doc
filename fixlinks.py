#!/usr/bin/env python
import os


for f in os.listdir("."):
	if f.endswith(".html"):
		data = ""
		with open (f, "r") as myfile:
			data=myfile.read()
		data = data.replace("_static/", "static/")
		with open (f, "w") as myfile:
			myfile.write(data)