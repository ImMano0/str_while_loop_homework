def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0 
    count = 0
    while a < len(s):
        if s[a].isdigit() and int(s[a])%2==0:
            a+=1 
        count+=1

    return count 

print(main('41554894987987987456458'))