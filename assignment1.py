m = int(input("Enter marks of student:"))
if m >= 90 and m <= 100:
  print('A+')
elif 80 <= m < 90: 
  print('A')
elif 70 <= m < 80:
  print('B')
elif  60 <= m < 70:
  print('C')
elif  50 <= m < 60:
  print('D')
else:
  print('Fail')
