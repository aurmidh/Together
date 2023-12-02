def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def main():
    try:
        n = int(input("Podaj długość ciągu Fibonacciego: "))
        if n <= 0:
            raise ValueError("Długość ciągu musi być liczbą dodatnią.")
        
        fib_sequence = fibonacci(n)

        # Wypisz ciąg
        print(f"Ciąg Fibonacciego o długości {n}: {fib_sequence}")

        # Zapisz do pliku
        file_name = input("Podaj nazwę pliku do zapisu: ")
        with open(file_name, 'w') as file:
            file.write(', '.join(map(str, fib_sequence)))
        
        print(f"Ciąg Fibonacciego został zapisany do pliku {file_name}")

    except ValueError as ve:
        print(f"Błąd: {ve}")

if __name__ == "__main__":
    main()

