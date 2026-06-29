results = ["Mario", "Luigi"]

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

#removing item from list
results.remove("Bowser")

#inserting item in specifc position
results.insert(0,"Bowser")

#reversing list
results.reverse()

#adding multiple items at once
results.extend(["Bowser", "Donkey Kong Jr."])

#clears all items in list
results.clear()

print(results)


#comprehension in lists and dict
#lowercase_words= [word.lower() for words in len(word>4)]
#counts={word: lowercase_words.count(word) for word in lowercase_words}