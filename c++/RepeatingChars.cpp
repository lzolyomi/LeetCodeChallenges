#include <iostream>
#include <unordered_map>

using namespace std;

int lenSubstring(string s)
{
    int maxLength = 0;                // highest length substring seen
    int lengthCount = 0;              // count length of current substring
    int lastReset = 0;                // store index at which we last reset the substring
    unordered_map<char, int> charPos; // store index of each character seen in substring

    for (int i = 0; i < s.length(); i++)
    {

        if (charPos.find(s[i]) != charPos.end())
        { // if character seen
            cout << "Character " << s[i] << " already seen" << endl;
            if (charPos[s[i]] > lastReset)
            { // if character seen AFTER we last reset the substring
                lastReset = charPos[s[i]];
            };
            lengthCount = i - lastReset; // length of new substring starts from last point we seen the character
            charPos[s[i]] = i;           // update character last seen position
        }
        else
        {                      // if character NOT seen yet
            charPos[s[i]] = i; // store that char was last seen at current index
            lengthCount++;     // increase counter
            cout << "Character " << s[i] << " seen, stored at index " << charPos[s[i]] << " with current length " << lengthCount << endl;
        };
        if (lengthCount > maxLength)
        {
            maxLength = lengthCount;
        };
    }

    return maxLength;
}

int main()
{
    string test = " ";
    cout << lenSubstring(test);
}