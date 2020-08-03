from flair.embeddings import FlairEmbeddings, DocumentPoolEmbeddings, WordEmbeddings
from flair.data import Sentence
import torch
import pandas as pd
import csv


df = pd.read_json(
    r'/Users/kameronquackenbush/Desktop/briq-app/test/src/data/quotes.json')

# test data to expedite the embedding
# df = pd.read_json(
#    r'/Users/kameronquackenbush/Desktop/briq-app/test/src/data/testdata.json')

print(df['en'])
df['en'] = pd.Series(df['en'])

new_list = []
for i in df['en']:
    new_list.append(i)
# Check to see if all data has been transferred to list
print(len(new_list))


# first, declare how you want to embed
embeddings = DocumentPoolEmbeddings(
    [WordEmbeddings('glove'), FlairEmbeddings('news-forward'), FlairEmbeddings('news-backward')])

# your query
# This query once implemented into a function, becomes the random quote from a 4 or 5 star
# rating
query = Sentence(
    "Everything should be made as simple as possible. But to do that you have to master complexity.")

# Embed the query
embeddings.embed(query)

# Must first tokenize each sentence to be prepared for embedding
paragraph = []
for i in range(len(new_list)):
    x = Sentence(new_list[i])
    paragraph.append(x)
print(paragraph)

# Embed each sentence
for i in range(len(paragraph)):
    embeddings.embed([paragraph[i]])

print(paragraph)

similarity_to_sent = []

# use cosine distance
cos = torch.nn.CosineSimilarity(dim=0, eps=1e-6)

# Use cosine similarity to find most similar sentences against the query
for i in range(len(paragraph)):
    similarity_to_sent.append(cos(query.embedding, paragraph[i].embedding))
    m = max(similarity_to_sent)
    if similarity_to_sent[i] == m:
        if similarity_to_sent[i] != 1:
            print("This is the most similar sentence:",
                  paragraph[i], similarity_to_sent[i])
        else:
            continue
    else:
        continue

# Same as above except the least similar
for i in range(len(paragraph)):
    similarity_to_sent.append(cos(query.embedding, paragraph[i].embedding))
    m = min(similarity_to_sent)
    if similarity_to_sent[i] == m:
        if similarity_to_sent[i] != 1:
            print("This is the least similar sentence:",
                  paragraph[i], similarity_to_sent[i])
        else:
            continue
    else:
        continue
