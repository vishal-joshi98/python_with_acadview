# QUESTION 4:
tweet="'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'"
import re
def clean_tweets(tweet):
    #remove URLs
    tweet=re.sub('http\S+\s*',' ',tweet)
    #remove RT and cc
    tweet = re.sub('RT|cc', ' ', tweet)
    #remove hashtags
    tweet = re.sub('#\S+', ' ', tweet)
    #remove mentions
    tweet = re.sub('@\S+', ' ', tweet)
    #remove punctuations
    tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_'{|}~"""), ' ', tweet)
    #remove extra whitespace
    tweet=re.sub('\s+',' ',tweet)
    return tweet

print(clean_tweets(tweet))
