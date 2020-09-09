a=[]
for count in range(2,101) :
    for check in range(2,count):
        if(count%check == 0):
            break
    else:
        a.append(count)
print(a)

def ilearning(mission):
    if (mission == 'create'):
        my_file = open("created.py", "w+")
        my_file.write("""
a=[]
for count in range(2,101) :
    for check in range(2,count):
        if(count%check == 0):
            break
    else:
        a.append(count)
print(a)
""")
ilearning('create')