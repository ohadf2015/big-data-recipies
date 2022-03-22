import re
import nltk
from nltk import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# converting each ingredients list in one string: ' word1, word2, ...'
df['ingredients_clean_string'] = [' , '.join(
    z).strip() for z in df["recipeIngredient"]]
#df['ingredients_clean_string'] = df['ingredients_clean_string'].str.replace('[^\w\s]','')
# df['ingredients_clean_string']

# further clean data and extract information through word lemmatization
df['ingredients_string'] = [' '.join([WordNetLemmatizer().lemmatize(re.sub('[^A-Za-z]', ' ', line))
                                      for line in lists]).strip() for lists in df['recipeIngredient']]
# df['ingredients_string']


# # # create corpus based on newly processed data
train_corpus = df['ingredients_string']
# print(train_corpus.head())

# # convert a collection of raw documents to a matrix of TF-IDF features,max_df = .57
train_vectorizer = TfidfVectorizer(stop_words='english',
                                   #ngram_range = ( 1 ,1 ),
                                   analyzer="word",
                                   binary=False,
                                   token_pattern=r'\w+',
                                   sublinear_tf=False)

# # # transform the corpus to a dense matrix representation
train_tfidf = train_vectorizer.fit_transform(
    train_corpus[:5000], y=None).todense()
print(train_tfidf[400])

# # prepare data for prediction
# train_predictor = train_tfidf

# train_target = df['category']
