from collections import deque
class RedBlackTree:
    class _Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.color = True
        def leftRed(self):
            if self.left:
                return self.left.color
            return False
        def rightRed(self):
            if self.right:
                return self.right.color
            return False
        def leftleftRed(self):
            if self.left and self.left.left:
                return self.left.left.color
            return False
        def rotateLeft(self):
            x = self.right
            self.right = x.left
            x.left = self
            x.color = self.color
            self.color = True
            return x
        def rotateRight(self):
            x = self.left
            self.left = x.right
            x.right = self
            x.color = self.color
            self.color = True
            return x
        def flip(self):
            self.color = not self.color
            self.left.color = not self.left.color
            self.right.color = not self.right.color
        def __repr__(self):
            return "({},{},{})".format(self.key, self.left if self.left else "None", self.right if self.right else "None")
    def __init__(self):
        self.root = None
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
        self.root.color = False
    def _insert(self, node, key, value):
        if not node:
            return RedBlackTree._Node(key, value)
        if node.leftRed() and node.rightRed():
            node.flip()            
        node.key = value if key == node.key else node.key
        node.left = self._insert(node.left, key, value) if key < node.key else node.left
        node.right = self._insert(node.right, key, value) if key > node.key else node.right
        node = node.rotateLeft()  if node.leftRed() and node.rightRed() else node
        node = node.rotateRight() if node.leftRed() and node.leftleftRed() else node
        return node
    def get(self, key):
        cur = self.root
        while cur and cur.key != key:
            cur = cur.left if cur.key > key else cur.right
        return None if not cur else cur.key
    def __repr__(self):
        return "(None)" if not self.root else str(self.root)

t = RedBlackTree()
t.insert(5, 2)
t.insert(4, 2)
t.insert(3, 2)
t.insert(1, 2)
print(t)