#Class to hold data
class Node:
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent
        self.level = 0
        self.x = 0
        self.y = 0
        self.left = None
        self.right = None
        self.painted_object_oval = None
        self.painted_object_string = None
        self.painted_object_line = None
        


#Class to hold all the nodes
class BST:

    def __init__(self):
        self.root = None

    #Find the deepest node level
    def search_deepest_level(self, node):
        if node == None:
            return 0
        if node != None:
            level = node.level
            x = self.search_deepest_level(node.left)
            y = self.search_deepest_level(node.right)
            if x > level:
                level = x
            if y > level:
                level = y
            return level
            
        

    #Search through the tree of nodes
    def search_node(self, node, key):
        if node == None or key == node.key:
            return node
        if key < node.key:
            return self.search_node(node.left, key)
        else:
            return self.search_node(node.right, key)

    #Go right as far as you can
    def find_max(self, node):
        while node.right != None:
            node = node.right
        return node
    #Go left as far as you can
    def find_min(self, node):
        while node.left != None:
            node = node.left
        return node

    #Find the successor of the given node
    def successor(self, node):
        if node.right != None:
            return self.find_min(node.right)
        else:
            parent = node.parent
            while parent != None and node == parent.right:
                node = parent
                parent = parent.parent
            return parent
        
    #Find the predecessor of the given node
    def predecessor(self, node):
        if node.left != None:
            return self.find_max(node.left)
        else:
            parent = node.parent
            while parent != None and node == parent.left:
                node = parent
                parent = parent.parent
            return parent

    #Traverse the tree preorder
    def preorder_node(self, node):
        if node != None:
            node_list = [node]
            if node.left != None:
                node_list += self.preorder_node(node.left)
            if node.right != None:
                node_list += self.preorder_node(node.right)
            return node_list

    #Traverse the tree inorder
    def inorder_node(self, node):
        if node != None:
            node_list = []
            if node.left != None:
                node_list += self.inorder_node(node.left)
            node_list += [node]
            if node.right != None:
                node_list += self.inorder_node(node.right)
            return node_list

    #Traverse the tree postorder
    def postorder_node(self, node):
        if node != None:
            node_list = []
            if node.left != None:
                node_list += self.postorder_node(node.left)
            if node.right != None:
                node_list += self.postorder_node(node.right)
            node_list += [node]
            return node_list
        
    #Function to delete every node in the tree postorder
    def postorder_delete(self, node):
        if node != None:
            self.postorder_delete(node.left)
            self.postorder_delete(node.right)
            self.delete_node(node, node.key)

    #When a node is deleted, bring all it's descendants up with it's replacement
    def propogate_down_level_changes(self, node):
        if node != None:
            self.propogate_down_level_changes(node.left)
            self.propogate_down_level_changes(node.right)
            node.level -= 1
    
    #Search through the tree of nodes, and if the node is found, delete it,
    #reorganising the tree as necessary.
    def delete_node(self, node, key):
        if node == None:
            return node
        elif key < node.key:
            node.left = self.delete_node(node.left, key)
        elif key > node.key:
            node.right = self.delete_node(node.right, key)
        else:
            #Node is a leaf node
            if node.left == None and node.right == None:
                if node == self.root:
                    self.root = None
                node = None
            #Node has one child
            elif node.left == None:
                self.propogate_down_level_changes(node.right)
                if node == self.root:
                    node.right.x = node.x
                    self.root = node.right
                temp = node
                node = node.right
                node.y = temp.y
                node.parent = temp.parent
            elif node.right == None:
                self.propogate_down_level_changes(node.left)
                if node == self.root:
                    node.left.x = node.x
                    self.root = node.left
                temp = node
                node = node.left
                node.y = temp.y
                node.parent = temp.parent
            #Node has two children
            else:
                temp = self.find_min(node.right)
                intermediate = node.key
                node.key = temp.key
                temp.key = intermediate
                node.right = self.delete_node(node.right, key)
        return node

    #Call the search_node function on the root node
    def search(self, key):
        return self.search_node(self.root, key)
        

    #Call the delete_node function on the root node
    def delete(self, key):
        return self.delete_node(self.root, key)

    #Insert a node in the appropriate position
    def insert(self, key):
        node = Node(key, None)
        parent = None
        root = self.root

        while root != None:
            parent = root
            if node.key < root.key:
                root = root.left
            else:
                root = root.right
        node.parent = parent
        if parent == None:
            self.root = node
            node.level = 0
            node.x = 1
        elif node.key < parent.key:
            parent.left = node
            node.level = parent.level + 1
            node.x = parent.x * 1.5
        else:
            parent.right = node
            node.level = parent.level + 1
            node.x = parent.x * 1.5
        return node

    #Call the preorder_node function on the root node
    def preorder(self):
        return self.preorder_node(self.root)

    #Call the inorder_node function on the root node
    def inorder(self):
        return self.inorder_node(self.root)

    #Call the postorder_node function on the root node
    def postorder(self):
        return self.postorder_node(self.root)
    
            
        
    
        
