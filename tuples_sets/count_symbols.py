""" text = input()

occurrences = {}

for letter in text:
    occurrences[letter] = occurrences.get(letter, 0) + 1
    
for letter, occ in sorted(occurrences.items()):
    print(f"{letter}: {occ} time/s") """
    
#######################################################

text = input()
this_set = set(text)

for letter in sorted(this_set):
    occ = text.count(letter)
    print(f"{letter}: {occ} time/s")