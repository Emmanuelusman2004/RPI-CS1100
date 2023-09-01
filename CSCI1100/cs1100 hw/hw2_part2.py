word = input("Enter a string to encode ==> ")
print(word)
print("")
def encrypt(word):
    word = word.replace(' a', '%4%') 
    word = word.replace('he', '7!')
    word = word.replace('e', '9(*9(') 
    word = word.replace('y', '*%$')
    word = word.replace('u', '@@@')
    word = word.replace('an', '-?')
    word = word.replace('th', '!@+3')
    word = word.replace('o', '7654') 
    word = word.replace('9', '2')
    word = word.replace('ck', '%4')
    return word
def decrypt(word):
    word = word.replace('%4', 'ck')
    word = word.replace('2', '9')
    word = word.replace('7654', 'o')
    word = word.replace('!@+3', 'th')
    word = word.replace('-?', 'an')
    word = word.replace('@@@', 'u')
    word = word.replace('*%$', 'y')
    word = word.replace('9(*9(', 'e')
    word = word.replace('7!', 'he')
    word2 = word.replace('%4%', ' a')
    
    #word = word.replace('ck', '%4')
    #word = word.replace('9', '2')
    #word = word.replace('o', '7654')
    #word = word.replace('th', '!@+3')
    #word = word.replace('an', '-?')
    #word = word.replace('u', '@@@')
    #word = word.replace('y', '*%$')
    #word = word.replace('e', '9(*9(')
    #word = word.replace('he', '7!')
    #word2 = word.replace(' a', '%4%')
    return word2

    #word = word.replace('%4%', ' a') 
    #word = word.replace('7!', 'he')
    #word = word.replace('9(*9(', 'e') 
    #word = word.replace('*%$', 'y')
    #word = word.replace('@@@', 'u')
    #word = word.replace('-?', 'an')
    #word = word.replace('!@+3', 'th')
    #word = word.replace('7654','o') 
    #word = word.replace('2', '9')
    #word2 = word.replace('%4', 'ck')

x = encrypt(word)
y = decrypt(encrypt(word))

print("Encrypted as ==> " + x)

difference_in_length = len(x) - len(word)
print("Difference in length ==> " + str(difference_in_length))

print("Deciphered as ==> " + y)

if word == y:
    print("Operation is reversible on the string.")
else:
    print("Operation is not reversible on the string.")
