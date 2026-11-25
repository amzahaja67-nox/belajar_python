class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def search(root, target):
    if root is None:
        return False

    if root.data == target:
        return True
    elif target < root.data:
        return search(root.left, target)
    else:
        return search(root.right, target)


# Program utama
root = None

data = [50, 30, 70, 20, 40, 60, 80]

for nilai in data:
    root = insert(root, nilai)

print("Data BST:")
inorder(root)

cari = int(input("\nMasukkan angka yang dicari: "))

if search(root, cari):
    print("Data ditemukan!")
else:
    print("Data tidak ditemukan!")
