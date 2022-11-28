#include <iostream>

using namespace std;

class ListNode
{
public:
    ListNode *next;
    int val;

    // Constructors
    ListNode(int Val)
    {
        val = Val;
    };
    ListNode(int Val, ListNode *Next)
    {
        val = Val;
        next = Next;
    };
};

void printList(ListNode *node)
{
    while (node != NULL)
    {
        cout << node->val << " -> ";
        node = node->next;
    };
    cout << endl;
};

ListNode *solution(ListNode *head, int n)
{
    ListNode *fastPointer; // pointer with the head start
    ListNode *slowPointer; // Pointer starting after the headstart
    fastPointer = head;    // both will start at the beginning of the list
    slowPointer = head;
    // headStart for fast pointer
    for (int i = 0; i < n; i++)
    {
        fastPointer = fastPointer->next;
    };
    if (fastPointer == NULL)
    {
        return head->next; // in case the fast pointer is at NULL, we delete the first element
    }
    // Go with both pointers
    while (fastPointer->next != NULL)
    { // once this loop terminates, slowpointer will be at the element BEFORE we delete
        fastPointer = fastPointer->next;
        slowPointer = slowPointer->next;
    };
    slowPointer->next = slowPointer->next->next;
    return head;
};

int main()
{
    // Construct first list
    ListNode *head = new ListNode(1);
    ListNode *l2 = new ListNode(2);
    ListNode *l3 = new ListNode(3);
    ListNode *l4 = new ListNode(4);
    ListNode *l5 = new ListNode(5);
    // Create links
    head->next = l2;
    l2->next = l3;
    l3->next = l4;
    l4->next = l5;
    l5->next = NULL; // end of list
    // Second test list
    ListNode *head2 = new ListNode(1, NULL);
    ListNode *res = solution(head2, 1);
    printList(res);
};