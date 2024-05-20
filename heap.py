class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f"{self}"

    def __str__(self):
        return f"{self.data}"

class TreeBinaryBuilder:
    @staticmethod
    def build(sexpr):
        stack = []
        add = lambda node: node if node.data != "#" else None

        root = None
        for tok in sexpr:
            if tok != ")":
                stack.append(TreeNode(tok))
                continue
            root_ = None
            while stack[-1].data != "(":
                node = stack.pop()
                if root_ is None:
                    root_ = node
                    continue
                right, root_ = root_, TreeNode(None)
                root_.left_child, root_.right_child = add(node), add(right)
            stack.pop()

            if not stack:
                return root_

            assert root_
            root = stack.pop()
            root_.data = root.data
            stack.append(root_)

        return root

class TreeBst:

    def __init__(self, root = None):
        self.root = root

    def findPredessor(self, node):
        curr_ = node
        while curr_ and curr_.right_child is not None:
            curr_ = curr_.right_child
        return curr_

    def insert(self, data):

        def insert_recursive(root):
            if root is None:
                return TreeNode(data)
            if data < root.data:
                root.left_child = insert_recursive(root.left_child)
            elif data > root.data:
                root.right_child = insert_recursive(root.right_child)
            return root

        self.root = insert_recursive(self.root)

    def delete(self, data):

        def delete_recursive(root):
            if root is None:
                return root
            if data < root.data:
                root.left_child = delete_recursive(root.left_child)
            elif data > root.data:
                root.right_child = delete_recursive(root.right_child)
            else:
                if root.left_child is None:
                    tmp = root.right_child
                    root.right_child, root.left_child, root.data = None, None, None
                    return tmp
                elif root.right_child is None:
                    tmp = root.left_child
                    root.right_child, root.left_child, root.data = None, None, None
                    return tmp
                tmp = self.findPredessor(root.left_child)
                root.data = tmp.data
                root.left_child = delete_recursive(root.left_child)
            return root

        self.root = delete_recursive(self.root)


    def traverse_inorder(self):
        ret = []
        def inorder_recursive(root):
            if root is None:
                return
            inorder_recursive(root.left_child)
            ret.append(root)
            inorder_recursive(root.right_child)
        inorder_recursive(self.root)
        return ret


if __name__ == "__main__":
    tree = TreeBst()
    elems = 30, 5, 40, 2, 80, 35
    for i in elems:
        tree.insert(i)
    actions = tree.traverse_inorder()
    print(actions)

    tree.delete(80)
    tree.delete(5)
    tree.delete(40)
    actions = tree.traverse_inorder()
    print(actions)