import os

FOLDER = 'text_files'
COMBINED_TEXT_FILE = '4.txt'


def get_text_file_info(file_name):
    file_path = os.path.join(FOLDER, file_name)
    with open(file_path, encoding='utf-8') as file:
        text = file.readlines()
        filename = f'{file_name}\n'
        text_length = f'{len(text)}\n'
        new_text = [filename, text_length]
        new_text.extend(text)
    return new_text


def add_separator(text):
    for item in text[1:]:
        for ind, line in enumerate(item):
            if '.txt' in line:
                item[ind] = f'\n{line}'
    return text


if __name__ == '__main__':
    file_names = os.listdir(FOLDER)
    combined_text = []
    for file_name in file_names:
        text_info = get_text_file_info(file_name)
        combined_text.append(text_info)
    combined_text.sort(key=len)
    combined_text = add_separator(combined_text)
    with open(COMBINED_TEXT_FILE, 'w', encoding='utf-8') as file:
        for text in combined_text:
            file.writelines(text)
