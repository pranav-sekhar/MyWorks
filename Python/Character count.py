s="Pranav"
c=[]
for i in s:
    if i not in c:
        print(i,"-",s.count(i))
        c.append(i)
