from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0

            s = x + y + carry

            carry = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy.next


def make_list(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out

sol = Solution()

tests = [
    ([2,4,3], [5,6,4], [7,0,8]),      # 342 + 465 = 807
    ([0], [0], [0]),
    ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1]),  # carry chain test
]

for l1_vals, l2_vals, expected in tests:
    l1 = make_list(l1_vals)
    l2 = make_list(l2_vals)
    result = to_list(sol.addTwoNumbers(l1, l2))
    status = "PASS" if result == expected else "FAIL"
    print(f"{status}: {l1_vals} + {l2_vals} -> {result} (expected {expected})")