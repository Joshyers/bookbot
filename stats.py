def get_count_words(book):
    words_list = book.split()
    return len(words_list)

def get_count_characters(book):
    dict_char = {}
    book = book.lower()
    for char in book :
        if char in dict_char:
            dict_char[char] += 1
        else :
            dict_char[char] = 1
    return dict_char

def chars_dict_to_sorted_list(chars_dict):
    def sort_on(items):
        return items["num"]
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"name" : char, "num" : chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list