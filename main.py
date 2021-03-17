list1 = ['hello','cherry','keyboard','pineapple','peanuts',"mouse"] #list of random words

letters = 0

#Nested loop
for x in range(0,len(list1)): #loops through each word in the list
    for y in range(0, len(list1[x])): #loops through each letter in each word
        letters = letters + 1 #every letter adds one to the counter

#Results
print("Total words:", len(list1))
print("Total letters:", letters)
print("Average letters per word:", letters/len(list1))
