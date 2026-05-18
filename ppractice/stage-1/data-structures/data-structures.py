#1.LIST-ordered,mutable,allows duplicates
# fruits=(["mango","apple","papaya"])
# fruits.append("pumpkin")  #add
# fruits.remove("mango")   #remove
# print(fruits[1])         #index
# print(fruits)


#2.TUPLE-ordered,immutable,allows duplcates
# numbers=(10,20,30)
# print(numbers[1])


#3.SET-unordered,no duplicates ,mutable
# nums={1,2,3,4,5}
# nums.add(6)   #adding
# nums.discard(2)   #remove
# print(nums)


#4.DICTIONARY-key-vale paird,ordered(python 3,7+),mutable
# person={'name':'hemanth','city':'madanapalle'}
# person['age']=21 #add
# del person['name']   #delete
# print(person['age'])


#5.STRING-ordered,immutable sequence of characters
# s="hemanth"
# print(s.upper())  #uppercase
# print(s[:3])      #slicing
# print(s[1])


#6.STACK-LIFO
# stack=[]
# stack.append(10)  #add at first
# print(stack)
# stack.append(20)  #add at second
# print(stack)
# stack.pop()       #remove second at first
# print(stack)


#7.QUEUE-FIFO
# from collections import deque
# queue=deque()
# queue.append("a")  #enqueue
# queue.append("b")
# queue.popleft()    #pop a
# print(queue)


#8.LINKEDLIST-nodes connected via pointers
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# head=node(1)
# head.next=node(2)
# head.next.next=node(3)
# temp = head
# while temp:
#     print(temp.data)
#     temp = temp.next


#9.TREE-hierarchical structure with parent/child nodes
# class treenode:
#     def __init__(self,val):
#         self.val=val
#         self.left=None
#         self.right=None
# root=treenode(1)
# root.left=treenode(2)
# root.right=treenode(3)
# print(root.val)
# print(root.left.val)
# print(root.right.val)

#ANOTHER WAY FOR PRINTINNG
# def preorder(node):
#     if node:
#         print(node.val)
#         preorder(node.left)
#         preorder(node.right)
# preorder(root)


#10.HEAP-specialized tree;min-heap by default in python
# import heapq
# h=[5,1,3]
# heapq.heapify(h)    #tree like
# print(h)
# heapq.heappush(h,0)  #adding
# print(h)
# heapq.heappop(h)    #removing first number
# print(h)


#11.GRAPH-nodes connected by edges(using dict/adjacency list)
# graph={
#     "A":["B","C"],
#     "B":["A","C"],
#     "C":["A"],
#     "D":["B"]
# }
# print(graph["C"])