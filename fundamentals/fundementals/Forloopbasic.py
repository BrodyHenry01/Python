for i in range(0, 151):
    print(i)

x=0 
while x <= 995:
	x = x + 5 
	print(x)

for i in range(0 ,101):
    if i % 5 == 0:
        print("Coding")
    elif i % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)

sum = 0
for y in range(1,500001,2):
    sum += y
print(sum)

for c in range(2018,0,-4):
    print(c)


LowNum = 2
HighNum = 9
Mult = 3

for i in range(LowNum,HighNum + 1):
    if i % Mult == 0:
        print(i)