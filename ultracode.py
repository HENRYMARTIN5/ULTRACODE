import shell
from termcolor import cprint, colored
import replit
replit.clear()
langInputText = colored('Enter language to run in, or type 3 to exit. Options are:\n 1. ULTRACODEshV2\n 2. UCpure\n 3. Exit\n', 'blue')
langInputTextSHonly = colored('Enter language to run, or type 3 to exit. Options are:\n 1. ULTRACODEshV2\n 2. Run Python Shell\n 3. Exit\n', 'blue')
UCfileInputText = colored('Enter filename/path or leave blank to run the ULTRACODE shell: ', 'green')
def runPyfromUC(UCfile):
	shell.run("cd projects")
	shell.pyExecute(UCfile)
def runUC(pureUC):
	UCfile = input(UCfileInputText)
	if pureUC != True:
		shell.run("python " + UCfile)
	else:
		while True:
			if UCfile == '':
				lang = input(langInputTextSHonly)
			else:
				lang = input(langInputText)
			if lang == "ultracodeshv1" or lang == "ULTRACODEshV1" or lang == "1":
				runPyfromUC("ultracodeSHv2.uc")
				break
			elif lang == "UCpure" or lang == "ucpure" or lang == "2":
				runPureUC(UCfile)
				break
			elif lang == "Exit" or lang == "exit" or lang == "3":
				break
			else:
				cprint("Please enter a valid option.", "yellow")
def runPureUC(UCfile):
	runPyfromUC(UCfile)