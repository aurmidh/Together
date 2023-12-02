def is_palindrome(word):
    # Funkcja sprawdzająca, czy słowo jest palindromem
    return word.lower() == word.lower()[::-1]

def main():
    try:
        # Pobierz od użytkownika słowa, oddzielone przecinkami
        words_input = input("Podaj słowa, oddzielone przecinkami: ")
        words = [word.strip() for word in words_input.split(',')]

        # Sprawdź, czy słowa są palindromami
        palindromes = []
        non_palindromes = []
        for word in words:
            if is_palindrome(word):
                palindromes.append(word)
            else:
                non_palindromes.append(word)

        # Wypisz wyniki
        print("Palindromy:", palindromes)
        print("Nie palindromy:", non_palindromes)

        # Zapisz do plików
        with open("palindromes.txt", 'w') as palindromes_file:
            palindromes_file.write(','.join(palindromes))

        with open("non_palindromes.txt", 'w') as non_palindromes_file:
            non_palindromes_file.write(','.join(non_palindromes))

        print("Palindromy zostały zapisane do pliku 'palindromes.txt'")
        print("Nie palindromy zostały zapisane do pliku 'non_palindromes.txt'")

    except Exception as e:
        print(f"Błąd: {e}")

if __name__ == "__main__":
    main()

