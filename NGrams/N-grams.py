# load in all the modules we're going to need
import nltk, re, string, collections
from nltk.util import ngrams # function for making ngrams

# this corpus is pretty big, so let's look at just one of the files in it

with open("C:/Users/danie/Documents/U/6to Semestre/Inteligencia Artificial/2do Corte/NGrams/spanishText_90000_95000", "r", encoding='latin-1') as file:
    text = file.read()

# let's do some preprocessing. We don't care about the XML notation, new lines
# or punctuation marks other than periods. (We'll consider the end of the sentence
# a "word") We also don't want to consider capitalization.

# get rid of all the XML markup
text = re.sub('<.*>','',text)

# get rid of the "ENDOFARTICLE." text
text = re.sub('ENDOFARTICLE.','',text)

# get rid of punctuation (except periods!)
punctuationNoPeriod = "[" + re.sub("", "", string.punctuation) + "]"
text = re.sub(punctuationNoPeriod, "", text)

# first get individual words
tokenized = text.split()

# and get a list of all the Uni-grams
esUnigrams = ngrams(tokenized, 1)
# and get a list of all the bi-grams
esBigrams = ngrams(tokenized, 2)
# and get a list of all the Tri-grams
esTrigrams = ngrams(tokenized, 3)

# get the frequency of each bigram in our corpus
esUnigramFreq = collections.Counter(esUnigrams)
# get the frequency of each bigram in our corpus
esBigramFreq = collections.Counter(esBigrams)
# get the frequency of each bigram in our corpus
esTrigramFreq = collections.Counter(esTrigrams)

#The twenty most popular ngrams in this Spanish corpus?
UniTop=esUnigramFreq.most_common(20)
BiTop=esBigramFreq.most_common(20)
TriTop=esTrigramFreq.most_common(20)

for i in range(1):
    print("** UNI-GRAMS **")
    for x in UniTop:
        print("Uni-grams",x[i],"/ N° Frecuencia ->",x[i+1])
    print("** BI-GRAMS **")
    for y in BiTop:
        print("Bi-grams",y[i],"/ N° Frecuencia ->",y[i+1])
    print("** TRI-GRAMS **")
    for z in TriTop:
        print("Tri-grams",z[i],"/ N° Frecuencia ->",z[i+1])