value = "abc"

def is_palindrome(value):
    left = 0
    right = len(value) - 1
    while left < right:
        if value[left] != value[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome(value))