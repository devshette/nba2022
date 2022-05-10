# -*- coding: utf-8 -*-
"""NBA75 SNA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NnESrPmuqHFaXi6Dc5LCegcykJaXrgmB
"""

#Import all libraries needed
#dataframes
import pandas as pd 
#data plotting
import matplotlib.pyplot as plt 
import seaborn as sb #visual settings for plt
#word processing
import re
import nltk 
# warnings to be ignored
import warnings
warnings.filterwarnings('ignore')

#Import dataset
#Exported .csv from NodeXL
df = pd.read_csv("/content/testNBA75.csv", sep=",", encoding='Latin-1')
#Verify the columns imported
df.head()
#Print some basic stats
print ('columns are:\n',df.columns)
print ('data types are:\n',df.dtypes)
print('Number of rows in data: ', df.size/4)
print('Number of vertex1 ids: ', df['Vertex 1'].size)
print('Number of vertex2 ids: ', df['Vertex 2'].size)
print('Number of tweets in data: ', df['Tweet'].size)
print('Number of unique tweets in data: ', df['Tweet'].size)
print('unique vertex1 ids: ', df['Vertex 1'].nunique())
print('unique vertex2 ids: ', df['Vertex 2'].nunique())

#Identify top 5 users
print('Top 5 users with most tweets made:\n ', df['Vertex 1'].value_counts().nlargest(5))
print('\n')
print('Top 5 users as vertex 2 (most common receivers of mentions):\n ', df['Vertex 2'].value_counts().nlargest(5))

#Plot most common vertex1 IDs
plt.figure()
df['Vertex 1'].value_counts().nlargest(10).plot(kind='bar')
plt.xticks(rotation=45)
plt.show()

#Plot most common vertex2 IDs
plt.figure()
df['Vertex 2'].value_counts().nlargest(10).plot(kind='bar')
plt.xticks(rotation=45)
plt.show()

pip install neattext #text cleaning package

#library from text cleaning package
import neattext.functions as nfx
# dir(nfx)

#Tweets column
print(len(df['Tweet']))
#Delete any null values
df = df[ ~ df['Tweet'].isnull()] #This is the only thing needed



# Onspect first 50 tweets
df['Tweet'][1:50]

#Create two new columns to extract and store hashtags and emojis
df['extracted_hashtags']= df['Tweet'].apply(nfx.extract_hashtags)
df['extracted_emojis']= df['Tweet'].apply(nfx.extract_emojis)

#Inspection step
df['extracted_hashtags']

#Inspection step
df['extracted_emojis']

#Process the extracted-haashtags column and collect the hashtags in a list
hashtags_list=[]
for word in  df['extracted_hashtags']:
  hashtags_list.extend(word)

print(hashtags_list)

#For each hashtag detected, count the instances of occurrence
dict = {}

for word in hashtags_list:
  if word not in dict:
    dict[word] = 1
  else:
    dict[word] += 1

sorted(dict.items(), key=lambda item: item[1])
print(dict)

teams_list = ['Phoenix', 'Dallas', 'Memphis', 'Golden State', 'Miami', 'Philadelphia', 'Boston', 'Milwaukee']

# team_counter = {}

# for team_name in teams_list:
#   for tweet in df['Tweet']:
#     if team_name in tweet:
#       team_counter[team_name] += 1
#     else:
#       continue

# print(team_counter)

pd.Series(nltk.ngrams(df['Tweet'], 1)).value_counts()

print(df['Tweet'][1])

for word in df['Tweet'][1].split():
    print (word)

teams_list = ['Phoenix', 'Dallas', 'Memphis', 'Golden State', 'Miami', 'Philadelphia', 'Boston', 'Milwaukee']

team_counter = []
for team_name in teams_list:
  for tweet in df['Tweet']:
    if team_name in tweet.split():
     team_counter.append(team_name)
    else:
      continue

#print(team_counter)

dict = {}

for word in team_counter:
  if word not in dict:
    dict[word] = 1
  else:
    dict[word] += 1

print(dict)

for tweet in df['Tweet']:
    if 'win' in tweet.split():
     print(tweet)
    else:
      continue

#hyperlink containing tweet
df['Tweet'][100]

#hyperlink removal
df['clean_tweets']= df['Tweet'].apply(nfx.remove_urls)
df['clean_tweets'][100]

#hashtag extraction
df['extracted_hashtags'][100]

#Several subsequent steps perform data cleaning operations
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_userhandles)
df['clean_tweets'][100]

df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_stopwords)
df['clean_tweets'][100]

df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_hashtags)
df['clean_tweets'][100]

# remove all the things that do not add to the sentiment of the text
df['clean_tweets']= df['Tweet'].apply(nfx.remove_bad_quotes)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_btc_address)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_currencies)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_currency_symbols)
#df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_custom_pattern)
#df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_custom_words)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_dates)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_emails)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_emojis)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_hashtags)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_html_tags)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_mastercard_addr)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_md5sha)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_multiple_spaces)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_non_ascii)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_numbers)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_phone_numbers)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_postoffice_box)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_puncts)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_punctuations)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_shortwords)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_special_characters)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_stopwords)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_street_address)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_terms_in_bracket)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_urls)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_userhandles)
df['clean_tweets']= df['clean_tweets'].apply(nfx.remove_visacard_addr)

def remove_my_stopwords(text):
  my_stop_words = ['like','comment','share','follow','retweet','https']
  words = [word for word in text.split() if word.lower() not in my_stop_words]
  new_text = " ".join(words)
  return new_text

df['clean_tweets']= df['clean_tweets'].apply(remove_my_stopwords)

# df['clean_tweets']

# df['clean_tweets'].iloc[4000]

"""Sentiment Analysis"""

from textblob import TextBlob

def get_sentiment(text):
  blob = TextBlob(text)
  sentiment_polarity = blob.sentiment.polarity
  sentiment_subjectivity = blob.sentiment.subjectivity
  if sentiment_polarity < 0:
    sentiment_label = 'Negative'
  elif sentiment_polarity > 0:
    sentiment_label = 'Positive'
  else:
    sentiment_label = 'Neutral'

  result = {'polarity': sentiment_polarity,
            'subjectivity': sentiment_subjectivity,
             'sentiment': sentiment_label}

  return result

get_sentiment(df['clean_tweets'].iloc[1600])

df['sentiment_results'] = df['clean_tweets'].apply(get_sentiment)

# df['sentiment_results']

# pd.json_normalize(df['sentiment_results'].iloc[500])

df = df.join(pd.json_normalize(df['sentiment_results']))

# df.head()

df['sentiment'].value_counts()

plt.figure()
df['sentiment'].value_counts().plot(kind='bar')
plt.xticks(rotation=45)
plt.show()

sb.countplot(df['sentiment'])

positive_tweets = df[df['sentiment'] == 'Positive']['clean_tweets']
negative_tweets = df[df['sentiment'] == 'Negative']['clean_tweets']
neutral_tweets = df[df['sentiment'] == 'Neutral']['clean_tweets']

teams_list = ['Phoenix', 'Dallas', 'Memphis', 'Golden State', 'Miami', 'Philadelphia', 'Boston', 'Milwaukee']

team_counter = []
for team_name in teams_list:
  for tweet in positive_tweets:
    if team_name in tweet.split():
     team_counter.append(team_name)
    else:
      continue

#print(team_counter)

dict = {}

for word in team_counter:
  if word not in dict:
    dict[word] = 1
  else:
    dict[word] += 1

print(dict)

teams_list = ['Phoenix', 'Dallas', 'Memphis', 'Golden State', 'Miami', 'Philadelphia', 'Boston', 'Milwaukee']

team_counter = []
for team_name in teams_list:
  for tweet in negative_tweets:
    if team_name in tweet.split():
     team_counter.append(team_name)
    else:
      continue

#print(team_counter)

dict = {}

for word in team_counter:
  if word not in dict:
    dict[word] = 1
  else:
    dict[word] += 1

print(dict)

teams_list = ['Phoenix', 'Dallas', 'Memphis', 'Golden State', 'Miami', 'Philadelphia', 'Boston', 'Milwaukee']

team_counter = []
for team_name in teams_list:
  for tweet in neutral_tweets:
    if team_name in tweet.split():
     team_counter.append(team_name)
    else:
      continue

#print(team_counter)

dict = {}

for word in team_counter:
  if word not in dict:
    dict[word] = 1
  else:
    dict[word] += 1

print(dict)

# positive_tweets[1:100]

# negative_tweets[1:100]

# neutral_tweets[1:100]

#remove stopwords and conver to tokens
#positive_tweets_list = positive_tweets.apply(nfx.remove_stopwords).tolist()
#negative_tweets_list = negative_tweets.apply(nfx.remove_stopwords).tolist()
#neutral_tweets_list = neutral_tweets.apply(nfx.remove_stopwords).tolist()
positive_tweets_list = positive_tweets
negative_tweets_list = negative_tweets
neutral_tweets_list = neutral_tweets

pos_tokens=[]
neg_tokens=[]
neu_tokens=[]

for line in  positive_tweets_list:
  for token in line.split():
    pos_tokens.append(token)

for line in  negative_tweets_list:
  for token in line.split():
    neg_tokens.append(token)

for line in  neutral_tweets_list:
  for token in line.split():
    neu_tokens.append(token)

#most common keywords
from collections import Counter

def get_tokens(docx,num=30):
  word_tokens = Counter(docx)
  most_common = word_tokens.most_common(num)
  result = dict(most_common)
  return result

words_to_count = (word for word in neg_tokens if word[:1].isupper())
c = Counter(words_to_count)
print(c.most_common(10))
pos_df = pd.DataFrame(c.most_common(10),columns=['words','scores'])
print(pos_df)

words_to_count = (word for word in pos_tokens if word[:1].isupper())
c = Counter(words_to_count)
print(c.most_common(10))
neg_df = pd.DataFrame(c.most_common(10),columns=['words','scores'])
print(neg_df)

words_to_count = (word for word in neu_tokens if word[:1].isupper())
c = Counter(words_to_count)
print(c.most_common(10))
neu_df = pd.DataFrame(c.most_common(10),columns=['words','scores'])
print(neu_df)

#most_common_neg_words = get_tokens(neg_tokens,len(neg_tokens))

#most_common_neu_words = get_tokens(neu_tokens,len(neu_tokens))

#plot with seaborn
# pos_df = pd.DataFrame(most_common_pos_words.items(),columns=['words','scores'])
# neg_df = pd.DataFrame(most_common_neg_words.items(),columns=['words','scores'])
# neu_df = pd.DataFrame(most_common_neu_words.items(),columns=['words','scores'])

neg_df['words']

plt.figure(figsize=(20,10))
sb.barplot(x='words', y='scores', data=neg_df[1:20], color='blue')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(20,10))
sb.barplot(x='words', y='scores', data=pos_df[1:20], color='blue')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(20,10))
sb.barplot(x='words', y='scores', data=neu_df[1:20], color='blue')
plt.xticks(rotation=45)
plt.show()

pd.Series(nltk.ngrams(neu_df['words'], 2)).value_counts()[:10]

pd.Series(nltk.ngrams(neg_df['words'], 2)).value_counts()[:10]

pd.Series(nltk.ngrams(pos_df['words'], 2)).value_counts()[:10]

pd.Series(nltk.ngrams(neu_df['words'], 3)).value_counts()[:10]

pd.Series(nltk.ngrams(neg_df['words'], 3)).value_counts()[:10]

pd.Series(nltk.ngrams(pos_df['words'], 3)).value_counts()[:10]

pd.Series(nltk.ngrams(neu_df['words'], 4)).value_counts()[:10]

pd.Series(nltk.ngrams(neg_df['words'], 4)).value_counts()[:10]

pd.Series(nltk.ngrams(pos_df['words'], 4)).value_counts()[:10]

pd.Series(nltk.ngrams(neu_df['words'], 5)).value_counts()[:10]

pd.Series(nltk.ngrams(neg_df['words'], 5)).value_counts()[:10]

pd.Series(nltk.ngrams(pos_df['words'], 5)).value_counts()[:10]

from wordcloud import WordCloud

def plot_wordcloud(docx):
  mywordcloud = WordCloud().generate(docx)
  plt.figure(figsize=(20,10))
  plt.imshow(mywordcloud,interpolation='bilinear')
  plt.axis('off')
  plt.show()

pos_docx= ' '.join(pos_tokens)
plot_wordcloud(pos_docx)

neg_docx= ' '.join(neg_tokens)
plot_wordcloud(neg_docx)

neu_docx= ' '.join(neu_tokens)
plot_wordcloud(neu_docx)