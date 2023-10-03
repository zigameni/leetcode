
def remove_duplicates(nums):
  i = 0;
  k = len(nums);
  if(k<2):
    return k;
  
  while(i<k):
    if(nums[i]==nums[i-1]):
      del nums[i];
      k-=1;
    else:
      i+=1;

  return k;


# nums = [0,0,1,1,1,2,2,3,3,4];
nums = [0];
k = remove_duplicates(nums);

for i in nums:
  print(f"{i}, ");

print("");
print(k);