# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.# 
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        if self.next:
            return str(self.val) + str(self.next)
        else:
            return str(self.val)


class Solution:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def list_to_int_step(l: Optional[ListNode], work_str:str) -> int:
            if l is None:
                return work_str[::-1]
            else:
                lit = str(l.val)
                work_str += lit
                return list_to_int_step(l.next, work_str)
        
        def list_to_int(l: Optional[ListNode]) -> int:
            int_str = list_to_int_step(l, "")
            return int(int_str)
        
        def str_to_list_step(s:str, initial_node: Optional[ListNode], last_node: Optional[ListNode]) -> Optional[ListNode]:
            if s == "":
                return initial_node
            else:
                lit = s[0]
                new_node = ListNode(int(lit), None)
                last_node.next = new_node
                return str_to_list_step(s[1:], initial_node, new_node)
        
        
        int_1 = list_to_int(l1)
        int_2 = list_to_int(l2)
        result_int = int_1 + int_2
        result_str = str(result_int)[::-1]
        initial_node = ListNode(result_str[0], None)
        result = str_to_list_step(result_str[1:], initial_node, initial_node)
        return result
    

if __name__=='__main__':
    l1 = ListNode(1,ListNode(2,ListNode(3,None)))
    l2 = ListNode(4,ListNode(5,None))
    s = Solution.addTwoNumbers(l1,l2)
    print(str(l1)[::-1])
    print(str(l2)[::-1])
    print(str(s)[::-1])        