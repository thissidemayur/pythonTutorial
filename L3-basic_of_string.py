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

salary="10000k salary/month"
# formating using fString or .format()
print("\n formating using fString or .format(): ")
print(f"{info} {salary}")
print(F"This side mayur here and i want min {salary}")

# ESCAPE CHARACTER: 
print("\nESCAPE_CHARACTER: ")
print("Double_quoute [\"]: this is \"mayur\"")
print("Backslash[\\]: maya \\ kali")
print("new line [\n]")
print("Carraige return :this is mayur here ")
print("tab [\t]:"+"mayur")
print("Backspace [\b]: mayur\b ")
char = "\110\145\154\154\157\256\111\123" 
print(f"OctalValue [\000] {char}",)

print("\n\nOpereators: ")
print("1. is operator: retur true if both object has same memory location irresective they are equall or not")
print("2. in operator: retur true if given element is present in sequence ")
print("\n\nOperator Presedence: ","(),** , / * % // , +  - , <<  >>  , & , ^ , | , comparsion , not , and , or")

