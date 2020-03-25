import shell
from termcolor import cprint, colored
import replit
replit.clear()
langInputText = colored('Enter language to run in, or type 3 to exit. Options are:\n 1. MCpure\n 2. Exit\n', 'blue')
langInputTextSHonly = colored('Enter language to run, or type 3 to exit. Options are:\n 1. Run Python Shell\n 2. Exit\n', 'blue')
MCfileInputText = colored('Enter filename/path or leave blank to run the Megacode shell: ', 'green')
def runPyfromMC(MCfile):
	shell.pyExecute(MCfile)
def runMC(pureMC):
	MCfile = input(MCfileInputText)
	if pureMC != True:
		shell.run("python " + MCfile)
	else:
		while True:
			if MCfile == '':
				lang = input(langInputTextSHonly)
			else:
				lang = input(langInputText)
			if lang == "MCpure" or lang == "MCpure" or lang == "1":
				runPureMC(MCfile)
				break
			elif lang == "Exit" or lang == "exit" or lang == "2":
				break
			else:
				cprint("Please enter a valid option.", "yellow")
def runPureMC(MCfile):
	runPyfromMC(MCfile)