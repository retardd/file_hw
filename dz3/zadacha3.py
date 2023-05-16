def get_files_lines(files_list):
    all_strings = []
    for file in files_list:
        file_strings = []
        with open(file, 'r') as f:
            file_strings.append(file)
            temp_strings = f.readlines()
            file_strings.append(len(temp_strings))
            file_strings += temp_strings
        all_strings.append(file_strings)
    all_strings = sorted(all_strings, reverse=False, key=lambda x: x[1])

    return all_strings

list_strings = get_files_lines(['first.txt', 'two.txt', 'three.txt'])
with open("res.txt", "w") as f:
    for strings in list_strings:
        for string in strings:
            f.write(str(string).rstrip() + '\n')