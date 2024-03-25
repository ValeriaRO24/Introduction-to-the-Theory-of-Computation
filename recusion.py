#Recusion Templates

#LINKED LISTS

#Traversing template:

curr = self._first
while curr is not None:

#while curr.next is not None(or curr.next.item not item): This will stop at the node before
#curr.next takes you to the very last node, curr takes you to the every end, past the
#last node
#curr_index = 0
#while curr is not None and curr_index < index -1 -> This is if you want to mutate with index
#(If you just want to find or replace item at index etc, then remove the -1 to get to the exact index)
    ... curr.item ...
    curr = curr.next

"""
TEST CASES
>>> lst = LinkedList([1, 2])

>>> lst = LinkedList([1, 2, 3, 4, 5])

>>> lst = LinkedList([1, 2, 1, 3, 2, 1])


"""

"""
You have to start at the first node on the list, and from then on traverse
across the whole linked list changing the current node to the next, and that's how you
access all the items in the list. If you want to mutate you have to make sure
there's no hole left by connecting links of next node to previous node.

Big Oh: It quicker to check front and mutate front of list than mutate the end. because you have to
traverse the whole thing. For normal lists the end if quicker and the front takes the most because
have to shift everything. 

"""


#RECUSION NESTED LISTS

#Template:

 if isinstance(obj, int):
         ...
     else:
         for sublist in obj:
        #Or for index in range(len(obj)): for index
             ... function(sublist) ...

"""
TEST CASES
>>> depth(12)

>>> depth([1, -2, [-10, 2, [3], [6], 4, -5], 4])

>>> depth([1, -2, [-10, 2, [3], [2, [45, 45]], 4, -5], 4])


"""

"""
For nested lists you have to think of them as going through the list and plan what should happen first,
what should be checked first and what should be checked if it's actually a list, what should happen
as you move through it. Dont think of it as recusion, but as just going through the list. And how
for the function every sublist must be checked the same way.
How should it act when its a number and how should it act when its a list, and what value should be output
when you hit each, (for example should you add up all the results? or compare them to the main list)

Big Oh: This usually depends on the size of the nested list, and how many values are in it all togehter
because usually it'll have to check all of them


"""


#RECUSION TREE

#Template

def f(self) -> ...:
    if self.is_empty():
        ...
    elif self._subtrees == []:
        ...
        
    else:
        ...
        for subtree in self._subtrees:
            ... subtree.f() ...
        ...

"""
TEST CASES
>>> Tree(None, [])

t = Tree(13, [Tree(2, []), Tree(6, [])])

>>> lt = Tree(2, [Tree(4, []), Tree(5, [])])
>>> rt = Tree(3, [Tree(6, []), Tree(7, []), Tree(8, [Tree(7, []), Tree(7, [])]), Tree(9, []),\
                          Tree(10, [])])
>>> t = Tree(1, [lt, rt])

"""

"""
Tree is a little stranger, but you have to be able to picture how it's basically a nested list mix with
a linked list, with only one value per list. Every node has a root and everything is connected to
the main tree root. Think of it as one tree, and the method you have to do to every subtree. form a plan
using a single tree first.
Leaves have subtrees as []

Big Oh: Usually depends on the sum of all nodes in a tree because usually you're checking every single
one. Even for methods like find height, you need to check all of them to compare greatest height. 

"""


#RECUSION BINARY SEARCH TREES

#Template
#THis method takes all nodes from BST and adds it to a list

        if self.is_empty():
            return []
        else:
            return self._left.items() + [self._root] + self._right.items()

#This one counts how many of item there are in Binary tree
        if self.is_empty():
            return 0
        else:
            count = 0
            if self._root == item:
                count += 1
            return self._left.count(item) + self._right.count(item) + count

#Searching, depending on which side of the root, left or right
if self.is_empty():
            return False
        else:
            if item == self._root:
                return True
            elif item < self._root:
                return item in self._left   # or, self._left.__contains__(item)
            else:
                return item in self._right  # or, self._right.__contains__(item)

#template  
    if self.is_empty():
            ...
        else:
            ... self._root ...
            ... self._left.my_bst_method() ...
            ... self._right.my_bst_method() ...

#template 2 USE THESE ANY TIME YOU NEED TO COMPARE ITEM
                def my_bst_method(self, item: Any) -> ...:
        if self.is_empty():
            ...
        elif item == self._root:
            ...
        elif item < self._root:
            ...
        else:  # item > self._root
            ...

"""
TEST CASES

>>> BinarySearchTree(None)

>>> bst = BinarySearchTree(24)

>>> bst = BinarySearchTree(7)
>>> left = BinarySearchTree(3)
>>> left._left = BinarySearchTree(2)
>>> left._right = BinarySearchTree(None)
>>> right = BinarySearchTree(11)
>>> right._left = BinarySearchTree(None)
>>> right._right = BinarySearchTree(13)
>>> bst._left = left
>>> bst._right = right



"""


"""
BST is a type of tree that only has two subtrees per node, a right and a left. The nodes aren't
sublists anymore so you have to traverse them differently. The methods on the top are two examples of
gathering the information from bianry trees

Big Oh: Usually, in an ideal world they would take O(h) which is the running time depending on the
height. For the most part it's not the whole size of the tree, only half. Which makes that the height.

"""

