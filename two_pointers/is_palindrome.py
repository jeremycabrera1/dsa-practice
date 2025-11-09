# Given a string s, determine whether it reads the same forward and backward after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.

# If it is a palindrome, return True; otherwise, return False

def is_palindrome(s:str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1

    return True
        