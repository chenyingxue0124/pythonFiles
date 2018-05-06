def arraypartition(nums):
    return sum(sorted(nums)[::2])

print(arraypartition([1,4,3,2,45,7,1,34,0,4]))