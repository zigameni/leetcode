#include <iostream>
#include <vector>
using namespace std;

int removeElement(vector<int>& nums, int val){
  int k = nums.size();
  int i = 0;

  while(i<k){
    if(nums[i]==val){
      nums.erase(nums.begin()+i);
      k--;
    }else{
      i++;
    }
  }

  return k;
}

// To run
// g++ 01_remove_elem.cpp -o 01_remove_elem
// ./01_remove_elem
int main(){
  vector<int> nums = {0, 1, 2, 2, 3, 0, 4, 2};
  int val = 2;
  int k = removeElement(nums, val);
  cout<<k<<endl;

  return 0;
}