class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i=0;
        lenArr = len(nums)
        resultArr=[]
        while i < lenArr:
            a=nums[i]
            j = i + 1
            while j < lenArr:
                b = nums[j]
                k = j+1
                while k < lenArr:
                    c = nums[k]
                    #print([a,b,c])
                    if a+b+c == 0:
                        resultArr.append([a,b,c])
                    k = k+1
                j = j+1
            i = i+1
        #Remove Duplicates
        i=0;j=0;
        while i<len(resultArr):
            j=i+1
            resI = resultArr[i]
            print("i->",resI)
            while j<len(resultArr):
                resJ = resultArr[j]
                print("j->",resJ)
                if (resJ[0] in resI and resJ[1] in resI and resJ[2] in resI):
                    print("Deleteing",resultArr[j])
                    del resultArr[j]
                j = j+1
            i=i+1
                
        return resultArr
                
            
            
        
        
        
        
