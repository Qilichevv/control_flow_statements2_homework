def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    s=0
    x1=n%10
    n//=10
    if(s<x1):
        s=x1
    x2=n%10
    n//=10
    if(s<x2):
        s=x2
    x3=n%10
    n//=10
    if(s<x3):
        s=x3
    x4=n%10
    n//=10
    if(s<x4):
        s=x4
    x5=n%10
    n//=10
    if(s<x5):
        s=x5
    return s