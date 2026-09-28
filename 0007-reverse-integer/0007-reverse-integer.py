class Solution:
    def reverse(self, x: int) -> int:
        nums=x
        ans=0
        flag=0
        if x<0:
            x=abs(x)
            flag=1
        while x>0:
            last_digit=x%10
            ans=ans*10+last_digit
            x//=10
        if flag==1:
            ans = -ans
        if -2**31>ans or ans>2**31-1:
            return 0

        
        
        return ans


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna