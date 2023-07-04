def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    a = 0
    count = 0
    while a < len(s):
        if s[a].isdigit():
            a += int(s[count])
        count += 1

    return a 

print(main('84848484'))