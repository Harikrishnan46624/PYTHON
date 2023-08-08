import datetime

now=datetime.datetime.now()

print(now.strftime("%d:%m:%y"))

print(datetime.date.today())

print(datetime.date.today().month)

x=datetime.datetime(year=2020,day=4,month=12)
y=datetime.datetime(year=2019,day=3,month=12)

dif=x-y
print(dif)

end=datetime.datetime.now()

diffrence=end-now
print(diffrence)
print(x)

f=open("harish.py","wb+")
f.write("Heyy")
f.close()