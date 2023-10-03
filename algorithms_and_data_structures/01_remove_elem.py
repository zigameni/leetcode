
def removeElement(nums, val: int)->int:
  k = len(nums);
  i = 0;
  while(i < len(nums)):
    if (nums[i]==val):
      del nums[i];
      k-=1;
    else:
      i+=1;
  
  return k;

# example
nums = [0,1,2,2,3,0,4,2]; 
val = 2;
k = removeElement(nums, val);
print(k);