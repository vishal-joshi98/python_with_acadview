# que 6: implement stack and queue using list
def stack(lis):
  a=int(input("ENTER 1 FOR POP AND 2 FOR PUSH"))
  if a==1:
    lis.remove(lis[0])
    print("AFTER POP FROM STACK  LIST:",lis)
  else:
    b=int(input("ENTER THE VALUE WHICH YOU WANT TO PUSH INTO STACK"))
    lis.insert(0,b)
    print("AFTER PUSH THE VALUE INTO STACK LIST:",lis)

def que(lis):
  c=int(input("ENTER  1 FOR DELETION AND 2 FOR INSERTION"))
  if c==1:
    lis.remove(lis[0])
    print("AFTER THE DELETION FROM QUEUE LSIT:",lis)
  else:
    d=int(input("ENTER THE ELEMENT WHICH YOU WANT TO INSERT INTO QUEUE"))
  lis.append(d)


                                  
lis=list(input("ENTER THE LIST "))
p=int(input(" ENTER 1 FOR STACK IMPLEMENTION AND 2 FOR QUEUE"))
if p==1:
  stack(lis)
else:
  que(lis)
                  
            
            
