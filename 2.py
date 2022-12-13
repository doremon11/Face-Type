import fuzzy
soundex = fuzzy.Soundex(10)
word = 'Murthy'
list=["Moorthy","Moorthi","Murthi","Mur","HELOO"]
for i in list:
    if soundex(i.upper())==soundex(word.upper()):
        print(i)
