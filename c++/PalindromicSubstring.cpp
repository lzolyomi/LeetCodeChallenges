#include <iostream>

using namespace std;

string longestPalSubs(string s)
{
    int indices[2] = {-1, -1}; // store begin and end index for longest palindrome seen so far
    int L, R;                  // will start to go outwards of center point to Left and Right
    int maxLength = 0;         // longest string seen so far (used to update indices)
    for (int i = 0; i < s.length(); i++)
    {
        L = i;
        R = i;                                           // set both to i for centered palindromes
        int even, odd;                                   // store longest palindrome found for even (non-centered) and odd (centered palindromes)
        int tempOdd[2], tempEven[2];                     // Temporary arrays to store begin and end indices for odd and even substring
        while (L >= 0 && R < s.length() && s[L] == s[R]) // check if all conditions still hold for palindrome
        {                                                // odd/centered palindrome check from index i as middle
            L--;                                         // Go to left (beginning of) string
            R++;                                         // Go to right (end of) string
        };
        odd = R - L - 1; // length of longest palindrome
        tempOdd[0] = L + 1;
        tempOdd[1] = R - 1;
        // Do the same for off-centered palindromes
        L = i;
        R = i + 1; // Right iterator starts one up.
        while (L >= 0 && R < s.length() && s[L] == s[R])
        {
            L--;
            R++;
        };
        even = R - L - 1;
        tempEven[0] = L + 1;
        tempEven[1] = R - 1;
        // check if odd or even palindrome is longer
        if (max(even, odd) > maxLength) // if there is a new highest substring
        {
            // cout << "New MAXIMUM found  at index i: " << i << " with max " << max(even, odd) << endl;
            maxLength = max(even, odd);

            if (even > odd)
            {
                // cout << "Even found " << tempEven[0] << ", " << tempEven[1] << endl;
                indices[0] = tempEven[0];
                indices[1] = tempEven[1];
            }
            else
            {
                // cout << "Odd found at " << tempOdd[0] << ",  " << tempOdd[1] << endl;
                indices[0] = tempOdd[0];
                indices[1] = tempOdd[1];
            };
        };
    };
    return s.substr(indices[0], maxLength);
}

int main()
{
    string test = "cbbd";
    cout << longestPalSubs(test);
};