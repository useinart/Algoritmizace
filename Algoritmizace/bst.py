class Node:
    def __init__(self,value=None):
        self.left = None
        self.right = None
        self.data = value

class BinarySearchTree:
    def __init__(self):
        self.root= None

    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,curNode):
        if value < curNode.data:
            if curNode.left ==  None:
                curNode.left = Node(value)
            else:
                self._insert(value, curNode.left)
        elif value > curNode.data:
            if curNode.right == None:
                curNode.right = Node(value)
            else:
                self._insert(value,curNode.right)


    def fromArray(self,array):
        for i in range(len(array)):
            if self.root == None:
                self.root = Node(array[i])
            else:
                self._insert(array[i],self.root)


    def search(self,value):
        if self.root != None:
            self.visited = 0
            return self._search(value,self.root)
        else:
            return False

    def _search(self,value,cur_node):
        if value == cur_node.data:
            self.visited += 1
            return True
        elif value < cur_node.data and cur_node.left != None:
            self.visited += 1
            return self._search(value,cur_node.left)
        elif value > cur_node.data and cur_node.right != None:
            self.visited += 1
            return self._search(value,cur_node.right)
        self.visited += 1
        return False


    def min(self):
        self.visited = 0
        if self.root == None:
            return None
        current = self.root
        if current.left == None:
            self.visited += 1
        while current.left != None:
            self.visited += 1
            current = current.left
        self.visited += 1
        return current.data


    def max(self):
        self.visited = 0
        if self.root == None:
            return None
        current = self.root
        while current.right != None:
            self.visited += 1
            current = current.right
        self.visited += 1
        return current.data


    def visitedNodes(self):
        return self.visited

'''
tree = BinarySearchTree()
array = [9932, 258, 9771, 72, 1648, 4622, -1391, 6609, -4289, -114, 6783, 6983, -8520, 3982, -9605, 1422, -8302, 9575, -3412, 1742]
tree.fromArray(array)
#tree.print_tree()
print(tree.search(10))
print(tree.visitedNodes())
print(tree.search(7))
print(tree.visitedNodes())
print(tree.search(3))
print(tree.visitedNodes())
print(tree.search(-99999999))
print(tree.visitedNodes())
print(tree.min())
print(tree.visitedNodes())
print(tree.max())
print(tree.visitedNodes())'''

