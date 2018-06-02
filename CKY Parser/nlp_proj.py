import re
import sys

backtrack = dict()
count_r = dict()
count = 1	

def get_single_rules(word, d, j, i = None):
	temp_list = list()
	s_list = list()
	t_list = list()

	if i is None:
		for k,v in d.items():
			for elem in v:
				if word in elem:
					s_list.append(k)
					t1 = (k, j, j)
					t2 = (word, j, j)
					t_list.append(t2)
					if t1 in backtrack:
						backtrack[t1].append(t_list)
					else:
						temp_list.append(t_list)
						backtrack[t1] = temp_list
						temp_list = list()
					t_list = list()
		for val in s_list:
			for k,v in d.items():
				for elem in v:
					if len(elem)==1 and elem[0]==val:
						s_list.append(k)
						t1 = (k, j, j)
						t2 = (elem[0], j, j)
						t_list.append(t2)
						if t1 in backtrack:
							backtrack[t1].append(t_list)
						else:
							temp_list.append(t_list)
							backtrack[t1] = temp_list
							temp_list = list()
						t_list = list()
	else:
		for k,v in d.items():
			for elem in v:
				if len(elem)==1 and elem[0]==word:
					s_list.append(k)
					t1 = (k, i, j)
					t2 = (elem[0], i, j)
					t_list.append(t2)
					if t1 in backtrack:
						backtrack[t1].append(t_list)
					else:
						temp_list.append(t_list)
						backtrack[t1] = temp_list
						temp_list = list()
					t_list = list()
	return s_list

def get_combo_rules(g1, g2, r, i, j, k):
	c_list = list()
	a_list = list()
	g_list = list()
	t_list = list()
	temp_list = list()
	for v1 in g1:
		for v2 in g2:
			c_list.append(v1)
			c_list.append(v2)
			a_list.append(c_list)
			c_list = list()		
	for key,v in r.items():
		for elem in a_list:
			if elem in v:
				g_list.append(key)
				t1 = (key, i, j)
				t2 = (elem[0], i, k-1)
				t3 = (elem[1], k, j)
				t_list.append(t2)
				t_list.append(t3)
				#temp_list.append(t_list)
				#backtrack[t1] = temp_list
				#t_list = list()
				#temp_list = list()
				if t1 in backtrack:
					backtrack[t1].append(t_list)
				else:
					temp_list.append(t_list)
					backtrack[t1] = temp_list
					temp_list = list()
				t_list = list()	
	return g_list

def backtracking(tup, mess, words, index):#index must start from 0
	if tup[0] in words:
		print(tup[0].upper(), end="", flush=True)
		return;
	if tup in mess.keys():
		print((tup[0]+"("), end="", flush=True)
		for val in mess[tup][index]:
			if val in backtrack.keys():
				count = len(backtrack[val])
				if count == 1:
					backtracking(val, mess, words, 0)
				elif count > 1:
					if val not in count_r:
						count_r[val] = 1
					else:
						count_r[val] += 1	
					#for i in range(0,count):
					backtracking(val, mess, words, count_r[val]-1) 	
			else:
				backtracking(val, mess, words, 0)			
			print(")", end="", flush=True)
	else:
		print("No parse tree available for this sentence")


filename = sys.argv[1]
sentence = sys.argv[2]

sentence = sentence.lower()
s_words = sentence.split()
s_len = len(s_words)

file = open(filename,"r",encoding="utf-8")
rules = file.read()
rules = rules.lower()

rules_dict = dict()
temp_list = list()
cnf_list = list()

lines = rules.split("\n")
for line in lines:
	lhs_key = line.split(":")[0].strip()
	rhs = line.split(":")[1].strip()
	rhs_list = rhs.split()
	#print("\nKEY: "+lhs_key)
	#print("\nrhs list complete  "+str(rhs_list))
	if len(rhs_list)==3:
		temp_list.append(rhs_list[:2])
		new_key = "X"+str(count)
		count +=1
		rules_dict[new_key] = temp_list
		temp_list = list()

		cnf_list.append(new_key)
		#print("\nrhs list_2 "+rhs_list[2])
		cnf_list.append(rhs_list[2])
		#print("\ncnf list: "+str(cnf_list))
		
		temp_list.append(cnf_list)
		if lhs_key in rules_dict:
			rules_dict[lhs_key].append(cnf_list)
		else:
			rules_dict[lhs_key] = temp_list

		temp_list = list()
		cnf_list = list()
	else:
		if lhs_key in rules_dict:
			rules_dict[lhs_key].append(rhs_list)
		else:
			temp_list.append(rhs_list)
			rules_dict[lhs_key] = temp_list
			temp_list = list()
#print("rules dictionary: "+str(rules_dict))
grid = [[[] for i in range(s_len)] for j in range(s_len)]

gs_list = list()
gc_list = list()

for j in range(0,s_len):
	gs_list = get_single_rules(s_words[j],rules_dict, j)
	grid[j][j].extend(gs_list)
	gs_list = list()
	for i in reversed(range(0,j)):
		for k in range(i+1,j+1):
			gc_list = get_combo_rules(grid[i][k-1],grid[k][j], rules_dict, i, j, k)
			grid[i][j].extend(gc_list)
		for g in grid[i][j]:
			gs_list = get_single_rules(g,rules_dict, j ,i)
			grid[i][j].extend(gs_list)	

print("\n")	
print("Grammar rules:")	
print("\n")
for k,v in rules_dict.items():
	print(str(k)+" : "+str(v))	
print("\n\n")	
print("Parse table:")	
print("\n")
for i in range(0,s_len):
	print(grid[i])
count = len(backtrack[("s",0,s_len-1)])
print("\n\n")
#for k,v in backtrack.items():
	#print(str(k)+" : "+str(v))
print("Parse trees:")
for i in range(0,count):
	print("\n")
	backtracking(("s",0,s_len-1),backtrack, s_words, i)
print("\n\n")
