class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lst = s.split()
        word=''
        for i in s_lst:
            for j in i:
                if j.isalnum():
                    word+=j.lower()
        if word == word[::-1]:
            return True
        return False