print("\t"*2+"Title")
print("Hello")
print("Hello World")
a=5
b=12.3456789
c=a+b

#Wrong code
#d="A number " + b #TypeError : String could only be conconate with a string
d="A number " + str(b)  #Solution : Cast b as a string

e=a+ \
    b+ \
    c
f=2
g=a/f

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)