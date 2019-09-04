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
        # Remove Duplicates
        i = 0;
        j = 0;
        arrLen = len(resultArr)
        while i < arrLen:
            j = i + 1
            resI = resultArr[i]
            resI.sort()
            # print("Checking For",resI)
            while j < arrLen:
                resJ = resultArr[j]
                resJ.sort()
                # print("j->", resJ)
                if resJ[0] == resI[0] and resJ[1] == resJ[1] and resJ[2] == resI[2]:
                    print("Checking for ", resI, "Deleting", resultArr[j])
                    del resultArr[j]
                    arrLen = arrLen - 1
                    j = i + 1
                else:
                    j = j + 1
            i = i + 1
        return resultArr

                
            
            
        
        
        
        
            
            
        
        
        
        
