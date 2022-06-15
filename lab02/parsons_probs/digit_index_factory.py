def digit_index_factory(num, k):
    """
    Returns a function that takes no arguments, and outputs the offset
    between k and the rightmost digit of num. If k is not in num, then
    the returned function returns -1. Note that 0 is considered to
    contain no digits (not even 0).
    >>> digit_index_factory(34567, 4)() # .Case 1
    3
    >>> digit_index_factory(30001, 0)() # .Case 2
    1
    >>> digit_index_factory(999, 1)() # .Case 3
    -1
    >>> digit_index_factory(1234, 0)() # .Case 4
    -1
    """
    "*** YOUR CODE HERE ***"
    if num == 0 or str(k) not in str(num):
        def f():
            return -1
        return f
    else:
        s = str(num)
        # TODO: next function
        for i in range(len(s) - 1, -1, -1):
            if s[i] == str(k):
                def f():
                    return len(s) - i - 1
                return f   