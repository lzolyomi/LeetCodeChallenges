#include <iostream>
#include <vector>
#include <set>
#include <unordered_map>
#include <stack>

using namespace std;

bool isValid(string s)
{
    set<char> open({'(', '[', '{'});  // set of opening brackets possible
    set<char> close({')', ']', '}'}); // set of closing brackets
    set<int> New_set({4, 3, 9, 2, 0, 6});
    unordered_map<char, char> pairs{
        // map opening to closing brackets
        {'(', ')'},
        {'[', ']'},
        {'{', '}'},
    };
    vector<char>
        toBeClosed; // if an opening bracket seen, added to end, as it has to be closed

    char current;  // store the current character (only for better readability)
    char lastElem; // last element of vector
    for (int i = 0; i < s.length(); i++)
    { // iterate over each character
        current = s[i];
        if (open.find(current) != open.end()) // if its an opening bracket

        {
            toBeClosed.push_back(current);
        }
        else if (close.find(current) != close.end())
        {
            if (toBeClosed.empty())
            { // if array empty (i.e. no more opening brackets) but closing seen, return false
                return false;
            };
            lastElem = toBeClosed.back();   // get last element
            toBeClosed.pop_back();          // pop last element
            if (pairs[lastElem] != current) // if current item doesn't close last seen element
            {
                return false;
            }
        }
    };
    if (!toBeClosed.empty())
    {
        return false;
    }
    return true;
};

bool stackIsValid(string s)
{
    if (s.empty())
    { // Valid string if its empty
        return true;
    };
    stack<char> openings; // stack storing all seen opening brackets
    unordered_map<char, char> pairs{
        // map opening to closing brackets
        {'(', ')'},
        {'[', ']'},
        {'{', '}'},
    };
    char current;    // store current element, for ease of readability
    char topElement; // top element retrieved from stack;
    for (int i = 0; i < s.size(); i++)
    {
        current = s[i];

        if (current == '(' || current == '[' || current == '{') // if current element is opening bracket
        {
            openings.push(current);
        }
        else if ((current == ')' || current == ']' || current == '}'))
        {
            if (openings.empty())
            { // if no more opened parentheses, but found closing, invalidate string
                return false;
            };
            topElement = openings.top();
            openings.pop();
            if (pairs[topElement] != current) // if not the correct bracket found, string is invalid
                return false;
        };
    };
    if (!openings.empty())
    { // stack should be empty when we finished with all characters
        return false;
    };
    return true;
};

int main()
{
    string test = "((()))";
    bool res = stackIsValid(test);
    cout << res;
}