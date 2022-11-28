#include <iostream>

using namespace std;

int reverse(int x)
{
    int ans = 0;
    if (x < INT32_MIN || x > INT32_MAX)
    {
        return 0;
    };

    while (x != 0)
    {
        ans = x % 10 + ans * 10; // modulo x gives us last digit, *10 pushes digits one higher
        x = x / 10;              // /10 needed to 'delete' last digit
    };
    return ans;
};

int main()
{
    int num = -123;
    cout << "Result is " << reverse(num) << endl;
}