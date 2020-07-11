import nltk
from nltk.corpus import stopwords
import pymorphy2
import re
import plotly as pt
import plotly.offline as offline
import plotly.graph_objs as go

morph = pymorphy2.MorphAnalyzer()
english_stopwords = stopwords.words("english")

rez = []


def normalize_words(line):
    line = str(line).split(",")
    for word in line:
        word2 = str(word).split(" ")
        for atr in word2:
            reg = re.compile('[^a-zA-Zа-яА-Я. ]')
            corpus = reg.sub('', atr)
            rez.append(corpus.lower())
    print(len(rez))


for line in open('weather-check.txt', 'r').readlines():
    normalize_words(line)

english_stopwords.append('')

with open('newfile.txt', 'w') as f:
    for word in rez:
        if word not in english_stopwords:
            f.write(word + " ")

keys = []
values = []
temp = dict()

for word in rez:
    if word not in english_stopwords:
        if word in temp:
            temp[word] += 1
        else:
            temp[word] = 1

for key in temp:
    if str(key) not in english_stopwords:
        keys.append(key)
        values.append(temp[key])

trace = go.Scatter(
    x=keys,
    y=values,
    mode='lines',
    name='CHASTOTY'
)

dataset = [trace]
layout = go.Layout(barmode="group", title='words statistic',
                   xaxis=dict(title="words", ticklen=5, zeroline=False),
                   yaxis=dict(title="values", ticklen=5, zeroline=False))

fig = go.Figure(data=[trace], layout=layout)
offline.plot(fig, validate=False)

