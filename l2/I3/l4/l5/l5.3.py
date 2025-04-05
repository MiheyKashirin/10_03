import string
text = 'Should, I. subscribe? Yes!'
words = text.split()
cleaned_words = [''.join(c for c in word if c not in string.punctuation) for word in words]
hashtag = ''.join(word.capitalize() for word in cleaned_words)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
hashtag = '#' + hashtag
print(hashtag)