def generate_chunks(input_string):
    # Funkcja generująca chunki o długości od 4 do 7 znaków
    chunks = []
    i = 0
    while i < len(input_string):
        chunk_length = min(7, len(input_string) - i)
        chunks.append(input_string[i:i + chunk_length])
        i += chunk_length
    return chunks

def main():
    try:
        # Pobierz od użytkownika losowy ciąg znaków
        input_string = input("Podaj losowy ciąg znaków: ")

        # Sprawdź, czy ciąg ma co najmniej 4 znaki
        if len(input_string) < 4:
            raise ValueError("Ciąg znaków musi mieć co najmniej 4 znaki.")

        # Wygeneruj chunki
        chunks = generate_chunks(input_string)

        # Zapisz chunki do pliku
        file_name = input("Podaj nazwę pliku do zapisu: ")
        with open(file_name, 'w') as file:
            file.write('\n'.join(chunks))

        print(f"Chunki zostały zapisane do pliku {file_name}")

    except ValueError as ve:
        print(f"Błąd: {ve}")

if __name__ == "__main__":
    main()

