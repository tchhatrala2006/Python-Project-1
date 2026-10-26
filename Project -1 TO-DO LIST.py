user=int(input("Enter the TO-DO LIST Number: "))
l=[]
d={}
for i in range(1,user+1):
    todo=input("Enter the TO-DO LIST: ")
    l.append(todo)
    d[i]={
        i:todo
    }
if l and d:
    for i,j in enumerate(l,start=1):
        print(f"{i}-{j}")
    for key,value in d.items():
        print(f"{key}-{value}")
    