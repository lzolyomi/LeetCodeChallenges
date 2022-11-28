#include <iostream>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    int romanToInt(string s)
    {
        unordered_map<char, int> valueMap;
        char romanChars[] = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
        int integers[] = {1, 5, 10, 50, 100, 500, 1000};
        int arrSize = sizeof(romanChars) / sizeof(romanChars[0]);

        for (int i = 0; i < arrSize; i++)
        {
            valueMap[romanChars[i]] = integers[i];
        };
        char next;      // store next character when iterating over
        char x;         // store current character
        int result = 0; // total result
        for (int i = 0; i < s.length(); i++)
        {
            x = s[i];
            if (i == s.length() - 1)
            {
                next = 'A';
            }
            else
            {
                next = s[i + 1];
            };
            if (valueMap[next] > valueMap[x])
            {
                result += valueMap[next] - valueMap[x];
                i++; // increment loop counter to skip double counting
            }
            else
            {
                result += valueMap[x];
            }
        };

        return result;
    };
};

int main()
{
    Solution s;
    cout << s.romanToInt("CDXIV");
}