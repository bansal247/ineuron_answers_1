l = len(nums)
first = 0
for i in range(l):
    if(nums[i]>0):
        nums[first] = nums[i]
        first+=1

while first<l:
    nums[first] = 0
    first+=1
print(nums)
