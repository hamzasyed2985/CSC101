def is_palindrome(word):
 
    word = word.replace(" ", "").lower()
    reversed_word = word[::-1]

    if word == reversed_word:
        return True
    else:
        return False
input_word = input("Enter a word or phrase: ")
if is_palindrome(input_word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
