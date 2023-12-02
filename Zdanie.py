def count_words(sentence):
    word_count = {}
    words = sentence.split()

    for word in words:
        # Usunięcie znaków interpunkcyjnych
        word = word.strip('.,?!()[]{}"\'')
        
        # Zliczanie wystąpień słów
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

def main():
    try:
        # Pobierz zdanie od użytkownika
        sentence = input("Podaj zdanie (min. 5 wyrazów): ")
        
        # Sprawdź, czy zdanie ma co najmniej 5 wyrazów
        if len(sentence.split()) < 5:
            raise ValueError("Podane zdanie musi zawierać co najmniej 5 wyrazów.")

        # Zlicz wystąpienia słów
        word_count = count_words(sentence)

        # Wypisz wyniki
        print("Wystąpienia każdego słowa:")
        for word, count in word_count.items():
            print(f"{word}: {count} raz(y)")

        # Zapisz wyniki do pliku
        file_name = input("Podaj nazwę pliku do zapisu: ")
        with open(file_name, 'w') as file:
            for word, count in word_count.items():
                file.write(f"{word}: {count} raz(y)\n")
        
        print(f"Wystąpienia słów zostały zapisane do pliku {file_name}")

    except ValueError as ve:
        print(f"Błąd: {ve}")

if __name__ == "__main__":
    main()
