import sys
import pandas as pd

#sys.argv will contain["python", "ngram_datable.py", "output_corpus1.csv"]
if len(sys.argv) >1:
    infile =  sys.argv[1]

    #generate a dataframe from the csv
    df = pd.read_csv("output_corpus1.csv", encoding='ISO-8859-1')

    #create a dataframe of only the Usernames and Ngrams to capture each student by deleting the columns for Utterances 
    del df['Utterance_1']
    del df['Utterance_2']

    #Create the pivot table for each student and the count of ngrams within their session 
    ngram_df = (df.set_index('User').stack()
        .rename_axis(['Username', 'NGram']).rename('columns').reset_index())
    ngram_table = ngram_df.pivot_table('NGram', 'Username', 'columns', aggfunc='count', fill_value=0)        

    #create an output file for the datatable
    ngram_table.to_csv('output_ngramTable.csv', header = True)
