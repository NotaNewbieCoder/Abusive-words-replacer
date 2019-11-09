from flask import Flask, request, jsonify, render_template
import re
import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

def GetCleanText(text):
  text = text.lower().split()

  stop_words = set(stopwords.words('english'))
  text = [w for w in text if not w in stop_words and len(w) >= 3]

  text = ' '.join(text)
  text = re.sub(r'https?://[A-Za-z0-9./]+' ,'url', text)
  text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]" ," ", text)
  text = re.sub(r"what's" ,"what is", text)
  text = re.sub(r"\'s" ," ", text)
  text = re.sub(r"\'ve" ," have", text)
  text = re.sub(r"\'t" ," not", text)
  text = re.sub(r"i'm" ,"i am", text)
  text = re.sub(r"\'re" ," are", text)
  text = re.sub(r"\'d" ," would", text)
  text = re.sub(r"\'ll" ," will", text)
  text = re.sub(r"," ," ", text)
  text = re.sub(r"\." ," ", text)
  text = re.sub(r"!" ," ", text)
  text = re.sub(r"\/" ," ", text)
  text = re.sub(r"\^" ," ^ ", text)
  text = re.sub(r"\+" ," + ", text)
  text = re.sub(r"\-" ," - ", text)
  text = re.sub(r"\=" ," = ", text)
  text = re.sub(r"'" ," ", text)
  text = re.sub(r"(\d+)(k)" ,r"\g<1>000", text)
  text = re.sub(r":" ," : ", text)
  text = re.sub(r" e g " ," eg ", text)
  text = re.sub(r" b g " ," bg ", text)
  text = re.sub(r" u s " ," us ", text)
  text = re.sub(r"\0s" ,"0", text)
  text = re.sub(r" 9 11 " ," 911 ", text)
  text = re.sub(r"e - maill" ," email ", text)
  text = re.sub(r" j k " ," jk ", text)
  text = re.sub(r"\s{2,}" ," ", text)
  text = re.sub(r"@[A-Za-z0-9]+" ," ", text)
  text = re.sub(r'(\w)\1{2,}' ,r'\1\1', text)
  text = re.sub(r"\w(\w)\1{2}" ," ", text)

  return text

from profanityfilter import ProfanityFilter
pf = ProfanityFilter()

def censor(text):
    pf.set_censor("*")
    censored = pf.censor(text)
    return censored

text= input("Enter text here:" )

text= GetCleanText(text)

text= censor(text)

text

