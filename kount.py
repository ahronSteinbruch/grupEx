count_sec = int (input ("enter sec"))
h = count_sec//3600
m = count_sec%3600
fm = m//60
s = m&60 
print (count_sec,"=",h,"= hours",",",fm,"= minutes",",",s,"= seconds",".")