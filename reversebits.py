def reverseBits(n):
    mean = "{0:032b}".format(n) #convert n to 32bit
    reversemean = mean[::-1]  #reverse
    return(int(reversemean,2)) #convert binary to decimal

print(reverseBits(6))