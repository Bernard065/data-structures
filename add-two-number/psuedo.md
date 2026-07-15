### Algorithm

1. Initialize a dummy head node and a pionter `cur` to build the result list.

2. Initialize `carry = 0`

3. While either `l1` or `l2` exists or `carry` is nonzero:
Read x = l1.val if l1 else 0.
Read y = l2.val if l2 else 0.
Compute s = x + y + carry.
Append node with value s % 10 to result.
Update carry = s // 10.
Advance l1, l2 and cur as appropriate.

4. Return dummy.next