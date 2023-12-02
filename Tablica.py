def generate_and_save_array(array_size, max_number, file_name):
    try:
        # Wygeneruj tablicę liczb
        numbers = [str(i) for i in range(1, min(array_size + 1, max_number + 1))]

        # Wypisz tablicę
        print("Wygenerowana tablica liczb:")
        for number in numbers:
            print(number)

        # Zapisz tablicę do pliku
        with open(file_name, 'w') as file:
            file.write('\n'.join(numbers))

        print(f"Tablica liczb została zapisana do pliku {file_name}")

    except Exception as e:
        print(f"Błąd: {e}")

def main():
    try:
        # Pobierz od użytkownika liczbę tablicy i maksymalną liczbę
        array_size = int(input("Podaj liczbę tablicy: "))
        max_number = int(input("Podaj maksymalną liczbę do wygenerowania: "))

        # Sprawdź, czy liczby są dodatnie
        if array_size <= 0 or max_number <= 0:
            raise ValueError("Liczby muszą być dodatnie.")

        # Pobierz nazwę pliku od użytkownika
        file_name = input("Podaj nazwę pliku do zapisu: ")

        # Wygeneruj i zapisz tablicę
        generate_and_save_array(array_size, max_number, file_name)

    except ValueError as ve:
        print(f"Błąd: {ve}")

if __name__ == "__main__":
    main()

