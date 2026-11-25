# Class untuk membuat Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Fungsi untuk memasukkan data ke BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Fungsi menampilkan BST secara inorder
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Membuat BST
root = None

data = [45, 25, 65, 15, 35, 55, 75, 10, 20, 30, 40]

for nilai in data:
    root = insert(root, nilai)


# Menampilkan hasil
print("Data yang dimasukkan:")
print(data)

print("\nHasil Inorder Traversal:")
inorder(root)

print("\n\nRoot BST:", root.data)
