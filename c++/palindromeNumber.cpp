#include <iostream>

using namespace std;

bool isPalindrome(int x)
{
    int copy = x;
    int reversed = 0;

    while (copy >= 1)
    {
        if (reversed > INT32_MAX / 10)
        {
            return false;
        };
        reversed = reversed * 10 + copy % 10;
        copy = copy / 10;
    };
    return reversed == x;
}

int main()
{

    int num = 1234567899;
    if (isPalindrome(num))
    {
        cout << "It is a palindrome";
    }
    else
    {
        cout << "NOT Palindrome";
    }
}