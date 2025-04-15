class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find middle (slow will point to middle)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        while slow:
            next_temp = slow.next
            slow.next = prev
            prev = slow
            slow = next_temp

        # Step 3: Compare both halves
        left, right = head, prev
        while right:  # Only need to check the second half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
