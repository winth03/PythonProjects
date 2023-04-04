class BinaryTree:
    def __init__(self, val=None) -> None:
        self._rootValue = val
        self._leftChild = None
        self._rightChild = None

    def getRootVal(self):
        return self._rootValue
    
    def getLeftChild(self):
        return self._leftChild
    
    def getRightChild(self):
        return self._rightChild

    def search(self, key):
        root = self.getRootVal()
        if root == key:
            return self
        elif self.getLeftChild() and root > key:
            return self.getLeftChild().search(key)
        elif self.getRightChild() and root < key:
            return self.getRightChild().search(key)
        return self
    
    def insert(self, key, val):
        pass

    def delete(self, key):
        pass

    def __str__(self) -> str:
        return f"  {self.getRootVal()}\n/ \\{self.getLeftChild()}{self.getRightChild()}\n"

tree = BinaryTree(3)
tree._leftChild = BinaryTree(2)
print(tree)