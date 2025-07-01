class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
            
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        l,r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
