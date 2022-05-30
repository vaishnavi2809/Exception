# Write a program in Python to check whether a file exixts or not use exception handling to deal with an error if occurs.
try:
	f=open("exce.txt","r")
	str=f.read()
	print(str)
except:
	print("File does'nt exists")
else:
	print("File found")
finally:
	print("Hello")
