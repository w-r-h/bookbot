def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents
    
def word_count(file_contents):
    words = file_contents.split()
    i = 0
    for word in words:
        i += 1
    final_count = i
    return final_count

def char_count(chars):
    letter_count = {}
    for char in chars:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count
    
txt = main()
w_count = word_count(txt)
c_count = char_count(txt.lower())

def dict_to_list_loop(c_count):
    output_list = []
    
    for key, value in c_count.items():
        if isinstance(key, str) and key.isalpha():
            output_list.append({'key': key, 'value': value})
    return output_list


dict_list = dict_to_list_loop(c_count)

def sort_on(dict):
    return dict["value"]

dict_list.sort(reverse=True, key=sort_on)


print("--- Begin report of books/frankenstein.txt ---")
print(f"{w_count} words found in document\n\n")


for dictionary in dict_list:
    final_val = []
    for value in dictionary.values():
        val1 = value
        final_val.append(val1)
    print(f"The {final_val[0]} character was found {final_val[1]} times")
print("--- End Report ---")