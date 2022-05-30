#Write a program to deal with and ZeroDivisionError error.
try:
	a=int(input("Enter  the no."))
	c=1/a
	print(c)
except Exception as s:
	print(s)
else:
	print("we are successfull")

print("OKAY Bye!!")
