import re
import sys

#Following function calculates the bigram counts of the sentences
def calcCounts(s_words, data):
	bigram_counts = dict()
	for x in range(0, len(s_words)):
		for y in range(0, len(s_words)):
			find_string = s_words[x]+" "+s_words[y]
			bigram_counts[find_string] = len(re.findall('\\b'+s_words[x]+'\s'+s_words[y]+'\\b', data))
	return bigram_counts;

#Following function calculates the bigram probabilities of the sentences
def calcProbs(s_words, bigram_counts, counts):
	bigram_probs = dict()
	for x in range(0, len(s_words)):
		for y in range(0, len(s_words)):
			find_string = s_words[x]+" "+s_words[y]
			bigram_probs[find_string] = bigram_counts[s_words[x]+" "+s_words[y]]/counts[s_words[x]]
	return bigram_probs;	

#Following function displays the bigram counts table for the sentences
def dispCounts(s_words, bigram_counts):
	for x in range(0, len(s_words)):
		print(s_words[x], end='\t\t')
		for y in range(0, len(s_words)):
			print("{}".format(bigram_counts[s_words[x]+" "+s_words[y]]),end='\t')
		print("\n")

#Following function displays the bigram probabilities table for the sentences
def dispProbs(s_words, bigram_probs):
	for x in range(0, len(s_words)):
		print(s_words[x], end='\t\t')
		for y in range(0, len(s_words)):
			print("{0:0.4f}".format(bigram_probs[s_words[x]+" "+s_words[y]]),end='\t')
		print("\n")

#Following function calculates the total probability for the sentences
def calcTotalProb(s_words, bigram_probs):
	total_prob = 1
	for x in range(0, len(s_words)-1):
		#print("{0:0.4f}".format(bigram_probs[s_words[x]+" "+s_words[x+1]]))
		total_prob *= bigram_probs[s_words[x]+" "+s_words[x+1]]
		#print("{}".format(total_prob))
	return total_prob;

filename = sys.argv[1]
s1 = sys.argv[2]
s2 = sys.argv[3]

s1_stripped = re.sub(r'[^\w\s-]','',s1)
s1_stripped = re.sub(r'-',' ',s1_stripped)
s2_stripped = re.sub(r'[^\w\s-]','',s2)
s2_stripped = re.sub(r'-',' ',s2_stripped)
s1_words = s1_stripped.split()
s2_words = s2_stripped.split()

file = open(filename,"r",encoding="utf-8")
corpus = file.read()
data = re.sub(r'[^\w\s-]','',corpus)
data = re.sub(r'-',' ',data)
words = data.split()
words = sorted(words)
counts = dict()
bigram_counts_s1 = dict()
bigram_counts_s2 = dict()
bigram_probs_s1 = dict()
bigram_probs_s2 = dict()

for word in words:
	if word in counts:
		counts[word] +=1
	else:
		counts[word] = 1

bigram_counts_s1 = calcCounts(s1_words, data)
bigram_counts_s2 = calcCounts(s2_words, data)
bigram_probs_s1 = calcProbs(s1_words, bigram_counts_s1, counts)
bigram_probs_s2 = calcProbs(s2_words, bigram_counts_s2, counts)

print('\n\n\n')
print("BIGRAM MODEL WITHOUT SMOOTHING")
print('\n\n')
print("BIGRAM COUNTS FOR SENTENCE 1")
dispCounts(s1_words, bigram_counts_s1)
print('\n\n')
print("BIGRAM COUNTS FOR SENTENCE 2")
dispCounts(s2_words, bigram_counts_s2)
print('\n\n')
print("BIGRAM PROBABILITIES FOR SENTENCE 1")
dispProbs(s1_words, bigram_probs_s1)
print('\n\n')
print("BIGRAM PROBABILITIES FOR SENTENCE 2")
dispProbs(s2_words, bigram_probs_s2)
print('\n\n')
print("TOTAL PROBABILITY FOR SENTENCE 1")
print(calcTotalProb(s1_words, bigram_probs_s1))
print('\n\n')
print("TOTAL PROBABILITY FOR SENTENCE 2")
print(calcTotalProb(s2_words, bigram_probs_s2))

print('\n\n\n')
print("BIGRAM MODEL WITH ADD-ONE SMOOTHING")
print('\n\n')
for key in bigram_counts_s1.keys():
	bigram_counts_s1[key] +=1
for key in bigram_counts_s2.keys():
	bigram_counts_s2[key] +=1
for key in counts.keys():
	counts[key] += len(counts)
bigram_probs_s1 = calcProbs(s1_words, bigram_counts_s1, counts)
bigram_probs_s2 = calcProbs(s2_words, bigram_counts_s2, counts)	
print("BIGRAM COUNTS FOR SENTENCE 1")
dispCounts(s1_words, bigram_counts_s1)
print('\n\n')
print("BIGRAM COUNTS FOR SENTENCE 2")
dispCounts(s2_words, bigram_counts_s2)
print('\n\n')
print("BIGRAM PROBABILITIES FOR SENTENCE 1")
dispProbs(s1_words, bigram_probs_s1)
print('\n\n')
print("BIGRAM PROBABILITIES FOR SENTENCE 2")
dispProbs(s2_words, bigram_probs_s2)
print('\n\n')
print("TOTAL PROBABILITY FOR SENTENCE 1")
print(calcTotalProb(s1_words, bigram_probs_s1))
print('\n\n')
print("TOTAL PROBABILITY FOR SENTENCE 2")
print(calcTotalProb(s2_words, bigram_probs_s2))
print('\n\n')