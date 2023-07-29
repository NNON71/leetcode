# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def linked_list_to_list(node):
        values = []
        while node:
            values.append(node.val)
            node = node.next
        return values
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        current = head
        while list1  and list2 :
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current = list2
                list2 = list2.next
            current = current.next
        current = list1 or list2
        return head.next
    
s = Solution()
node1 = ListNode()
node1.val = 1
node2 = ListNode()
node2.val = 2
node3 = ListNode()
node3.val = 3
node4 = ListNode()
node4.val = 1
node5 = ListNode()
node5.val = 3
node6 = ListNode()
node6.val = 4
node1.next = node2
node2.next = node3
node4.next = node5
node5.next = node6
print(s.mergeTwoLists(list1 = node1, list2 = node4))