from collections import deque

WORDS = {
    "rose": "rose", 
    "tulip": "tulip", 
    "lotus": "lotus", 
    "daffodil": "daffodil",
}

vowels = deque(input().split())
consonants = deque(input().split())

while vowels and consonants:
    curr_vowel = vowels.popleft()
    curr_consonant = consonants.pop()
    
    for word in WORDS:
        WORDS[word] = WORDS[word].replace(curr_vowel, "")
        WORDS[word] = WORDS[word].replace(curr_consonant, "")
        
        if not WORDS[word]:
            print(f"Word found: {word}")
            break
    else:
        continue
    
    break
else:
    print("Cannot find any word!")     
    
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")       
    
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")