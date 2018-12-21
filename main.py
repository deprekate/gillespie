import sys
from variables import * 
import math
from functions import iteration

def show(mols):
	for m in mols:
		sys.stdout.write(str(mols[m]))
		sys.stdout.write("\t")
	sys.stdout.write("\n")

dna = {
	38200 : 'RNAP'
}
operators = {
	"Or1" : [],
	"Or2" : [],
	"Or3" : [],
	"Ol1" : [],
	"Ol2" : [],
	"Ol3" : [],
	"Oe1" : [],
	"Oe2" : []
}
t = 0
tfinal = 1000
while(t < tfinal):
	tau = iteration(reactions1, molecules, reactions_sub, reactions_pro, dna)
	t += tau
	#show(molecules)
	if(tau < 1e-10):
		break

for m in molecules:
	sys.stdout.write("_")
	sys.stdout.write("\t")
sys.stdout.write("\n")
for c in range(0, 14):
	for m in molecules:
		try:
			if m[c] is "_":
				sys.stdout.write("|")
			else:
				sys.stdout.write(m[c])
		except:
			sys.stdout.write(" ")

		sys.stdout.write("\t")
	sys.stdout.write("\n")
