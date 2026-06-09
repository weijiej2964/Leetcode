class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) <= 0:
            return True
        
        leftPointer = 0
        rightPointer = len(s) - 1

        while not s[leftPointer].isalnum():
            leftPointer += 1
            if leftPointer >= len(s):
                return True
        while not s[rightPointer].isalnum():
            rightPointer -= 1
            if rightPointer < 0:
                return True
        
        while leftPointer < rightPointer:
            if s[leftPointer].lower() != s[rightPointer].lower():
                return False
            leftPointer += 1
            rightPointer -= 1
            while not s[leftPointer].isalnum():
                leftPointer += 1
                if leftPointer >= len(s):
                    return True
            while not s[rightPointer].isalnum():
                rightPointer -= 1
                if rightPointer < 0:
                    return True
        
        return True
