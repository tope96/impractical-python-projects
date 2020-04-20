"""Znadz palindromy w pliku tekstowym"""
import load_dictionary

def main():
    """Wczytuje plik ze slownikiem wykorzystujac modul load_directory,
        nastepnie znajduje palindromy i zapisuje je do listy."""
    word_list = load_dictionary.load("2of4brif.txt")
    palindrome_list = []

    for word in word_list:
        if len(word) > 1 and word == word[::-1]:
            palindrome_list.append(word)

    print("\nNumber of palindromes found: {}\n".format(len(palindrome_list)))
    print(*palindrome_list, sep="\n")

if __name__ == "__main__":
    main()
    