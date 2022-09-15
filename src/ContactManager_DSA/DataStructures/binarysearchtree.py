from src.ContactManager_DSA import utils


class BSTNode:
    """
    # Description:
        # A binary search tree node                                                                                   #
    """

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def compare_to(self, other):
        return utils.comparator(self, other)


class BST:
    """
    # Description:
        * A binary search tree node, this will be used for storing contacts as apposed to the sorted list.
        * A BST has a better performance(linear vs logarithmic), although it takes more space.
        * This implementation of a binary tree is known as an inverted tree i.e., root to leaf.                                                           *
    """

    def __init__(self, root=None):
        self.root = root
        self.count = 0

    def __iter__(self):
        return  self

    def __next__(self):
        items = []
        return self.inorder_traversal()

    def add(self, value):
        if not self.root:
            self.root = BSTNode(value)
        else:
            self.add_to(self.root, value)
        self.count = self.count + 1

    def add_to(self, node, value):
        if value.compare_to(node.data) < 0:
            if not node.left:
                node.left = BSTNode(value)
            else:
                self.add_to(node.left, value)

        else:
            if not node.right:
                node.right = BSTNode(value)
            else:
                self.add_to(node.right, value)

    def remove(self, value):
        current = BSTNode(None)
        parent = BSTNode(None)

        current, parent = self.find_with_parent(value)
        if not current:
            return False
        self.count = self.count - 1

        if not current.right:
            if not parent:
                self.root = current.left
            else:
                result = parent.compare_to(current.value)
                if result > 0:
                    parent.left = current.left
                elif result < 0:
                    parent.right = current.left
        elif not current.right.left:
            current.right.left = current.left

            if not parent:
                self.root = current.right
            else:
                result = parent.compare_to(current.value)
                if result > 0:
                    parent.left = current.right
                elif result < 0:
                    parent.right = current.right
        else:
            leftmost = current.right.left
            leftmostparent = current.right

            while leftmost.left:
                leftmostparent = leftmost
                leftmost = leftmost.left

            leftmostparent.left = leftmost.right

            leftmost.left = current.left
            leftmost.right = current.right

            if not parent:
                self.root = leftmost
            else:
                result = parent.compare_to(current.value)
                if result > 0:
                    parent.Left = leftmost
                elif result < 0:
                    parent.Right = leftmost

        return True

    def find_with_parent(self, value):
        current = self.root
        parent = None

        while current:
            result = int(current.compare_to(value))

            if result > 0:
                parent = current
                current = current.left
            elif result < 0:
                parent = current;
                current = current.right
            else:
                break
        return current, parent

    # Traversals
    # Traversal - For identical copying - Preorder
    def preorder_traversal(self, action):
        self.preorder_traversal_main(action, self.root)

    def preorder_traversal_main(self, action, node):
        if node:
            action(node.data)
            self.preorder_traversal(action, node.left)
            self.preorder_traversal(action, node.right)

    # Traversal - For Sorting - Inorder
    def inorder_traversal(self, action):
        self.inorder_traversal_helper(action, self.root)

    def inorder_traversal_helper(self, action, node):
        if node:
            action(node.data)
            self.inorder_traversal(action, node.left)
            self.inorder_traversal(action, node.right)

    # Traversal - For Deleting in Place - Postorder
    def postorder_traversal(self, action):
        self.postorder_traversal(action, self.root)

    def postorder_traversal_helper(self, action, node):
        if node:
            action(node.data)
            self.preorder_traversal(action, node.left)
            self.preorder_traversal(action, node.right)
