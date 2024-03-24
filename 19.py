# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
          
    
      
      
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = self.get_length(head)
        p,c,q,count = None,head,head.next,0
        if length == 2 and n == 1:
            c.next = None
            return head
        while(c.next):
            print('p',p,'q',q,'c',c,'length',length,'count',count)
            if count == length - n:
                p.next = q
                return head
            count += 1
            p = c
            c = c.next
            q = c.next
            print('p',p,'q',q,'c',c,'length',length,'count',count)
        return None
            
    def get_length(self,head):
        count = 0
        while head.next != None:
          count +=1
          head = head.next
        return count+1
        
        
        
        
        
					