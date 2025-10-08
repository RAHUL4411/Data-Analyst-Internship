
'''def palindrome():
    a=input("Enter the string:")
    z=a.lower()
    if(z==z[::-1]):
        print(z,"is palindrome")
    else:
        print(z,"is not a palindrome")
palindrome()'''


a=input("Enter the word:")
def letter_freq(text):
    text=text.lower()
    letter={}
    space=0
    for i in text:
        if i==' ':
           space += 1
        elif i.isalpha():
            if i in letter:
                letter[i] += 1
            else:
                letter[i] = 1
    for letter, count in letter.items():
        print({letter:count})
letter_freq(a)


'''a=[]
def adding_elements():
    while True:
        i=input("Add a number to this list: ")
        i.lower()
        if i=="yes":
            b=int(input("Enter the number: "))
            a.append(b)
        elif i=="no":
            print("list:", a)
            break
        else:
            print("invalid")
adding_elements()'''







