def leap(year):
  if(year%4==0 and year%100!=0) or year%400==0 :
    return 1
  else:
    return 0
year=int(input("Enter a Year"))
l=leap(year)
if l==1:
  print(year,"is a leap year")
else:
  print(year,"is not a leap year")