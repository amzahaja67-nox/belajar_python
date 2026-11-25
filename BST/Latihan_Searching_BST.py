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


# Fungsi untuk mencari data pada BST
def search(root, target):
    current = root
    jalur = []

    while current is not None:
        jalur.append(current.data)

        if target == current.data:
            return True, jalur

        elif target < current.data:
            current = current.left

        else:
            current = current.right

    return False, jalur


# Membentuk BST
root = None

data = [50, 30, 70, 20, 40, 60, 80,
        10, 35, 65, 90]

for nilai in data:
    root = insert(root, nilai)


# Melakukan pencarian
data_dicari = [20, 35, 65, 90, 100]

print("HASIL PENCARIAN DATA BST")

for target in data_dicari:
    ditemukan, jalur = search(root, target)

    print("\nData yang dicari:", target)
    print("Node yang diperiksa:", " -> ".join(map(str, jalur)))

    if ditemukan:
        print("Status: Data ditemukan")
    else:
        print("Status: Data tidak ditemukan")
