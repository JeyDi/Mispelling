import nltk
import re

#Function to create and load frequencies by the text


raw=open("ex.txt","r").read()
tokens=nltk.word_tokenize(raw)
words=re.compile('.*[A-Za-z0-9].*')
filtered=[w for w in tokens if words.match(w)]
pairs=nltk.bigrams(filtered)
#Main function in the NLTK packages
fdist=nltk.FreqDist(pairs)
#fdist.keys()[:2]
type(fdist)

for w1,w2 in fdist.items():
   print (w1,w2)