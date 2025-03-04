def get_words_count(text: str) -> int:
    return len(text.split())

def get_char_counts(text: str) -> dict[str, int]:
    char_count_dict = {}

    for letter in text:
        letter = letter.lower()

        if letter not in char_count_dict:
            char_count_dict[letter] = 0

        char_count_dict[letter] += 1

    return char_count_dict

def comparator_dict_value(letter_dict: dict[str, int]):
    return letter_dict["count"]

def get_sorted_list_char_counts(
    count_dict: dict[str, int]
) -> list[dict[str, int]]:
    sorted_list = []
    
    for k, v in count_dict.items():
        letter_struct = {
            "letter": k,
            "count": v,
        }
        sorted_list.append(letter_struct)

    sorted_list.sort(reverse=True, key=comparator_dict_value)

    return sorted_list
