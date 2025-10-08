'''def details(name,age):
    print("My name is",name)
    print("My age is",age)
details('Rahul',22)'''



'''def num(a,b):
    sum=a+b
    print("The sum of number",sum)
num(10,20)
num(5,8)'''



'''def details(*name):
    print("name is",name[1])
details('rahul','niranjan','arjun')'''



'''def details(name1,name2,name3):
    print("name is",name2)
details(name1='rahul',name2='niranjan',name3='arjun')

def details(**names):
    print("name is",names['name1'])
details(name1='rahul',name2='niranjan',name3='arjun')

'''

'''um = int(input('Enter the number'))

for i in range(2,num):
    if num%i==0:
        print('not prime number')
        break
else:
    print('prime number')'''






'''num = input("Enter a number")

len_num = len(num)
total = 0

for i in num:
    total += int(i)**len_num 

if int(num)==total:
    print('is armstrong number')
else:
    print('is not a armstrong number')'''




'''class Car:

    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def display_info(self):
        print("car makes ",self.make)
    
        print("car model ",self.model)
    
        print("car year ",self.year)

   

obj=Car('Suzuki','swift',2024)
obj.display_info()'''



'''class Rectangle:
    
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        print("the area of a rectangle is",self.length*self.width)

    def perimeter(self):
        print("The perimeter of a rectangle is", 2*(self.length+self.width))

obj=Rectangle(2,3)
obj.area()
obj.perimeter()'''


'''class Student:

    def __init__(self,name,roll_num,marks):

        self.name=name
        self.roll_num=roll_num
        self.marks=marks

    def calculate_grade(self):
        if self.marks>=90 and self.marks<=100:
            print("Grade A+")
        elif self.marks>=80 and self.marks<=90:
            print("Grade A")
        elif self.marks>=70 and self.marks<=80:
            print("Grade B")
        else:
            print("Grade D")

obj=Student("rahul",14,60)
obj.calculate_grade()'''


'''class BankAccount:
    def __init__ (self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        self.balance-=amount
        

    def get_balance(self):
        return 'balance', self.balance
        

obj=BankAccount("rahul",100)
obj.deposit(1000)
obj.withdraw(500)

print(obj.get_balance())'''


'''#single inheritence
class Parent:
    def F(self):
        print("father")


class Child(Parent):
    def S(self):
        print("child")
            

obj=Parent()
obj1=Child()

obj.F()
obj1.S()
obj1.F()'''


'''#multiple inheritence
class Parent:
    def F(self):
        print("father")


class Child():
    def S(self):
        print("child")

class Mother(Parent,Child):
    def M(self):
        print("Mother")
            

obj=Parent()
obj1=Child()
obj2=Mother()

obj.F()
obj1.S()
obj2.M()
obj2.S()
obj2.F()'''





#Multilevel
'''class Grandparent:
    def F(self):
        print("grandparent")


class Parent(Grandparent):
    def S(self):
        print("parent")

class Child(Parent):
    def M(self):
        print("child")

c=Child()
c.F()
c.S()
c.M()'''

'''class Animal:
    def eat(self):
        print("Animal eats.")

class Dog(Animal):
    def bark(self):
        print("Dog barks.")

class Cat(Animal):
    def meow(self):
        print("Cat meows.")

d = Dog()
d.eat()
d.bark()

ct = Cat()
ct.eat()
ct.meow()'''



'''x="HelloWorld"
print(len(x))'''



#Polymorphism
'''class Bird:
    def fly(self):
        print('Bird fly')
class Plane:
    def fly(self):
        print('plane fly')
def flying(obj):
    obj.fly()

b=Bird()
p=Plane()

flying(b)
flying(p)'''



'''x=6
def hii():
    
    x=7
    print(x)
hii()
print(x)'''


'''n1=int(input("Enter an number:"))
n2=int(input("Enter an number:"))
n3=int(input("Enter an number:"))

if((n1>=n2) and (n1>=n3)):
    print(n1)

elif((n2>=n1) and (n2>=n3)):
    print(n2)
else:
 print(n3)'''




'''def square():
    list=[2,4,6,8,10]
    result=[]
    for i in list:
        result.append(i**2)
    return result

print(square())'''



'''list=[2,3,4,5,6,7,8]
def even(numbers):
    result=[]
    for i in numbers:
        
        if i%2==0:
            result.append(i)
    return result
    

print(even(list))'''


'''def Students_details(studs):
    grades={"A":[],"B":[],"C":[],"D":[],"E":[]}

    for name,score in studs:
        if score>=90:
            grades["A"].append(name)
        elif score>=80:
            grades["B"].append(name)
        elif score>=70:
            grades["C"].append(name)
        elif score>=60:
            grades["D"].append(name)
        else:
            grades["E"].append(name)
    return grades
print(Students_details([("rahul",75),("prajith",80),("raghul",95),("niranjan",68)]))'''



'''def stud_det():
    mark={"rahul":[98,85,65],
          "raghul":[90,76,86],
          "prajith":[94,38,78]
          }
    avg_mark={}
    for names,scores in mark.items():

        avg=round(sum(scores)/len(scores))
        
        avg_mark[names]=avg
    return avg_mark
print(stud_det())'''




'''year=int(input("Enter a year: "))
def leap_year():
 
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print( year ,"is leap year")
    else:
        print( year ,"is not leap year")
leap_year()'''


'''def details():
    data={}
    while True:
        name=input("Enter an name:")
        if name.lower()== "done":
            break
        score=int(input("Enter an score:"))
        data[name]=score
    return data
result=details()
print("Data:",result)'''


'''def palindrome():
    a=input("Enter the name:")
    z=a.lower()
    if(z==z[::-1]):
        print(z," is palindrome")
    else:
        print("is not a palindrome")
palindrome()'''


'''def count_word(text):
    text=text.lower()
    words=text.split()
    freq={}
    for word in words:
        freq[word]=freq.get(word,0)+1
    return freq
print(count_word("hello world! hello again"))'''


'''a=[1,1,1,2,2,3,4,4,2,3,5,5,6,7,8,8,7]
def duplicate():
    b=set(a)
    c=list(b)
    print(c)
duplicate()'''


    












        
    
    
    



    
            
        







       


    
    





























        
            












































































