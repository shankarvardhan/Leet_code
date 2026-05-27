class Solution:
    def isPalindrome(self, x: int):
        orgnum=x
        rev=0
        
        while x>0:
            num1=x%10
            rev=rev*10+num1
            x=x//10
        return orgnum==rev
        