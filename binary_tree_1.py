# search complexity = log2n
# insert complexity = log2n
# binary search tree does not have duplicate elements
''' traversal techniques in binary tree
    - breadth first search
    - depth first search
        -in order traversal
        - pre order traversal
        - post order traversal
'''

class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        if data < self.data:
            # add data to left sub tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)


        if data > self.data:
            # add data to right sub tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements+=self.left.in_order_traversal()
        if self.right:
            elements+=self.right.in_order_traversal()
        elements.append(self.data)
        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements+=self.left.in_order_traversal()
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data


    def calculate_sum(self):
        return sum(self.in_order_traversal())

    def search(self,val):
        if self.data == val:
            return True
        if val < self.data:
            # check left sub tree
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            # check right sub tree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def delete(self,val):
        if val < self.data and self.left:
            self.left.delete(val)
        if val > self.data and self.right:
            self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None

                


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,180,34]
    tree = build_tree(numbers)
    print(tree.search(200))
    print(tree.post_order_traversal())
    print(tree.find_max())
    print(tree.find_min())
    print(tree.calculate_sum())

# bound method BinarySearchTreeNode.find_min of <__main__.BinarySearchTreeNode object at 0x0000025931CD4E20>>