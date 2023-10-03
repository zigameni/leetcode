
def shuffle(nums, n):
  j = n;
  nums1 = []
  for i in range(0,n):
    print(f"{i}, {j}")
    
    nums1.append(nums[i]);
    nums1.append(nums[j]);
    i+=1;
    j+=1;
  
  return nums1

nums = [2,5,1,3,4,7];
n = 3;

nums = shuffle(nums, n);
print(nums)