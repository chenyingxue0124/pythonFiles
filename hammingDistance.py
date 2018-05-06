def hammingDistance(x,y):#计算两个二进制的数中不同数字的数量，这个就是hamming距离
    return(bin(x^y).count("1")) #^二进制中相同的取0，不同的取1，bin是表示二进制，count是计算里面的1的数量.


print(hammingDistance(1,4))
  
  

  