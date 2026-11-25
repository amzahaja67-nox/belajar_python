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


# Fungsi mencari nilai terkecil
def min_value_node(root):
    current = root

    while current.left is not None:
        current = current.left

    return current


# Fungsi untuk menghapus data dari BST
def delete(root, data):
    if root is None:
        return None

    if data < root.data:
        root.left = delete(root.left, data)

    elif data > root.data:
        root.right = delete(root.right, data)

    else:
        # Kondisi 1: Node tidak memiliki anak
        if root.left is None and root.right is None:
            return None

        # Kondisi 2: Node hanya memiliki anak kanan
        elif root.left is None:
            return root.right

        # Kondisi 2: Node hanya memiliki anak kiri
        elif root.right is None:
            return root.left

        # Kondisi 3: Node memiliki dua anak
        successor = min_value_node(root.right)
        root.data = successor.data
        root.right = delete(root.right, successor.data)

    return root


# Fungsi menampilkan BST secara inorder
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Membentuk BST awal
root = None

data_awal = [
    50, 30, 70, 20, 40, 60,
    80, 10, 35, 65, 90
]

for nilai in data_awal:
    root = insert(root, nilai)


# Menampilkan BST sebelum deletion
print("BST SEBELUM DELETION:")
inorder(root)


# Data yang akan dihapus
data_hapus = [10, 60, 70]

# Proses penghapusan
for nilai in data_hapus:
    root = delete(root, nilai)

    print("\n\nMenghapus data:", nilai)
    print("BST setelah penghapusan:")
    inorder(root)


# Menampilkan root akhir
print("\n\nRoot BST setelah deletion:", root.data)
