import glob
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
nltk.download('stopwords')

tokenizer = RegexpTokenizer(r'\w+')
tally = {}

for filepath in glob.glob("./politics/*.txt"):
    with open(filepath, 'r') as file:
        doc = file.read()
    stop_words = set(stopwords.words('english'))
    s_temp = tokenizer.tokenize(doc)
    s = []
    for w in s_temp:
        l = w.lower()
        if l not in stop_words:
            s.append(w)

    index = 0
    tempdic = {}
    for x in s:
        if x in tally:
            tally[x] += 1
        else:
            tally.update({x: 1})

    tallySorted = sorted(tally.items(), key=lambda item: item[1])

for i in tallySorted:
    print(i)

