def concatenate(*args, **kwargs):
    final_word = ""
    for word in args:
        final_word += word
        
    for old_w, new_w in kwargs.items():
        if old_w in final_word:
            final_word = final_word.replace(old_w, new_w)
    
    return final_word

##########################################################

def concatenate(*args, **kwargs):
    final_word = ''.join(args)
    
    for old_w, new_w in kwargs.items():
        final_word = final_word.replace(old_w, new_w)
        
    return final_word
        
    
print(concatenate("Soft", "UNI", "Is", "Grate", "!", 
UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", 
C="P", s="", java='Java'))