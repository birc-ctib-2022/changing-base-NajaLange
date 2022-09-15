"""Changing bases."""

digits = {}

for i in range(0, 10):
    digits[i] = str(i)
    print(digits[i % 4])
    print( ">", i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'


print(digits)





def change_to_base(n: int, b: int) -> str:
    """
    Return `n` in base `b`.

    The base `b` must be in the range 2 to 16.

    >>> change_to_base(1, 2)
    '1'
    >>> change_to_base(31, 2)
    '11111'
    >>> change_to_base(31, 8)
    '37'
    >>> change_to_base(31, 16)
    '1F'
    """
    assert 2 <= b <= 16
    lst = []
    while n >= b: 
        lst.append(digits[n % b])
        n = n // b 
    else: 
        lst.append(digits[n % b])

    return "".join(lst[::-1])  # FIXME: return n in the right base

print(change_to_base(31, 2))