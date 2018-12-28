import math
import random

def product(list):
    p = 1
    for i in list:
        p *= i
    return p

def same(items):
	return len(set(items)) == 1 #faster all(x == items[0] for x in items)
def where_on_genome(position):
	if(not position):
		raise ValueError('A very specific bad thing happened.')
	#these are for Pl
	if(position <= 34000):
		return "RNA_l"
	if(position < 34542):
		return "DNA"
	if(position < 34559):
		return "DNA_Tl1"
	if(position < 35518):
		return "DNA"
	if(position < 35534):
		return "DNA_Nut"
	if(position <= 35591):
		return "DNA"
	#these are for Pre


	#these are for Pr
	if(position <= 38249):
		return "DNA"
	if(position < 38281):
		return "DNA_Nut"
	if(position < 38301):
		return "DNA_Tr1"
	if(position < 39000):
		return "DNA"
	if(position >= 39000):
		return "RNA_r"


# this is one step of the iteration
def iteration(reactions, molecules, substrate, product, dna):
	# do stuff
	tot = list(reactions.values())
	for i, k in enumerate(reactions):
		r = reactions[k]
		if(len(substrate[k]) > 1 and len(set(substrate)) == 1):
			#special case for reactions that use two of same thing
			s = substrate[k][0]
			tot[i] *= molecules[s] * (molecules[s]-1)
		else:
			for s in substrate[k]:
				tot[i] *= molecules[s]
	# nothing more can occur so avoid div zero
	if(sum(tot) == 0):
		return float("-inf")
	# cumulative sum of the probabilities
	cumsum = [sum(tot[:i+1])/sum(tot) for i in range(len(tot))] 
	rand = random.random()
	for i, k in enumerate(reactions):
		if(rand < cumsum[i]):
			break
	tau = math.log(1/random.random())/sum(tot)
	# adjust the molecules
	for s in substrate[k]:
		molecules[s] -= 1;
	for p in product[k]:
		molecules[p] += 1;
	# adjust the genetic
	if(substrate[k] == product[k]):
		s = substrate[k][0]
		#print(k, s, dna)
		j = get_random_pol(s, dna)
		#print(i)
		dna[j+1] = dna[j]
		temp = dna.pop(j)
		molecules[temp + "*" + where_on_genome(j)] -= 1;
		molecules[temp + "*" + where_on_genome(j+1)] += 1;
	elif any("DNA" in s for s in substrate[k]+product[k]):
		print(substrate[k])
		print(get_random_pol(substrate[k][0], dna) )

			
	return tau

def get_random_pol(r, dna):
	# get a random polymerase in the region r
	i = r.find('DNA')
	what = r[:i-1]
	where = r[i:]
	#print("what where", what, where, dna)
	keys = list(dna.keys())
	random.shuffle(keys)
	for k in keys:
		if(where_on_genome(k) == where and dna[k] == what):
			return k
	return


