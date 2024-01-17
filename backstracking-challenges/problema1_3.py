""" Provide the code for the TREAP-INSERT procedure in a language of your choice, attaching an editable file. 
Hint: perform the standard Binary Search Tree (BST) insertion and then perform rotations to restore the min-heap
property (min-heap order). """

import numpy as np

TOP_PRIORITY = 1
BOTTOM_PRIORITY = 500

NIL = None

class Node:
    def __init__(self, key):
        self.key = key
        self.priority = np.random.randint(low = TOP_PRIORITY, high = BOTTOM_PRIORITY)
        self.right = NIL
        self.left = NIL
        self.father = NIL

class Treap:
    def __init__(self):
        self.root = NIL

    def min_heap_order(self, node):
        if node.father != NIL:
            topper = node.father
            if node.priority < topper.priority:
                min = node
                
                if node.key < topper.key:
                    node.left = topper
                    node.right = topper.right
                    node.father = topper.father
                else:
                    node.right = topper
                    node.left = topper.left
                    node.father = topper.father
                           
                if min != self.root:
                    self.min_heap_order(min)
            


    def treap_insert(self, node):
        router = self.root              # instradatore
        follower = NIL                  # puntatore inseguitore
        while(router != NIL):
            follower = router           
            if node.key < router.key:
                router = router.left
            else: router = router.right
        
        node.father = follower

        if follower == NIL:
            self.root = node
        elif node.key < follower.key:
            follower.left = node
            self.min_heap_order(node)
        else: 
            follower.right = node
            self.min_heap_order(node)
            

    def print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            if node.left or node.right:
                self.print_tree(node.left, level + 1, "L--- ")
                self.print_tree(node.right, level + 1, "R--- ")

treap = Treap()

for i in range(10):
    node = Node(i)
    treap.treap_insert(node)

treap.print_tree(treap.root)