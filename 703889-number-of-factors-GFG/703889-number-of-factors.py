class Solution:
    def countFactors (self, n):
        from math import sqrt 
        count=0
        for i in range(1,int(sqrt(n)+1)):
            if n%i==0:
                count+=1
                if n//i!=i:
                    count+=1
        return count
                
            
            
        # code here
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna