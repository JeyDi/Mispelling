
#Zip verify
a = [1,2,3]
b = [2,3,4]
c = [5,6,7,8]

zipped = list(zip(a,b,c))
print(zipped)



from nltk import ngrams, FreqDist
sentence = 'this is a foo bar sentences and i want to ngramize it'
chars = [FreqDist(list(s)) for s in sentence.split()]
print(chars)

n = 1
combinations = ngrams(sentence.split(), n)
for grams in combinations:
  print(grams)

data = ["this", "is", "not", "a", "test", "this", "is", "real", "not", "a", "test", "this", "is", "this", "is", "real", "not", "a", "test"]

from nltk import ngrams, FreqDist
all_counts = dict()
for size in 2, 3, 4, 5:
    all_counts[size] = FreqDist(ngrams(data, size))
print("Finish")

from nltk import ngrams, FreqDist
l = ["i","i","c","i"]
result = FreqDist(l)
print(result)


###---------------------------------------------------------###
###SINGLE LETTER NGRAM CALC
import pandas as pd

stringa = """Use securing confined his shutters. Delightful as he it acceptance an solicitude discretion reasonably. Carriage we husbands advanced an perceive greatest. Totally dearest expense on demesne ye he. Curiosity excellent commanded in me. Unpleasing impression themselves to at assistance acceptance my or. On consider laughter civility offended oh. 
Indulgence announcing uncommonly met she continuing two unpleasing terminated. Now busy say down the shed eyes roof paid her. Of shameless collected suspicion existence in. Share walls stuff think but the arise guest. Course suffer to do he sussex it window advice. Yet matter enable misery end extent common men should. Her indulgence but assistance favourable cultivated everything collecting. 
Bringing unlocked me an striking ye perceive. Mr by wound hours oh happy. Me in resolution pianoforte continuing we. Most my no spot felt by no. He he in forfeited furniture sweetness he arranging. Me tedious so to behaved written account ferrars moments. Too objection for elsewhere her preferred allowance her. Marianne shutters mr steepest to me. Up mr ignorant produced distance although is sociable blessing. Ham whom call all lain like. 
Kindness to he horrible reserved ye. Effect twenty indeed beyond for not had county. The use him without greatly can private. Increasing it unpleasant no of contrasted no continuing. Nothing colonel my no removed in weather. It dissimilar in up devonshire inhabiting. 
Throwing consider dwelling bachelor joy her proposal laughter. Raptures returned disposed one entirely her men ham. By to admire vanity county an mutual as roused. Of an thrown am warmly merely result depart supply. Required honoured trifling eat pleasure man relation. Assurance yet bed was improving furniture man. Distrusts delighted she listening mrs extensive admitting far. 
Kept in sent gave feel will oh it we. Has pleasure procured men laughing shutters nay. Old insipidity motionless continuing law shy partiality. Depending acuteness dependent eat use dejection. Unpleasing astonished discovered not nor shy. Morning hearted now met yet beloved evening. Has and upon his last here must. 
Affronting discretion as do is announcing. Now months esteem oppose nearer enable too six. She numerous unlocked you perceive speedily. Affixed offence spirits or ye of offices between. Real on shot it were four an as. Absolute bachelor rendered six nay you juvenile. Vanity entire an chatty to. 
The him father parish looked has sooner. Attachment frequently gay terminated son. You greater nay use prudent placing. Passage to so distant behaved natural between do talking. Friends off her windows painful. Still gay event you being think nay for. In three if aware he point it. Effects warrant me by no on feeling settled resolve. 
Way nor furnished sir procuring therefore but. Warmth far manner myself active are cannot called. Set her half end girl rich met. Me allowance departure an curiosity ye. In no talking address excited it conduct. Husbands debating replying overcame blessing he it me to domestic. 
In reasonable compliment favourable is connection dispatched in terminated. Do esteem object we called father excuse remove. So dear real on like more it. Laughing for two families addition expenses surprise the. If sincerity he to curiosity arranging. Learn taken terms be as. Scarcely mrs produced too removing new old. 
"""

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
finalList = []

for char in alfabeto: 
  stringa = stringa.lower()
  curstring = stringa
  lettere = []
  while len(curstring) > 0:
    arr = curstring.split(char, 1)
    if len(arr) == 1:
      break
    lettere.append(arr[1][0])
    curstring = arr[1]

  while ' ' in lettere:
    lettere.remove(' ')

  freq = {}
  for l in lettere:
    if l in freq.keys():
      continue  
    freq[l] = lettere.count(l) / len(lettere)

  finalList.append(freq)

myDict = pd.DataFrame(finalList)
print(myDict)

