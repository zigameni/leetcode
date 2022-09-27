# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        rList = head
        listHead = head
        prev = head
        if(head == None):
            listHead = None
            return listHead

        first = True        
        cnt = 0
        while(head.next):
           
            if head.val != val:
                # array.append(head.val)
                if (first):
                    rList.val = head.val
                    rList = rList.next
                    cnt = cnt + 1
                    first = False
                else: 
                    rList.val = head.val
                    prev = rList
                    rList = rList.next
                    cnt = cnt + 1
                
            head = head.next
        
        if(head.val != val):
            rList.val = head.val
            rList.next = None
            cnt = cnt + 1 
        else:
            prev.next = None
        
        if(cnt==0):
            listHead = None
            
        return listHead