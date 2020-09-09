
a=[]
for count in range(2,101) :
    for check in range(2,count):
        if(count%check == 0):
            break
    else:
        a.append(count)
print(a)
