'''
    deleting a node in a binary tree!
    Three cases:
        - delete node entirely
        - remove node and shift its child(1) to its position
        - if node has both left and right children, move minimum in the tree of its right child to its position
            - then delete node
        - or find maximum in left node
'''