def hammingWeight(n):
    mean = "{0:032b}".format(n) #convert to 32bit binary
    return(mean.count("1")) #calculte the number of 1

print(hammingWeight(11))