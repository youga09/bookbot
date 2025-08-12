import sys

def get_num_words():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    new_string = file_contents.split()
    cont = 0
    for i in new_string:
        cont += 1
    return cont

def get_sep_count():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    lwr_string = file_contents.lower()
    bot = {}
    for i in lwr_string:
        if i in bot:
            bot[i] = bot[i] + 1
        else:
            bot[i] = 1
    return bot

def sort_on(items):
    return items["num"]

def get_sorted_dictionary():
    diction_list = []
    dict = get_sep_count()
    for i in dict:
        diction_list.append({"char": i, "num": dict[i]})
    diction_list.sort(reverse=True, key=sort_on)
    return diction_list

def print_report(book_path, nr_words, diction_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {nr_words} total words")
    print("--------- Character Count -------")
    for i in diction_list:
        if not i["char"].isalpha():
            continue
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

def verify_sys():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
