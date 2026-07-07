import inflect
p = inflect.engine()
names=[]

while True:
    try:
        name=input("Name: ")
        names.append(name)
        
    except EOFError:
        if len(names)==1:
            print("Adieu, adieu, to",name)
            break
        else:
            print("Adieu, adieu, to",p.join(names))
            break


        
        
    