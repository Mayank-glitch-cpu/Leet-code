class ListNode:
    def __init__(self,value):
        #self.head = None
        self.next = None
        #self.disp= []  
        self.value= value  

class linked_list:
    def __init__(self):
        self.head= None
        
    def insert(self, value):
        newNode= ListNode(value)
        newNode.next= self.head
        self.head= newNode

    def traverse(self):
        arr=[]
        temp= self.head
        while temp!= None:
            arr.append(temp.value)
            #print(temp.value)
            temp= temp.next 
        print(arr)
        pow= len(arr) -1 
        div=10**pow
        sum=0
        for val in arr:
            sum+= div*val
            pow-=1
            print= sum
        #strings= [str(x) for x in arr]
        #string= ''.join(strings)
        #print(string)
        #intarr= int(string)
        print(sum)
        return sum    
    

    def traverse_reverse(self):
        arr=[]
        temp= self.head
        while temp!= None:
            arr.append(temp.value)
            #print(temp.value)
            temp= temp.next 
        return arr      

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp_l= linked_list()
        a1=l1.traverse()
        a2=l2.traverse()
        
        #print(a1)
        #print(a2)
        
        sum=a1 + a2 
        #print(sum)
        sum1=str(sum)
        
        disect_sum=[]

        for ch in range(0,len(sum1),1):
            disect_sum.append(sum1[ch:ch+1])
            temp_l.insert(disect_sum[ch])
        print(temp_l.traverse_reverse())    


        
        #for val1 in disect_sum:
        #    temp_l.insert(val1)
        

        

l1= linked_list()
l1.insert(6)
l1.insert(9)
l1.insert(4)
l1.insert(5)
#l1.traverse()

l2= linked_list()
l2.insert(5)
l2.insert(3)
l2.insert(8)
#l2.traverse()

l3= linked_list()
l3.addTwoNumbers(l1,l2)


