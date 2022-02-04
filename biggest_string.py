from tkinter import N


arr= []
string= input('Enter')
div=1


for ch in range(0,len(string)):
    while div <=len(string):
        arr.append(string[ch:div])
        div+=1
        
    div=ch+2

arr1=[]
arr2=[]
final_arr=[]
sum1=0
sum2=0
for ch in arr:
    arr1.append(''.join(set(ch)))
    arr2.append(ch)
    
    for ch1 in arr1[0]:
        sum1= sum1 + ord(ch1)
        
    for ch2 in arr2[0]:
        sum2= sum2+ ord(ch2) 
           
    if sum1== sum2 and sum1!=0 and sum2!=0:    
        final_arr.append(ch)
    arr1=[]  
    arr2=[]  
    
    sum1=0
    sum2=0


set=[]
for ch in final_arr:
    set.append(len(ch))
max= max(set)
for ch in final_arr:
    if len(ch)== max:
        print(ch,end=',')


print(max)    