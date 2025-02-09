x= int(input("Enter a three-digit number"))
y= x%100//10
z=x//100
s= x%100%10
print (y-(z+s))