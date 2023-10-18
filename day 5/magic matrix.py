def generate_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Order 'n' must be odd")

    magic_square = [[0] * n for _ in range(n)]

    # Initialize position for 1st number
    i, j = 0, n // 2

    # Fill the square with numbers
    num = 1
    while num <= n**2:
        magic_square[i][j] = num
        num += 1

        newi, newj = (i - 1) % n, (j + 1) % n

        if magic_square[newi][newj]:
            i = (i + 1) % n
        else:
            i, j = newi, newj

    return magic_square

def print_magic_square(square):
    for row in square:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    n = int(input("Enter the order of the magic square (must be odd): "))
    if n % 2 == 0:
        print("Order 'n' must be odd.")
    else:
        magic_square = generate_magic_square(n)
        print("Magic Square of Order", n)
        print_magic_square(magic_square)

def generate_mirror_magic_square(n):
    if n % 2 == 0:
        raise ValueError("Order 'n' must be odd")

    magic_square = generate_magic_square(n)  # Generate a regular magic square

    # Create a mirror image of the magic square
    mirror_square = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mirror_square[i][j] = magic_square[i][n - 1 - j]

    return mirror_square

if __name__ == "__main__":
    n = int(input("Enter the order of the magic square (must be odd): "))
    if n % 2 == 0:
        print("Order 'n' must be odd.")
    else:
        magic_square = generate_mirror_magic_square(n)
        print("Mirrored Magic Square of Order", n)
        print_magic_square(magic_square)
