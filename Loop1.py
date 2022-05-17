#loop to a, where a is a number with correcting wrong entry
a = input()
print (a)
count=1
x=1
while x==1:
 try:
  b=int(a)*int(a)
  print(b)
  x=0
 except ValueError:
  print('try again this time type number')
  x=1
  a= input()
count=1
while count <= int(a):
 print(count)
 count+=1
print("this is the end of the program")
