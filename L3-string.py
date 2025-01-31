name="mayur",'pal'
print("single line string:",name)

# multiple line print:
info=''' this side mayur here
stding btech cse from LPU, Phagwara 
looking for job 
'''
print("multiple line string: ",info)

# string is array here there no char data type so to access char print [0]
greet ="Namaste duniya kese ho! "
print("Access 1 position:",greet[0])

# find word is present or not. use -> in opereator if it present it return true else false
if("Namaste" in greet):
    print("Namaste is present:",greet)

if("World" in greet):
    print("Word is present:",greet)
else:
    print("Word is not present:",greet)

# loop in string

print("Loop in string: ")
for i in greet:
    print(i)

# find length:
print("Length of String:",len(greet))



