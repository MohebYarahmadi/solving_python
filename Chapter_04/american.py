# DMOJ problem ccc02j2, AmeriCanadian
word = ''

while True:
    word = input().strip()
    
    if word == 'quit!' or len(word) < 4:
        break

    if word[-2:].lower() == 'or':
        if word[-3].lower() not in 'aiueo' and word[-3].lower() != 'y':
            word = word[:-2] + 'our'
            print(word)
            continue
    print(word)

    



# ------------
# def is_consonant(char):
#     # Check if a character is a consonant (not a vowel and not 'y')
#     vowels = "aeiouAEIOU"
#     return char not in vowels and char != 'y' and char != 'Y'
# 
# def translate_to_canadian(word):
#     # Check if the word is longer than 4 letters
#     if len(word) > 4:
#         # Check if the word ends with a consonant followed by 'or'
#         if word[-2:].lower() == 'or' and is_consonant(word[-3]):
#             # Replace 'or' with 'our'
#             return word[:-2] + 'our'
#     # Return the original word if no translation is needed
#     return word
# 
# 
# while True:
#     # Get user input
#     word = input()
#     # Check if the user wants to quit
#     if word.lower() == "quit!":
#         break
#     # Translate the word if necessary
#     translated_word = translate_to_canadian(word)
#     # Output the result
#     print(translated_word)
