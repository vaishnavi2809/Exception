#Write a program to deal with multiple Exceptions in a program.
try:
    a=eval(input("Enter Ist. number"))
    b=eval(input("Enter IInd. number"))
    print(a+b)
    print(a-b)
    print(a/b)
    print(a//b)
    print(a*b)
except  (ZeroDivisionError,ValueError,NameError) as e:
    print(e)
else:
    print("Program does not have any Error")
finally:
    print("Happy Coding")
