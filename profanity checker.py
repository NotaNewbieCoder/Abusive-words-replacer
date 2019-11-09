from profanityfilter import ProfanityFilter

#function to censor text
pf= ProfanityFilter()

def censor(text):
    '''censor all offensive words with *'''
    pf.set_censor("*")
    censored = pf.censor(text)
    return censored

text= input("Enter text here:" )

text= censor(text)

text

