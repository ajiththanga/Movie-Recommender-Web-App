import pandas as pd
import pickle
import requests
import json
import string


### GET LIST OF IMDB IDS

# download imdb tsv's from https://www.imdb.com/interfaces/
df_titles = pd.read_csv("title.basics.tsv\data.tsv",sep="\t")
df_ratings = pd.read_csv("title.ratings.tsv\data.tsv",sep="\t")

# filter for titles with type = movie, an existent runtime, an existent genre
df_titles = df_titles.loc[(df_titles['titleType'] == 'movie') & (df_titles['runtimeMinutes'] != '\\N') & (df_titles['genres'] != '\\N')]

# get list of imdb ids
id_list = df_titles['tconst'].unique().tolist()

# using id_list, filter for movies with at least 1 rating
df_ratings = df_ratings.loc[df_ratings['tconst'].isin(id_list)]

# get list of imdb ids
id_list_final = df_ratings['tconst'].unique().tolist()

# save final list of imdb ids
with open('id_list', 'wb') as fp:
    pickle.dump(id_list_final, fp)


### OMDB API CALL

apiKey = '938a9276'
url = 'http://private.omdbapi.com/?apikey='+apiKey

# read list of imdb ids
with open ('id_list', 'rb') as fp:
    id_list = pickle.load(fp)

# omdb api call for each id
omdb_data = []
i = 0

for imdb_id in id_list:
    i += 1
    print(str(i) + ": " + imdb_id)
    
    params = {
        'i': imdb_id,
        'plot': 'full'
    }
    
    try:
        response = requests.get(url, params=params).json()
        omdb_data.append(response)
        
    except:
        print("error")
        pass

# save omdb data
with open('omdb_data.json', 'w', encoding='utf-8') as outfile:
    json.dump(omdb_data, outfile, force_ascii=False)
