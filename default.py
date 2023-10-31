from english_words import get_english_words_set
web2lowerset = get_english_words_set(['web2'], lower=True,alpha=True)
print(type(web2lowerset))
wor = [i for i in web2lowerset if len(i)==5]
print(len(wor))