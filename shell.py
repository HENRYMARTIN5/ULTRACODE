import os
def loadBash(tag):
	while True: os.system(input(tag))
def run(command):
	os.system(command)
def pyExecute(pyCommand):
	os.system("python " + pyCommand)