### To run the program, please use the following command:
```bash
    python bigram_prob.py "<corpus file name>" "<first sentence>" "<second sentence>"
```
For example: 
```bash
python bigram_prob.py "Corpus.txt" "Apple computer is the first product of the company." 
"Apple introduced the new version of iPhone in 2008."
```

The quotation marks ("") are needed.

#### Program needs to be run with Python version 3.x.
---
The given program uses the Bigram Language Model, which is trained on the corpus provided by the user, 
to find out which of the two sentences is most probable.

The probabilities of the two sentences have been calculated under two scenarios:

1. Bigram model without smoothing
2. Bigram model with add-one smoothing
   
First the bigram counts for the given sentences are calculated for the bigram model without smoothing.

These counts are then converted to bigram probabilities, which are used to calculate the joint probability 
of the given word sequences (the sentences).

The probability matrix obtained from the bigram model without smoothing, is a sparse matrix which makes it 
highly probable for the given sentences to have 0 probability.

This is why smoothing is performed.

In add-one smoothing the bigram counts are increased by 1, and the probabilities are calculated after 
adjusting for these increased counts.
