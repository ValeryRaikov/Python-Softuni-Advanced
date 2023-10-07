# 1)Recursive way:

def palindrome(word, idx):
    if idx == len(word) // 2:
        return f"{word} is a palindrome"
    
    if word[idx] != word[-idx - 1]:
        return f"{word} is not a palindrome"
    
    return palindrome(word, idx+1)

print(palindrome("abcba", 0))
print(palindrome("peter", 0))
print(palindrome("abbabcgffcgbabba", 0))

##################################################
# 2)Reversed way:

word = list(input())
reversed_word = list(reversed(word))

if word == reversed_word:
    print(f"{''.join(word)} is a palindrome")
else:
    print(f"{''.join(word)} is not a palindrome")

#####################################################
    
word = list(input())

if word == word[::-1]:
    print(f"{''.join(word)} is a palindrome")
else:
    print(f"{''.join(word)} is not a palindrome")
    
####################################################

# 3)Iterative_way:

word = list(input())
counter = 0
for i in range(len(word)):
    if len(word) // 2 == counter:
        print(f"{''.join(word)} is a palindrome")
        break
    
    if word[i] != word[-i-1]:
        print(f"{''.join(word)} is not a palindrome")
        
    counter += 1