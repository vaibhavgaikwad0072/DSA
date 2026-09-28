class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        ans=0
        if x<0:
            return False
        while num>0:
            last_digit=num%10
            ans=ans*10+last_digit
            num//=10
        return x==ans

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna