import matplotlib.pyplot as p

x = [1,2,3,4,5,6,7]
y = [2,3,4,6,8,6,10]

a = ["Audi", "BMW", "Citroen", "D"]
b = [5,10,15,30]

#p.xlabel("X - Independent variable")
#p.ylabel("Y - Dependent variable")

#p.plot(x,y)
#p.plot(x,y, "o")
#p.step(x,y)
#p.bar(x,y)
#p.pie(b, labels = a)
#p.plot(x,y, "yo")
#p.plot(x,y, "yo--")
#p.plot(x,y, "yo:")
p.subplot(2,2,1)
p.plot(x,y, "yo:")

p.subplot(2,2,2)
p.step(x,y)

p.subplot(2,2,3)
p.bar(x,y)

p.subplot(2,2,4)
p.pie(b, labels = a)
p.show()