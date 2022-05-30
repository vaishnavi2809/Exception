#Write a Program to raise an Error
try:
    a=int(input("Enter the no"))
    if a==5:
        raise ValueError("Do not Enter 5 ")
    print(a)
except Exception as e:
    print(e)
    print("Value Error")
else:
    print("Program Executes without any Error")
finally:
    print("Stay blessed and safe")
