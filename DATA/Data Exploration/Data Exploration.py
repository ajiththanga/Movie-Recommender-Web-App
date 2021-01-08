import pandas as pd
import json
import string
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_json(r'omdb_data_clean.json')


### Year
df.hist(column='Year Count', bins=20)


### Genre
genre_list = []
for index, row in df.iterrows():
    genre = row['Genre']
    genre_split = genre.split(",")
    for genre in genre_split:
        genre = genre.strip()
        genre_list.append(genre)
        
c = Counter(genre_list)
del c["N/A"]
data = c.most_common(20)

## plot graph
names, values = zip(*data)
ind = np.arange(len(data))  # the x locations for the groups
width = 0.5 # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, values, width)

# add some text for labels, title and axes ticks
ax.set_ylabel('Count')
ax.set_xticks(ind+width/2.)
ax.set_xticklabels(names, rotation=45)
plt.xticks(size='small')
plt.title('Genre Count (Top 20)')

plt.show()


### Director
director_list = []
for index, row in df.iterrows():
    director = row['Director']
    director_split = director.split(",")
    for director in director_split:
        director = director.strip()
        director_list.append(director)
        
c = Counter(director_list)
del c["N/A"]
data = c.most_common(10)

## plot graph
names, values = zip(*data)
ind = np.arange(len(data))  # the x locations for the groups
width = 0.5 # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, values, width)

# add some text for labels, title and axes ticks
ax.set_ylabel('Count')
ax.set_xticks(ind+width/2.)
ax.set_xticklabels(names, rotation=45)
plt.xticks(size='small')
plt.title('Director Count (Top 10)')

plt.show()


### Actors
actors_list = []
for index, row in df.iterrows():
    actors = row['Actors']
    actors_split = actors.split(",")
    for actors in actors_split:
        actors = actors.strip()
        actors_list.append(actors)
        
c = Counter(actors_list)
del c["N/A"]
data = c.most_common(10)

## plot graph
names, values = zip(*data)
ind = np.arange(len(data))  # the x locations for the groups
width = 0.5 # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, values, width)

# add some text for labels, title and axes ticks
ax.set_ylabel('Count')
ax.set_xticks(ind+width/2.)
ax.set_xticklabels(names, rotation=45)
plt.xticks(size='small')
plt.title('Actors Count (Top 10)')

plt.show()


### Country
country_list = []
for index, row in df.iterrows():
    country = row['Country']
    country_split = country.split(",")
    for country in country_split:
        country = country.strip()
        country_list.append(country)
        
c = Counter(country_list)
del c["N/A"]
data = c.most_common(10)

## plot graph
names, values = zip(*data)
ind = np.arange(len(data))  # the x locations for the groups
width = 0.5 # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, values, width)

# add some text for labels, title and axes ticks
ax.set_ylabel('Count')
ax.set_xticks(ind+width/2.)
ax.set_xticklabels(names, rotation=45)
plt.xticks(size='small')
plt.title('Country Count (Top 10)')

plt.show()


### Language
language_list = []
for index, row in df.iterrows():
    language = row['Language']
    language_split = language.split(",")
    for language in language_split:
        language = language.strip()
        language_list.append(language)
        
c = Counter(language_list)
del c["N/A"]
data = c.most_common(10)

## plot graph
names, values = zip(*data)
ind = np.arange(len(data))  # the x locations for the groups
width = 0.5 # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, values, width)

# add some text for labels, title and axes ticks
ax.set_ylabel('Count')
ax.set_xticks(ind+width/2.)
ax.set_xticklabels(names, rotation=45)
plt.xticks(size='small')
plt.title('Language Count (Top 10)')

plt.show()


### imdbVotes
df.hist(column='imdbVotes', bins=50)


### imdbRating
df.hist(column='imdbRating', bins=20)
