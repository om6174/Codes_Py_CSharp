#assuming correct inputs for the sake of simplicity
#assuming the input is a word with no spaces, space not handled in program
def palindrome(word):
    word = word.lower()
    for i in range(int(len(word)/2)):
        if word[i] != word[-i-1]:            
            return "Word is not a palindrome"
    return "Word is a palindrome"
while True:
    input_word = input("Enter a word to check for palindrome, press Enter without typing a word to exit\n")
    if not input_word: break
    print(palindrome(input_word))

"""
Output:
Enter a word to check for palindrome, press Enter without typing a word to exit
asd
Word is not a palindrome
Enter a word to check for palindrome, press Enter without typing a word to exit
as
Word is not a palindrome
Enter a word to check for palindrome, press Enter without typing a word to exit
asa
Word is a palindrome
Enter a word to check for palindrome, press Enter without typing a word to exit
assa
Word is a palindrome
Enter a word to check for palindrome, press Enter without typing a word to exit

"""
