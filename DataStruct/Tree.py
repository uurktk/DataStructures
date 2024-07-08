class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)  # We created the node
        # Check if root exists, if it is not our node is root
        if self.root is None:
            self.root = newNode
            return True
        # Find the element which has no child
        tempNode = self.root
        while True:
            if newNode.value == tempNode.value:
                return False
            if newNode.value < tempNode.value:
                if tempNode.left is None:
                    tempNode.left = newNode
                    return True
                tempNode = tempNode.left
            else:
                if tempNode.right is None:
                    tempNode.right = newNode
                    return True
                tempNode = tempNode.right

    def contains(self, value):
        tempNode = self.root
        while tempNode:
            if value < tempNode.value:
                tempNode = tempNode.left
            elif value > tempNode.value:
                tempNode = tempNode.right
            if tempNode.value == value:
                return True
        return False

    def minOfNode(self, currentNode):
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode

    def BFS(self):
        currentNode = self.root
        queue = []
        values = []

        queue.append(currentNode)
        while len(queue)>0:
            currentNode = queue.pop(0)
            values.append(currentNode.value)

            if currentNode.left is not None:
                queue.append(currentNode.left)
            if currentNode.right is not None:
                queue.append(currentNode.right)

        return values

    def DFSPreOrder(self):
        # Root to Leaf
        values = []
        def traverse(currentNode):
            values.append(currentNode.value)
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
        traverse(self.root)
        return values

    def DFSPostOrder(self):
        # Leaf to Root
        values = []
        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            if currentNode.right is not None:
                traverse(currentNode.right)
            values.append(currentNode.value)
        traverse(self.root)
        return values

    def DFSInOrder(self):
        # Root is in the middle, right nodes on the right side , left ones on the left side
        values = []
        def traverse(currentNode):
            if currentNode.left is not None:
                traverse(currentNode.left)
            values.append(currentNode.value)
            if currentNode.right is not None:
                traverse(currentNode.right)
        traverse(self.root)
        return values
