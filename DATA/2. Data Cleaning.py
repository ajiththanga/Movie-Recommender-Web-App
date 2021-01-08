import pandas as pd
import json
import string


### CLEAN OMDB DATA

df = pd.read_json(r'omdb_data.json')

df = df.fillna(0)

# remove movies with blank titles
df = df[df.Title != 0]

# remove movies with no votes
df = df[df.imdbVotes != "N/A"]

# create new column "Title + Year"
df = df.astype({"Year": str})
df["Title + Year"] = df["Title"] + " (" + df["Year"] + ")"

# clean 'Year' column
def clean_year(x):
    if isinstance(x, str):
        return(x.replace('–', ''))
    return(x)

df['Year'] = df['Year'].apply(clean_year).astype('float')
df['Year'] = df['Year'].astype(int)

# clean 'Runtime' column
for index, row in df.iterrows(): 
    num_hours = 0
    num_mins = 0
    runtime_clean = 0
    runtime = row['Runtime']
    
    if runtime == 'N/A':
        runtime_clean = 0
    elif 'h' in runtime:
        num_hours = runtime[0]
        runtime_clean = int(num_hours)*60
        if 'min' in runtime:
            num_mins = runtime[4:-4]
            runtime_clean = runtime_clean + int(num_mins)
    else:
        num_mins = runtime[:-4]
        num_mins = num_mins.replace(',','')
        runtime_clean = int(float(num_mins))
    
    df.at[index, 'Runtime'] = runtime_clean

# clean "BoxOffice" column
# (0 if N/A)
df["BoxOffice"].replace({"N/A": 0}, inplace=True)
df = df.astype({"BoxOffice": str})
df['BoxOffice'] = df['BoxOffice'].str.replace(',','')
df['BoxOffice'] = df['BoxOffice'].str.replace('$','')

boxoffice_list = []
# convert millions
for index, row in df.iterrows():
    if row["BoxOffice"][-1] == "M":
        value = row['BoxOffice'].replace('M','')
        value = float(value)*1000000
    elif row["BoxOffice"][-1] == "k":
        value = row['BoxOffice'].replace('k','')
        value = float(value)*1000
    else:
        value = row['BoxOffice']
        
    boxoffice_list.append(value)
    
df['BoxOffice'] = boxoffice_list

# clean 'imdbVotes' column
df['imdbVotes'] = df['imdbVotes'].str.replace(',','') 

# set datatypes
df = df.astype({"Title + Year": str})
df = df.astype({"Title": str})
df = df.astype({"Year": int})
df = df.astype({"Rated": str})
df = df.astype({"Released": str})
df = df.astype({"Runtime": str})
df = df.astype({"Title": str})
df = df.astype({"Genre": str})
df = df.astype({"Director": str})
df = df.astype({"Writer": str})
df = df.astype({"Actors": str})
df = df.astype({"Plot": str})
df = df.astype({"Language": str})
df = df.astype({"Country": str})
df = df.astype({"Poster": str})
df = df.astype({"imdbRating": float})
df = df.astype({"imdbVotes": int})
df = df.astype({"imdbID": str})
df = df.astype({"BoxOffice": float})
df = df.astype({"Production": str})

# deleting columns
del df['DVD']
del df['Website']
del df['Response']
del df['totalSeasons']
del df['Season']
del df['Episode']
del df['seriesID']
del df['Error']
del df['Awards']
del df['Ratings']
del df['Metascore']
del df['Type']

# save df as json to be uploaded to MongoDB
with open('omdb_data_clean.json', 'w', encoding='utf-8') as file:
    df.to_json(file, force_ascii=False)
