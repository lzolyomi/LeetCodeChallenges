// This exercise is from HackerRanks
#include <iostream>
#include <vector>

using namespace std;

int hourglassSum(vector<vector<int>> arr)
{
    int rowBegin = 0;        // first element's row index
    int colBegin = 0;        // first element's column index
    int n = arr.size();      // assuming an n x n matrix (square)
    vector<int> results;     // store results for all hourglass sums
    int maxSum = -100;       // Stores highest sum seen so far
    while (colBegin < n - 2) // we cannot go to n - 2 begin row, bc of index overflow
    {
        rowBegin = 0; // reset rowBegin to upmost position
        while (rowBegin < n - 2)
        {
            int curSum = arr[rowBegin][colBegin] + arr[rowBegin][colBegin + 1] + arr[rowBegin][colBegin + 2] +
                         arr[rowBegin + 1][colBegin + 1] + arr[rowBegin + 2][colBegin] + arr[rowBegin + 2][colBegin + 1] +
                         arr[rowBegin + 2][colBegin + 2];
            results.push_back(curSum);
            if (curSum > maxSum) // update maximum
            {
                maxSum = curSum;
            };
            rowBegin++; // move row begin downwards
        };
        colBegin++;
    }
    return *max_element(results.begin(), results.end());
}

int main()
{
    vector<vector<int>> test{
        {-1, -1, 0, -9, -2, -2},
        {-2, -1, -6, -8, -2, -5},
        {-1, -1, -1, -2, -3, -4},
        {-7, -3, -3, -2, -9, -9},
        {-1, -3, -1, -2, -4, -5}};
    cout << hourglassSum(test) << endl;
    // cout << test[1][4];
}