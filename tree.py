''' 
#Notes
Trees have branches and leaves and a parent node
A tree is a recursive data type.
'''

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self,child):
        child = TreeNode(child)
        child.parent = self
        self.children.append(child)
        return child
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level
    
    def print_tree(self,indent=None):
        prefix = '  '*self.get_level() +'|_ _' if self.parent else ''
        print(prefix+self.data)
        for child in self.children:
            child.print_tree()
            
  
        
def build_product_tree():
    root = TreeNode('Electronics')
    
    laptops = root.add_child('Laptop')
    laptops.add_child('HP')
    laptops.add_child('Mac')
    
    phones = root.add_child('Phones')
    phones.add_child('Samsung')
    phones.add_child('Iphone')
    phones.add_child('Motorola')
    
    root.print_tree()
        
if __name__ == '__main__':
    build_product_tree()