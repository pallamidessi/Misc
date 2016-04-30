import re

dict = []
tlds = ["fr",
       "be",
       "com",
       "me",
       "es"]

result = set()

with open("fr_dict.txt") as file:
    for line in file:
        dict.append(line)
for tld in tlds:
    regexSuffix = re.compile(".*" + tld + "$")
    regexSimpleWord = re.compile('[a-zA-Z,$]+$')

    print "test"
    for word in dict:
        if regexSuffix.match(word) is not None:
            if regexSimpleWord.match(word) is not None:
                result.add(word)

print len(result)
for word in result:
    pass
    #print word
