class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        if (self.isPalindrome(A)):
            return 0
        
        for i in reversed(range(len(A))):
            string = A[:i] 
            if (self.isPalindrome(string)):
                return (len(A)) - i
        
        return len(A) - 1

    
    def isPalindrome(self, string):
        start = 0
        end = len(string) -1 

        rev = string[::-1]

        if (string == rev):
            return True
        
        return False
