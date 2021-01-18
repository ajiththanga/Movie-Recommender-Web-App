### Pre-Processing
Plot Feature
* Remove punctuation, lowercase
* Create corpus of words
* Using Google pretrained Word2Vec model, train corpus
* Build TD-IDF W2V model and save embeddings
Other Text Features
* Lowercase, combine names
* Create and save a count matrix for each feature
Numerical Features
* Create and save numpy array

### Recommendation Algorithm
* Load dataframe and vectors from preprocessing script
* Find weighted cosine similarity for all features for each chosen movie
* Find average cosine similarity for each chosen movie
* Add a little randomness to results
* Apply numerical filters
* Return recommendations
