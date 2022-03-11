# Day 1 python exercise Question 1 Unique Letters

a= input("Enter your Vocabulary:")
#print(a)
#a = "Hello World"
b = a.replace(" ","")
b2 = b.upper()
#print(list(b2))
string_parameter = list()
count = 0

for i in list(b2):
    if i not in string_parameter:
        string_parameter.append(i)
        count = count+1
    else:
     pass
final_list = string_parameter
print(final_list, count)


# Question 2
a= input("Enter your Vocabulary:")
#a = "Hello World"
b = a.replace(" ","")
Uppercase = 0
Lowercase = 0

for i in list(b):
    if i.isupper() == 1:
        Uppercase = Uppercase+1
    if i.isupper() == 0:
        Lowercase = Lowercase+1

print("Uppercase:",Uppercase,"Lowercase",Lowercase)
