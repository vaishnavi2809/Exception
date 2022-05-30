#Write a program to deal with AssertionError.
try:
    a=eval(input("Enter a number"))
    assert a==5,"Other number are not allowed except 5"
    print("Number is:",a)
except AssertionError as e:
    print(e)
