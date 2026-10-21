# Mencari posisi target dalam data.
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i

    return -1

# Data yang akan dicari.
data = [10, 20, 30, 40, 50]

print(linear_search(data, 10))
print(linear_search(data, 50))
