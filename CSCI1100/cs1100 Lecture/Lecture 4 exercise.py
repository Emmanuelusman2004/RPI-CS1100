phrase = 'Things you wish you knew as a freshman'
phrase.title()
hashtag = phrase.title()
hashtag = hashtag.replace(" ", "")
hashtag = '"' + "#" + hashtag + '"'
phrase = '"' + phrase + '"'
print("The phrase " + phrase + "\n" + "becomes the hashtag " + hashtag)
