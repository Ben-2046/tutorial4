def solveCubic(a,b,c,d):
    b1 = (-b**3)/(27*a**3) + (b*c)/(6*a**2) + (-d)/(2*a)
    b2 = (c)/(3*a)+(-b**2)/(9*a**2)
    b3 = (-b)/(3*a)
    x = (b1+(b1**2+b2**3)**(1/2))**(1/3) + (b1-(b1**2+b2**3)**(1/2))**(1/3) + b3
    x = str(x.real)
    line = "The root of the cubic is "+x
    return(line)

print("I can solve cubics with 3 real roots i.e. ax^3+bx^2+cx+d=0.")
name = input("What is your name?")
a = int(input("What is your a?"))
b = int(input("What is your b?"))
c = int(input("What is your c?"))
d = int(input("What is your d?"))

line = "Hello "+name.capitalize()+", I will solve "+str(a)+"x^3+"+str(b)+"x^2+"+str(c)+"x+"+str(d)+"=0."
line = line.replace("+-","-")
line = line.replace(" 1x^3"," x^3")
line = line.replace(" -1x^3"," x^3")
line = line.replace("+1x^2","+x^2")
line = line.replace("-1x^2","-x^2")
line = line.replace("+1x","+x")
line = line.replace("-1x","-x")
print(line)

print(solveCubic(a,b,c,d))

quit()