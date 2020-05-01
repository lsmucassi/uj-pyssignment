#create an empty list
user_val_list = []

#get numbers from a user
for i in range(0,6):
    num = input("Enter a number: ")
    user_val_list.append(num) #append method add the num value entered to the list

#convert list to tuple - create the tuple 
user_val_tpl = tuple(user_val_list) 
print("The Lowest number is: ", min(user_val_tpl))
print("The Highest number is: ", max(user_val_tpl))