def is_palindrome(n):
    s = str(n)
    s2 = s[-1::-1]
    if s == s2:
        return n

output = filter(is_palindrome, range(1,1000))
print(list(output))
