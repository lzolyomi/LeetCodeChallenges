#include <iostream>
#include <vector>

using namespace std;

int solutionLegacy(vector<int> &height)
{
    int maxCapacity = 0; // Store max capacity
    int n = height.size();
    for (int i = 0; i < n; i++)
    {                                // outer loop for first element
        int firstHeight = height[i]; // first pillar, accessed by index of outer loop

        for (int j = i + 1; j < n; j++)
        {                                                     // inner loop for second element
            int secondHeight = height[j];                     // second pillar, accessed by index of inner loop
            int width = abs(i - j);                           // width of container defined by difference between indices
            int lowerHeight = min(firstHeight, secondHeight); // take the lower pillar
            int capacity = lowerHeight * width;               // total capacity of water tank

            if (capacity > maxCapacity)
            {
                cout << "Highest capacity achieved: " << capacity << " at indices: " << i << ", " << j << endl;
                maxCapacity = capacity;
            }
        }
    }
    cout << "Highest capacity container: " << maxCapacity << endl;
    return maxCapacity;
};

int solution(vector<int> &height)
{
    int maxSize = 0;       // store largest size
    int size;              // store size of current container
    int n = height.size(); // number of elements in list
    int begin = 0;         // index pointer at beginning of sequence
    int end = n - 1;       // index pointer at end of sequence

    while (begin != end)
    { // iterate towards the middle of the array
        int width = end - begin;
        size = min(height[begin], height[end]) * width; // calculate height
        if (size > maxSize)
        { // if size is largest seen so far, update maxSize
            maxSize = size;
        };
        // check which pointer to move (always move one with smaller height)
        if (height[begin] < height[end])
        { // begin height smaller, increase begin pointer
            begin++;
        }
        else if (height[end] < height[begin])
        { // end height smaller, decrease end pointer
            end--;
        }
        else if (height[begin] == height[end])
        { // same height, move both pointers towards center
            begin++;
            end--;
        };
    };
    return maxSize;
};

int main()
{
    vector<int> a1 = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    vector<int> a2 = {1, 1};
    cout << solution(a1);
};