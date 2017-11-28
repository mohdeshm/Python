names=[]
ages=[]
emailIds=[]

for counter in range(0,3):
    name=raw_input("Enter name")
    age = input("Enter age")
    emailId = raw_input("Enter emailId")
    names.append(name)
    ages.append(age)
    emailIds.append(emailId)
print("names are",names)
print("ages are",ages)
print("email Ids are",emailIds)