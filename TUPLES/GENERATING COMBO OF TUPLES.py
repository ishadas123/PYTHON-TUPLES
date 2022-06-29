#GENERATING COMBO OF TUPLES
l1=[]
ctl=[]
n1=int(input("Enter number of elements of first list : "))
print("Enter the elements of first list : ")
for i in range(0,n1):
 ele1=int(input())
 l1.append(ele1)
l2=[]
n2=int(input("Enter number of elements of first list : "))
print("Enter the elements of second list : ")
for i in range(0,n2):
 ele2=int(input())
 l2.append(ele2)
print("First list : ",l1)
print("Second list : ",l2)
for i in l1:
 for j in l2:
  if(i!=j):
   ctl.append((i,j))
print("List of tuples : ",ctl)
  