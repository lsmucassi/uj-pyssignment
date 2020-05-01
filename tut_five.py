try:
    with open("covid.txt") as rona:
        covid = rona.read()
except FileNotFoundError:
    covid = None

corona_file = [k for k in covid.split("\n") if len(k)>3] #list comprehence
lockdown = {k.split(":")[0]:k.split(":")[1] for k in corona_file}
# print(type(lockdown)) check if it is a dictionary

#test with key & value
for key,val in lockdown.items():
    print (key, "=>", val)

print(lockdown)
