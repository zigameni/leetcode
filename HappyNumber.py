class Solution:
    def squareSum(self, n):
        sum = 0
        while(n):
            sum = sum + (n%10)*(n%10)
            n = int(n/10)
        return sum
    
    def isHappy(self, n: int) -> bool:    
        first = True
        seen = set()
        seen.add(n)
        sum = 0
        while(True):     
            if(sum not in seen):
               
                if(first):
                    sum = n
                    first = False
                    
                sum_temp = self.squareSum(sum)
                seen.add(sum)
                sum = sum_temp
                
                if(sum == 1):
                    return True   
            else: 
                return False
            
            
            
                
            
        
        
        
                