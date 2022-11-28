#include <iostream>

using namespace std;

class ListNode
{
public:
    int val;
    ListNode *next;

    ListNode(int value)
    {
        val = value;
    };

    ListNode(int value, ListNode *next)
    {
        val = value;
        next = next;
    };
};

void printList(ListNode *head)
{
    while (head != NULL)
    {
        cout << head->val;
        head = head->next;
    };
};

ListNode *solution(ListNode *l1, ListNode *l2)
{
    ListNode *dummy = new ListNode(0);
    ListNode *current = dummy; // for keeping track of current node
    int carry = 0;             // in case we need to carry elements

    while (l1 != NULL || l2 != NULL || carry == 1)
    {
        int sum = 0; // keep track of sum in current nodes
        if (l1 != NULL)
        {
            sum += l1->val; // add value of l1 to sum
            l1 = l1->next;  // Go to next element in l1
        };
        if (l2 != NULL)
        {
            sum += l2->val;
            l2 = l2->next;
        }
        sum += carry;                            // add carried value from previous iteration
        carry = sum / 10;                        // if sum is higher than 10, we carry it over to next digit, rounded as carry is int
        ListNode *node = new ListNode(sum % 10); // create new node with modulo to get last digit
        current->next = node;                    // link new node to current node
        current = current->next;                 // Jump to newly created node and start again
    };
    return dummy->next; // return Next pointer from Dummy
}

int main()
{
    // Create l1
    ListNode *l1 = new ListNode(2);
    ListNode *l12 = new ListNode(4);
    ListNode *l13 = new ListNode(3);
    l1->next = l12;
    l12->next = l13;
    l13->next = NULL;

    // Create l2
    ListNode *l2 = new ListNode(5);
    ListNode *l22 = new ListNode(6);
    ListNode *l23 = new ListNode(4);
    l2->next = l22;
    l22->next = l23;
    l23->next = NULL;

    ListNode *res = solution(l1, l2);
    printList(res);
}