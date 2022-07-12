from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        if isinstance(val, int):
            self.val = val
            self.next = next
        elif isinstance(val, list):
            self.val = val[0]
            self.next = None
            curr = self
            for i in val[1:]:
                curr.next = ListNode(i)
                curr = curr.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(None)
        curr = prev
        carry = 0
        if isinstance(l1, list):
            l1 = ListNode(l1)
            l2 = ListNode(l2)

        while(l1 or l2 or carry):
            
            sum = l1.val if(l1) else 0 + l2.val if(l2) else 0 + carry
            curr.val = sum % 10
            carry = sum / 10
            curr.next = ListNode(sum)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry != 0:
            curr.next = ListNode(carry)
        return prev


def test01():
    l1_01 = ListNode(1)
    l1_02 = ListNode(2)
    l1_03 = ListNode(3)
    l1_01.next = l1_02
    l1_02.next = l1_03
    l1 = [l1_01, l1_02, l1_03]

    l2_01 = ListNode(3)
    l2_02 = ListNode(4)
    l2_03 = ListNode(5)
    l2_01.next = l2_02
    l2_02.next = l2_03
    l2 = [l2_01, l2_02, l2_03]

    r01 = ListNode(4)
    r02 = ListNode(6)
    r03 = ListNode(8)
    r01.next = r02
    r02.next = r03
    r = [r01, r02, r03]

    actual = Solution.addTwoNumbers(None, [1,2,3], [3,4,5])
    assert ListNode([4,6,8]) == actual
