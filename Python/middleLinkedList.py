class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def printList(head):
    while head is not None:
        print(head.val)
        head = head.next


def constructLL(array):
    header = ListNode(array[0], None)
    temp = header
    for i, value in enumerate(array):
        if i < len(array) - 1:
            temp.val = value
            temp.next = ListNode(-1, None)
            temp = temp.next
        else:
            temp.val = value
            temp.next = None
    return header


def middleNode(head):
    ### Using the slow-fast double pointer approach
    slow = head
    fast = head

    counter = 0  ## count number of visited nodes
    while fast is not None:
        fast = fast.next
        counter += 1
        if counter % 2 == 0:  ## every second iteration move slow pointer
            slow = slow.next

    return slow


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6]
    header = constructLL(array)
    solution = middleNode(header)
    print(solution.val)
