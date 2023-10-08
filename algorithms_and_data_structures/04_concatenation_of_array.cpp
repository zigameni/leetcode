#include <vector>
#include <iostream>

using std::vector;

vector<int> getConcatenation(vector<int>& nums) {
        int size = nums.size();
        vector<int> result;
        result.reserve(size*2);

        result.insert(result.end(), nums.begin(), nums.end());
        result.insert(result.end(), nums.begin(), nums.end());

        return result;
}

int main()
{
    vector<int> nums = {1, 2, 1};
    vector<int> result = getConcatenation(nums);

    // Print the updated vector
    for (int element : result) {
        std::cout << element << " ";
    }
}