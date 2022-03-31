# load in all the modules we're going to need
import nltk, re, string, collections
from nltk.util import ngrams  # function for making ngrams

# this corpus is big, so let's look at just one of the files in it

with open("spanishText_90000_95000", "r", encoding='latin-1') as file:
    text = file.read()

# let's do some preprocessing. We don't care about the XML notation, new lines
# or punctuation marks other than periods. (We'll consider the end of the sentence
# a "word") We also don't want to consider capitalization.

# get rid of all the XML markup
text = re.sub('<.*>', '', text)

# get rid of the "ENDOFARTICLE." text
text = re.sub('ENDOFARTICLE.', '', text)

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

# get the frequency of each unigram in our corpus
esUnigramFreq = collections.Counter(esUnigrams)
# get the frequency of each bigram in our corpus
esBigramFreq = collections.Counter(esBigrams)
# get the frequency of each trigram in our corpus
esTrigramFreq = collections.Counter(esTrigrams)

# The twenty most popular ngrams in this Spanish corpus?
UniTop = esUnigramFreq.most_common(20)
BiTop = esBigramFreq.most_common(20)
TriTop = esTrigramFreq.most_common(20)

print("Top 20 de las palabras mas usadas en el corpus español\n")

for i in range(1):
    print("** UNI-GRAMS **")
    for x in UniTop:
        print("Uni-grams", x[i], "/ N° Frecuencia ->", x[i+1])
    print("** BI-GRAMS **")
    for y in BiTop:
        print("Bi-grams", y[i], "/ N° Frecuencia ->", y[i+1])
    print("** TRI-GRAMS **")
    for z in TriTop:
        print("Tri-grams", z[i], "/ N° Frecuencia ->", z[i+1])

with open("C:/Users/danie/Documents/U/6to Semestre/Inteligencia Artificial/2do Corte/internet_archive_scifi_v3.txt",
          "r", encoding='utf-8') as file:
    text2 = file.read()

# let's do some preprocessing. We don't care about the XML notation, new lines
# or punctuation marks other than periods. (We'll consider the end of the sentence
# a "word") We also don't want to consider capitalization.

# get rid of all the XML markup
text2 = re.sub('<.*>', '', text2)

# get rid of the "ENDOFARTICLE." text
text2 = re.sub('ENDOFARTICLE.', '', text2)

# get rid of punctuation (except periods!)
punctuationNoPeriod = "[" + re.sub("", "", string.punctuation) + "]"
text2 = re.sub(punctuationNoPeriod, "", text2)

# first get individual words
tokenized2 = text2.split()

# and get a list of all the Uni-grams
esUnigrams2 = ngrams(tokenized2, 1)
# and get a list of all the bi-grams
esBigrams2 = ngrams(tokenized2, 2)
# and get a list of all the Tri-grams
esTrigrams2 = ngrams(tokenized2, 3)

# get the frequency of each unigram in our corpus
esUnigramFreq2 = collections.Counter(esUnigrams2)
# get the frequency of each bigram in our corpus
esBigramFreq2 = collections.Counter(esBigrams2)
# get the frequency of each trigram in our corpus
esTrigramFreq2 = collections.Counter(esTrigrams2)

# The twenty most popular ngrams in this Spanish corpus?
UniTop2 = esUnigramFreq2.most_common(20)
BiTop2 = esBigramFreq2.most_common(20)
TriTop2 = esTrigramFreq2.most_common(20)

print("\n\nTop 20 de las palabras mas usadas en el corpus texto de historias de ciencia ficción\n")

for i in range(1):
    print("** UNI-GRAMS **")
    for x in UniTop2:
        print("Uni-grams", x[i], "/ N° Frecuencia ->", x[i+1])
    print("** BI-GRAMS **")
    for y in BiTop2:
        print("Bi-grams", y[i], "/ N° Frecuencia ->", y[i+1])
    print("** TRI-GRAMS **")
    for z in TriTop2:
        print("Tri-grams", z[i], "/ N° Frecuencia ->", z[i+1])
