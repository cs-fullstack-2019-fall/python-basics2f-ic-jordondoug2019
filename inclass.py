#Practice: Random and f-string formatting
# import random
#
#
# name_list=["boib","joe","fox","kobe"]
# randomNumber=random.randint(0,len(name_list)-1)
# #print(randomNumber)
# # print(name_list[randomNumber])
# #can use with arrays/list
#
# rand=random.sample(name_list,2)
# print(rand)

fname="kevin"
lname="yancy"
city="Memphis"

# welcomeText="hello "+fname+" "+lname+" "+ "from"+" "+city+ "!!! "
welcometext2= f"Hello {fname} {lname} from {city}!!!"
print(welcometext2)