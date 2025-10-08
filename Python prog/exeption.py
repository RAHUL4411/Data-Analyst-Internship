


try:
    a=int(input("Enter an 1st number :"))
    b=int(input("Enter an 2st number :"))

    c=a+b
   
except ZeroDivisionError:
    print("Can't divide by zero")

except ValueError:
    print("Enter an valid integer")
else:
    print(c)
    print('transactiom siccess')
finally:
    print('thank you')