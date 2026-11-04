# 1. Rekursif biasa: F(n) = F(n-1) + F(n-2)
def fibonacci_rekursif(n):
    if n <= 1:
        return n
    return fibonacci_rekursif(n - 1) + fibonacci_rekursif(n - 2)


# 2. Rekursif dengan memoization (simpan hasil agar cepat)
def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Program utama
jumlah = int(input("Masukkan jumlah suku Fibonacci: "))

if jumlah < 0:
    print("Error: Jumlah suku tidak boleh negatif!")
else:
    print("\nDeret Fibonacci (Rekursif Sederhana):")
    for i in range(jumlah):
        print(fibonacci_rekursif(i), end=" ")

    print("\n\nDeret Fibonacci (Memoization):")
    for i in range(jumlah):
        print(fibonacci_memo(i), end=" ")
    print()
