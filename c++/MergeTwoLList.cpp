#include <iostream>

using namespace std;

// Boilerplate code for Linked Lists
class ListNode
{
public:
    ListNode *next;
    int val;
    // Constructor with pointer AND value
    ListNode(ListNode *Next, int Val)
    {
        next = Next;
        val = Val;
    };
    // Constructor with value only, next pointer empty
    ListNode(int Val)
    {
        val = Val;
    }
};

void printLList(ListNode *head)
{
    while (head != NULL)
    {
        cout << head->val << " -> ";
        head = head->next;
    };
};

// Actual function
ListNode *MergeTwoLists(ListNode *list1, ListNode *list2)
{
    ListNode *dummy = new ListNode(-1); // Dummy node to start the sorted list, will return its 'next' pointer
    ListNode *lastElem;                 // store the last element of the merged array
    lastElem = dummy;
    while (list1 != NULL && list2 != NULL) // until haven't reached end of at least one list
    {
        if (list1->val < list2->val)
        {                           // if list1's next element is lower than list2's
            lastElem->next = list1; // last element of merged array points to list1
            lastElem = list1;       // update new last element
            list1 = list1->next;    // move to next element in list1
        }
        else
        {
            lastElem->next = list2; // last element of merged array points to list2
            lastElem = list2;       // update new last element
            list2 = list2->next;    // move to next element in list2
        };
    }
    // check if either list has remaining elements
    if (list1 != NULL) // list1 still has elements
    {
        while (list1 != NULL) // get to end of the lsit
        {
            lastElem->next = list1;
            lastElem = list1;
            list1 = list1->next;
        }
    }
    else if (list2 != NULL) // list2 still has elements
    {
        while (list2 != NULL) // get to end of list
        {
            lastElem->next = list2;
            lastElem = list2;
            list2 = list2->next;
        }
    };

    return dummy->next;
}

int main()
{
    // Construct first list
    ListNode *head1 = new ListNode(1);
    ListNode *l12 = new ListNode(2);
    ListNode *l13 = new ListNode(4);
    // Create links
    head1->next = l12;
    l12->next = l13;
    l13->next = NULL; // end of list
                      // Construct second list
    ListNode *head2 = new ListNode(1);
    ListNode *l22 = new ListNode(3);
    ListNode *l23 = new ListNode(4);
    // Create links
    head2->next = l22;
    l22->next = l23;
    l23->next = NULL; // end of list
    // Merge two lists
    ListNode *result = MergeTwoLists(head1, head2);
    printLList(result);
}
