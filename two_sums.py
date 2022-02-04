def twoSum( nums, target):
        """
        :type nums: List[int]
        :type target: num
        :rtype: List[int]
        """
        #nums = np.zeros(dtype='int')
        counter1=0
        num=0
        limit= len(nums)-1
        counter=1
        while True:
            if counter== limit:
                counter1+=1
                counter= counter1+1
            num= nums[counter1] + nums[counter]
            if num== target:
                break
            counter+= 1
        print ([counter,counter1])   

a= [2, 5, 5,11]
ts= twoSum(a,10)     
