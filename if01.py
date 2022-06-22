from operator import truediv


def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and b>c:
        return a
    if a>c or c>b:
        return a
    if b>a and b>c:
        return b
    if a>b or c>b:
        return b
    if c>a and c>b:
        return c
    if a>c or b>c:
        return c