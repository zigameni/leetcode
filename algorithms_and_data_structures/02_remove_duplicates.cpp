#include <iostream>
#include <vector>
using namespace std;

vector<int> shuffle(vector<int>& nums, int n){
  int j = n;
  vector<int> nums1;
  for(int i =0; i<n; i++){
    nums1.push_back(nums[i]);
    nums1.push_back(nums[j]);
    j++;
  }

  return nums1;
}

// To run
// g++ 01_remove_duplicates.cpp -o 01_remove_duplicates
// ./01_remove_duplicates
int main(){
  vector<int> nums = {0, 1, 2, 2, 3, 0, 4, 2};
  int n = 4;
  vector<int> nums1 = shuffle(nums, n);
  
  cout << "Shuffled array: ";
    for (int num : nums1) {
        cout << num << " ";
    }
  cout << endl;
  return 0;
}