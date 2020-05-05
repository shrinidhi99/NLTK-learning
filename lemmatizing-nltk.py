from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("goodness"))
print(lemmatizer.lemmatize("highness"))
print(lemmatizer.lemmatize("higher"))
print(lemmatizer.lemmatize("high"))
print(lemmatizer.lemmatize('run', 'v'))
