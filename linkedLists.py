from __future__ import print_function

class Node:
  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    return str(self.val)

def display(lst):
    """ Print LinkedList value by value """
    if lst:
        print(str(lst.val), end='')
        if lst.next is not None:
            print(", ", end='')
        display(lst.next)

    else:
        print('')

def insert(val, lst):
    """ Insert value into LinkedList """
    if lst is None:
        return
    runner = lst.next
    prev = lst
    while runner is not None:
        runner = runner.next
        prev = prev.next
    runner = Node(val)
    prev.next = runner

def remove(val, lst):
    """ Remove value from LinkedList """
    if lst.val == val:
        lst = lst.next

    runner = lst.next
    prev = lst

    while runner is not None:
        if runner.val == val:
            prev.next = runner.next
            return
        else:
            runner = runner.next
            prev = prev.next

def reverse(lst):
    """ Reverses LinkedList """
    prev = None
    cur = lst

    while (cur is not None):
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    lst = prev
    return lst

def is_palindrome_permutation(lst):
    hm = {}
    cur = lst

    while cur is not None:
        if not cur.val in hm:
            hm[cur.val] = 1
        else:
            hm[cur.val] += 1
        cur = cur.next

    foundOdd = False

    for key in hm.keys():
        print(key)
        if hm[key] % 2 == 1:
            print("Encountered odd count")
            if foundOdd:
                return False
            else:
                foundOdd = True
    return True


def remove_duplicates(lst):
    """ Removes duplicates from LinkedList """
    dct = {}
    cur = lst
    prev = None

    while cur is not None:
        value = cur.val
        if value in dct:
            prev.next = cur.next
        else:
            dct[value] = True
        prev = cur
        cur = cur.next
    return lst

def partition(lst, val):
    """ Partition LinkedList around value val """
    before = None
    after = None

    cur = lst

    while cur is not None:
        if cur.val < val:
            if before is None:
                before = Node(cur.val)
            else:
                insert(cur.val, before)
        else:
            if after is None:
                after = Node(cur.val)
            else:
                insert(cur.val, after)
        cur = cur.next

    iterator = before
    while iterator.next is not None:
        iterator = iterator.next
    iterator.next = Node('X', after)

    return before

def remove_middle_node(node):
    """ Remove middle node without need of head of LinkedList """
    if node.next == None:
        node = None
    else:
        node.val = node.next.val
        node.next = node.next.next

def add_reversed_nums_improved(num1, num2, carry):
    """ Not working cause types are broken """
    if num1 is None and num2 is None and carry is 0:
        return
    res = Node()
    value = carry


    if num1 is not None:
        value += num1.val
    if num2 is not None:
        value += num2.val

    if value >= 10:
        value -=10
        carry = 1
    else:
        carry = 0
    res.val = value
    v1 = None if not num1 else num1.val
    v2 = None if not num2 else num2.val
    res.next = add_reversed_nums_improved(v1, v2, carry)

def add_reversed_nums(num1, num2, carry):
    """
    Add two numbers stored in linkedLists as follows:
        num1 = 145 -> [5, 4, 1]
    """
    result = Node()

    if not num1:
        if not num2:
            if carry is 1:
                return Node(carry)
            else:
                return
        else:
            result = Node()
            result.val = num2.val + carry
            if result.val >= 10:
                result.val -= 10
                carry = 1
            else:
                carry = 0
            result.next = add_reversed_nums(None, num2.next, carry)
    else:
        if not num2:
            result = Node(0)
            result.val = num1.val + carry
            if result.val >= 10:
                result.val -= 10
                carry = 1
            else:
                carry = 0
            result.next = add_reversed_nums(num1.next, None, carry)
        else:
            result.val = carry + num1.val + num2.val
            if result.val >= 10:
                result.val -= 10
                carry = 1
            else:
                carry = 0
        result.next = add_reversed_nums(num1.next, num2.next, carry)
    return result

""" Build a linkedList for testing """
head2 = Node(0)
for x in range(1, 10):
    insert(x, head2)

#Untouched LinkedList
display(head2)

num1 = Node(3)
insert(2, num1)
insert(1, num1)

num2 = Node(1)
insert(2, num2)
insert(9, num2)
insert(1, num2)

palindrome_permutation = Node('a')
insert('b', palindrome_permutation)
insert('a', palindrome_permutation)

display(num1)
display(num2)

res = add_reversed_nums(num1, num2, 0)
display(res)
print("------------------------------")

display(partition(head2, 5))

print("------------------------------")
#Remove dupes from LinkedList
print("------------------------------")

print(is_palindrome_permutation(palindrome_permutation))
