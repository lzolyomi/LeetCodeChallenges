#include <iostream>
#include <stack>
#include <cmath>
using namespace std;

class ListNode
{
public:
    int val;
    ListNode *next;
    // constructors
    ListNode()
    {
        val = 0;
        next = nullptr;
    };
    ListNode(int x)
    {
        val = x;
        next = nullptr;
    };
    ListNode(int x, ListNode *Next)
    {
        val = x;
        next = Next;
    };
};

bool isPalindrome(ListNode *head)
{
    if (head->next == NULL || head == NULL)
    {
        return true;
    };
    stack<int> s;
    int length = 0;
    ListNode *temp = head;
    // get length of list in linear time
    while (head != NULL)
    {
        length++;
        head = head->next;
    };
    int middle = ceil(length / 2);
    cout << "Middle length of list: " << middle << "Total length: " << length << endl;
    if (length % 2 == 0)
    {
        int counter = 0;
        while (counter < middle)
        {
            s.push(temp->val);
            temp = temp->next;
            counter++;
        };
        while (temp != NULL)
        {
            int stackVal = s.top();
            s.pop();
            if (stackVal != temp->val)
            {
                return false;
            }
            temp = temp->next;
        };
        return true;
    }
    else
    { // if odd length, skip middle element
        int counter = 0;
        while (counter < middle)
        {
            s.push(temp->val);
            temp = temp->next;
            counter++;
        };
        temp = temp->next; // jump to next one
        while (temp != NULL)
        {
            int stackVal = s.top();
            s.pop();
            if (stackVal != temp->val)
            {
                return false;
            }
            temp = temp->next;
        };
        return true;
    }
};

int main()
{
    ListNode *head = new ListNode(1);
    ListNode *l1 = new ListNode(0);
    ListNode *l2 = new ListNode(1);
    // ListNode *l3 = new ListNode(1);
    head->next = l1;
    l1->next = l2;
    l2->next = NULL;
    // l3->next = NULL;

    if (isPalindrome(head))
    {
        cout << "It is a palindrome";
    }
    else
    {
        cout << "It is NOT palindrome";
    }
}