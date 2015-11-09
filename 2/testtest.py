def func_name(argument):
    """
    >>> func_name(2)
    4
    """
    #Some code
    return argument*2

if __name__ == "__main__":
    import doctest
    doctest.testmod()