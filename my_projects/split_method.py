def split_method(message, separator, words = []):
    if not isinstance(message, str):
        raise ValueError("Entered message is not string!")
    
    if message == "":
        return None
    
    curr_word = ""
    for i in range(len(message)):
        if message[i] != separator:
            curr_word += message[i]
        elif message[i] == separator:
            words.append(curr_word)
            curr_word = ""
            
    words.append(curr_word)
        
    return words

print(split_method(input("Enter string here: "), input("Enter separator here: ")))