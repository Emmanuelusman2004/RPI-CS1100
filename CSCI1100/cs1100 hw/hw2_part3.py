sentence = input("Enter a sentence => ")
print(sentence)

def number_happy(sentence):
    sentence = sentence.lower()
    x = sentence.count("happiness")
    y = sentence.count("laugh")
    z = sentence.count("love")
    a =sentence.count("excellent")
    b = sentence.count("good")
    c = sentence.count("smile")
    d = sentence.count("Happiness")
    e = sentence.count("Laugh")
    f = sentence.count("Love")
    g =sentence.count("Excellent")
    h = sentence.count("Good")
    i = sentence.count("Smile")
    number_H = x+y+z+a+b+c+d+e+f+g+h+i
    return number_H
def number_sad(sentence):
     sentence = sentence.lower()
     j = sentence.count("bad")
     k = sentence.count("sad")
     l = sentence.count("terrible")
     m =sentence.count("horrible")
     n = sentence.count("problem")
     o = sentence.count("hate")
     p = sentence.count("Bad")
     q = sentence.count("Sad")
     r = sentence.count("Terrible")
     s =sentence.count("Horrible")
     t = sentence.count("Problem")
     u = sentence.count("Hate")
     number_S = j+k+l+m+n+o+p+q+r+s+t+u
     return number_S

print("Sentiment: " + ("+" * number_happy(sentence)) + ("-" * number_sad(sentence)))

if number_happy(sentence) > number_sad(sentence):
    print("This is a happy sentence.")
elif number_happy(sentence) == number_sad(sentence):
    print("This is a neutral sentence.")
elif number_happy(sentence) < number_sad(sentence):
    print("This is a sad sentence.")

 
