def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    mean = "{0:032b}".format(n)
    return(mean.count("1"))

print(hammingWeight(11))


