#!/usr/bin/env python
import sys, os, getopt

def print_help():
	print("Usage: generaterst.py [options] directory")

def pascal_case(inp):
	output = ""
	x = inp.split("_")
	for y in x:
		output += y[0].upper() + y[1:]
	return output

def titlize(inp):
	output = ""
	x = inp.split("_")
	for y in x:
		output += y[0].upper() + y[1:] + " "
	return output.strip()

options, remainder = getopt.getopt(sys.argv[1:], 'o:t:hp', ['output', 'title', 'help'])
outpath = os.path.abspath(os.getcwd() + "/source") + "/"

if len(remainder) < 1:
	print_help()
	exit(1)
else:
	pfad = os.path.abspath(remainder[0])
package = os.path.basename(pfad)
title = titlize(package)
outfile = outpath + package + ".rst"

writeprivate = False

for opt, arg in options:
	if opt in ("-h", "--help"):
		print_help()
		exit(1)
	if opt in ("-p"):
		writeprivate = True
	if opt in ("-o", "--output"):
		outfile = outpath + arg
	if opt in ("-t", "--title"):
		title = arg

rstout = title + "\n" + "*" * len(title) + "\n\n"

for f in os.listdir(pfad):
	if f.endswith(".py") and f not in ("setup.py", "__init__.py"):
		t = pascal_case(f[0:-3])
		rstout += t + "\n" + "=" * len(t) + "\n"
		rstout += ".. automodule:: " + package + "." + f[0:-3] + "\n"
		rstout += "   :members:\n"
		if writeprivate:
			rstout += "   :private-members:\n"
		rstout += "\n"

print("written to " + outfile)
f = open(outfile, "w")
f.write(rstout)
f.close()