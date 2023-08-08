# class Solution:
#     def twoSum(self, nums, target):
#         d = {}
#         for i,j in enumerate(nums):
#             r = target - j
#             if r in d: return [d[r], i]
#             d[j] = i


# sl = Solution()
# a = sl.twoSum([5,4,3,6],10)
# [print(a)]

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for char in s:
#             if char == '(' or char == '{' or char == '[':
#                 stack.append(char)
#             else:
#                 if not stack:
#                     return False
#                 if char == ')' and stack[-1] == '(':
#                     stack.pop()
#                 elif char == '}' and stack[-1] == '{':
#                     stack.pop()
#                 elif char == ']' and stack[-1] == '[':
#                     stack.pop()
#                 else:
#                     return False
#         return not stack
# sl = Solution()
# print(sl.isValid("[]"))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current = head
        for val in sorted(list1 + list2):
            current.next = ListNode(val)
            current = current.next

        return head.next

sl = Solution()

a = sl.mergeTwoLists([5, 2, 3, 9, 7, 1], [6, 4, 7, 12])
print(a)
