import argparse # arguments parser
import sys
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--nodes", help="Route to the node file (example ./nodes)") 
parser.add_argument("-p", "--pearson", help="Route to the pearson correation file (example ./hb_hb)")
parser.add_argument("-v","--value",help="absolute pearson. value bigger than this for each pair of nodes will be returned (example 0.5)", type=float)

args = parser.parse_args()

if(len(sys.argv) <4):
	print "Run python corr_graph.py --help for more information about input parameters"
	exit()

file = open(args.nodes,"r")
dict_index_node={}

for line in file:
		if ("ID" not in line):
			aux = line[:-1].split("\t")
			dict_index_node[str(aux[0])] = aux[1]


hb = open(args.pearson,"r")

#matrix = np.zeros((len(dict_index_node),len(dict_index_node)))
pearson = args.value
i = 0
#print dict_index_node
print "node1\tnode2\tr"
for line in hb:
	aux = line[:-2].split("\t")
	j = i+1
	while j<len(aux):
		value = abs(float(aux[j]))
		if (value >= pearson) and (i!=j):
			print dict_index_node[str(i+1)]+"\t"+dict_index_node[str(j+1)]+"\t"+aux[j] #index + 1 due the node IDs begin from 1 and not from 0
		j += 1
	i += 1


