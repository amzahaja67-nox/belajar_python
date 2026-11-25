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


# Fungsi menampilkan data secara inorder
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Membentuk BST awal
root = None
data_awal = [50, 30, 70, 20, 40, 60, 80]

for nilai in data_awal:
    root = insert(root, nilai)


# Menambahkan data baru
data_baru = [10, 35, 65, 90]

for nilai in data_baru:
    root = insert(root, nilai)
    print("Data berhasil ditambahkan:", nilai)


# Menampilkan hasil BST
print("\n\nHasil Inorder Setelah Insertion:")
inorder(root)

print("\n\nRoot BST:", root.data)
