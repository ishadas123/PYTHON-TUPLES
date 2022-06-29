#REPETATION OF WORDS
l=[]
n=int(input("Enter number of words in the sentence : "))
print("Enter sentence : ")
for i in range(0,n):
 w=str(input())
 l.append(w)
for i in l:
 print(i," ",l.count(i))
