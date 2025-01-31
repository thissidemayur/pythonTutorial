name= "mayur"
print(name)


print(type(name))

# explicity data conversion 
roll_no =4
print(type(roll_no))
roll_no = float(roll_no)
print(type(roll_no))
roll_no = str(roll_no)
print(type(roll_no))

# asssigning many value to multiple variable
name1 , name2 ="mayur","sameer"
print(name1,"and",name2 )

# one value to multipe variable
class1=class2=class3=12
print("class1:",class1,"class2:",class2,"class3:",class3)

# unpacking: extraction of value from list called unpacking
fruits=["apple","mango","banana","pineapple"]
a,m,b,p=fruits
print(a,b,m,p)

# gloabal variable in python: 2 ways declare vairble outside of fn or using gloabl keywaord
name="aman pal"
def fun1():
    print("global variable: ",name)

def fun2():
    global user_name
    user_name="thissidemayurhere"
    print("global varible inside funciton: ",user_name)

fun1()
fun2()

print("global variable outside function:",user_name)

x=1+1j
print("imaginary numm:",x)

num1=int("123")
print("num1:",num1,"type: ",type(num1))


