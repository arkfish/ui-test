#import globals as _G
import regex as re

a = 158
b = 159

def getvar(var: str):
    return vars()[var]

with open("test.ui", "r") as file:
	for line in file:
		if line.startswith("!"):
			split = line.split("!")
			varcode = split[2].replace("\n", "")
		else:
			if varcode in line:
				all = re.findall("\$\(\w*\)", line)
				for i,v in enumerate(all):
					print(re.findall("\w", v)[0])