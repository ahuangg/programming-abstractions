class Node():

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def __iter__(self):
        return self.inorder(self)

    def inorder(self, root):
        if root:
            for v in self.inorder(root.left):
                yield v

            yield root.val

            for v in self.inorder(root.right):
                yield v


class BinarySearchTree():

    def __init__(self, name, root):
        self.root = root
        self.name = name

    def insert(self, val, root):
        if root.val == None:
            root.val = val
        else:
            self._insert(val, root)

    def _insert(self, val, curr):
        if val < curr.val:
            if curr.left == None:
                curr.left = Node(val)
            else:
                self._insert(val, curr.left)
        else:
            if curr.right == None:
                curr.right = Node(val)
            else:
                self._insert(val, curr.right)

    def add_all(self, *tup):
        for v in tup:
            self.insert(v, self.root)


if __name__ == "__main__":
    t1 = BinarySearchTree(name="Oak", root=Node())
    t2 = BinarySearchTree(name="Birch", root=Node())
    t1.add_all(5, 3, 9, 0)
    t2.add_all(1, 0, 10, 2, 7)
    print(t1.name)
    for x in t1.root:
        print(x)
    print(t2.name)
    for x in t2.root:
        print(x)
