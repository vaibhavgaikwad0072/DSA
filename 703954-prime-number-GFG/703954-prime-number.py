class Solution:
    def isPrime(self, n):
        # code here
        if n==1:
            return False
        for i in range(2,n):
            if n%i==0:
                return False
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna