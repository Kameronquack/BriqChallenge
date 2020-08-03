# QuoteCodingChallenge

## In order to run the Vue.js app, cd into the BriqChallenge folder and run 'npm run serv' in the terminal. 

For this challenge I created a Vue.js UI that takes a randomly generated coding quote from : https://programming-quotes-api.herokuapp.com/ and displays it. The UI displays the quote as well as the author. Below the quote I implemented a rating system where the user can rate the quote on a scale from 1-5. Once the quote is rated another randomly generated quote from the API is generated and displayed.  

I also used a method that can find the most similar quote to a given quote using cosine vector similarity. This can be found in the quote_model folder. In order to run this, go to a new terminal tab, cd into the 'quote_model' folder, and on the command line run 'python quotemodel.py'. 

This script will create a pandas dataframe object with the json data from https://programming-quotes-api.herokuapp.com/, and use flair embeddings to give sentence embeddings to each sentence in the dataframe. From here you can choose a quote and use it as a query, and run it against the rest of the embeddings using cosine similarity funtion to obtain the most similar quote as well as the least similar to the query quote. 

I was however unable to succesfully implement this script into my Vue UI to use for a 4 or 5 star rating. I do not have too much experience with Vue.js as well as Javascript/CSS/HTML, so I was trying to learn these aspects on the fly. Another problem I ran into was trying to save the cosine similarty method in the quotemodel.py script as a function, but I could not figure out a solution as to how to save the document embeddings and use them for future use. 
