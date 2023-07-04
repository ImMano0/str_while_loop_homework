def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """ 
    l = 'asdfas'
    a,b =0, 0 
    while a < len(s):
        if not s[a].lower() in l and s[a].isalpha():
            a+=1 
        b+=1 
    return b 

print(main('CodeShoolUz'))