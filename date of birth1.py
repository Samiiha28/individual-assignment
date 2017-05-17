import datetime
print('THE PROGRAM TO OUTPUT THE DAY OF BIRTH')
y=int(input('Input your year of birth: '))
m= int(input('Input your month of birth: '))
d= int(input('Input your date of birth: '))


p = datetime.date(y,m,d)
print ( 'You were born on', p.strftime('%a'), str(d) + '/'+ str(m) + '/'+ str(y))
