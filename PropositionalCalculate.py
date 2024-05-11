class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.value = None

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

class TreeBinary:
    def __init__(self, root):
        self.root = root

    def calculate_propositional(self, *param):
        v = list(param)
        def calculate_recursive(root, v):
            if not root:
                return
            if root.data == "AND":
                return calculate_recursive(root.left_child, v) and calculate_recursive(root.right_child,v)
            if root.data == "OR":
                return calculate_recursive(root.left_child,v) or calculate_recursive(root.right_child,v)
            if root.data == "NOT":
                return not calculate_recursive(root.right_child,v)
            if root.data.isdigit():
                return v[int(root.data)]
            if root.data == "#":
                return
        result = calculate_recursive(self.root, v)
        return result





if __name__ == "__main__":
    sexpr = "( OR ( OR ( AND ( 0 NOT ( # 1 ) ) AND ( NOT ( # 0 ) 2 ) ) NOT ( # 2 ) ) )".split()
    root = TreeBinaryBuilder.build(sexpr)
    assert root
    tree = TreeBinary(root)
    prop = tree.calculate_propositional(True, True, True)
    print(prop)