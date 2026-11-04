# Node untuk pohon biner
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Preorder: Root -> Kiri -> Kanan
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Inorder: Kiri -> Root -> Kanan
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Postorder: Kiri -> Kanan -> Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Membuat struktur pohon biner
root = Node(10)
root.left, root.right = Node(5), Node(15)
root.left.left, root.left.right = Node(3), Node(7)
root.right.right = Node(20)

# Menampilkan hasil traversal
print("Preorder  :", end=" ")
preorder(root)

print("\nInorder   :", end=" ")
inorder(root)

print("\nPostorder :", end=" ")
postorder(root)
print()
