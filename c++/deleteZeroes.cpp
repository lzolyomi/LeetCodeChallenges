#include <iostream>
#include <vector>

using namespace std;

void moveZeroes(vector<int> &nums)
{
    vector<int>::iterator it;
    it = nums.begin();         // iterator starts at beginning of vector
    int begin = 0;             // pointer starting at first element
    int end = nums.size() - 1; // pointer starting at last element
    while (begin != end)       // until two pointers do not meet
    {
        if (nums[begin] == 0)
        {
            nums.erase(it + begin);
            nums.push_back(0);
            end--;
        }
        else
        {
            begin++;
        };
    }
};

void printArray(vector<int> nums)
{
    cout << "[";
    for (const auto &n : nums)
    {
        cout << n << ", ";
    };
    cout << "]";
};

int main()
{
    vector<int> test;
    test.push_back(0);
    test.push_back(0);
    test.push_back(1);
    printArray(test);
    moveZeroes(test);
    printArray(test);
}