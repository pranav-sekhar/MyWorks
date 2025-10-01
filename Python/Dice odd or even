#if dice odd,print sum of num at even pos
#if dice even,print sum of num at odd pos
num = 328645
dice = 2 
s = 0 
n = str(num) #store num as string to n to check len
if dice % 2 == 0: #if dice is even(here its even so this loop executes)
    for i in range(0,len(n),2): #odd position(0,2,4...)
        s = s + int(n[i]) #sum of n at odd pos 
else: #if dice is odd
    for i in range(1,len(n),2): #even position(1,3,5...)
        s = s + int(n[i]) #sum of n at even pos
print(s)

#Output - 15 (3+8+4)
