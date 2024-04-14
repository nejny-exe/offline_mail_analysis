# import re
# import os
# import email
# from collections import defaultdict
# from email import policy
# from email.parser import BytesFeedParser
#
# # Словарь с названиями функций и соответствующими регулярными выражениями
# patterns_dict = {
#     'account': r'\b\d{20}\b',
#     'card': r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b(?:\s\d{2}/\d{2})?(?:\s\d{3})?\b',
#     'passport': r'\b\d{4}(?:[ -]?[N№]?[ -]?|\s?)\d{6}\b',
#     'phone': r'\+7\s?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}',
#     'snils': r'\b\d{3}-\d{3}-\d{3}\s\d{2}\b',
# }
#
#
# def add_pattern(name, pattern):
#     # Добавляем новый шаблон в словарь и создаем функцию для его анализа
#     patterns_dict[name] = pattern
#     func_name = f"extract_{name}_numbers"
#
#     def func(text):
#         return re.findall(pattern, text)
#
#     globals()[func_name] = func
#
#
# def analyze_email_file(file_path, selected_patterns):
#     leaks = defaultdict(int)
#
#     with open(file_path, 'r', encoding="utf-8") as file:
#         msg = email.message_from_file(file)
#         body = ''
#
#         for part in msg.walk():
#             content_type = part.get_content_type()
#             if content_type == 'text/plain' or content_type == 'text/html':
#                 body += part.get_payload(decode=True).decode()
#
#         for pattern_name in selected_patterns:
#             if hasattr(globals(), f"extract_{pattern_name}_numbers"):
#                 func = globals()[f"extract_{pattern_name}_numbers"]
#                 leaks[pattern_name] += len(func(body))
#
#     return dict(leaks)
#
#
# def main(directory_path, selected_patterns):
#     total_leaks = defaultdict(int)
#     files_with_leaks = 0
#     total_files = 0
#     files_with_selected_leaks = []
#
#     for filename in os.listdir(directory_path):
#         file_path = os.path.join(directory_path, filename)
#
#         if os.path.isfile(file_path) and filename.endswith('.eml'):
#             leaks = analyze_email_file(file_path, selected_patterns)
#             total_files += 1
#
#             if any(leaks.values()):
#                 files_with_leaks += 1
#                 files_with_selected_leaks.append((filename, leaks))
#
#             for pattern_name, count in leaks.items():
#                 total_leaks[pattern_name] += count
#
#     print(f"Total files processed: {total_files}")
#     print(f"Total files with leaks: {files_with_leaks}")
#     for pattern_name, count in total_leaks.items():
#         print(f"{pattern_name}: {count}")
#
#     print("\nFiles with selected leaks:")
#     for filename, leaks in files_with_selected_leaks:
#         print(f"{filename}: {leaks}")
#
#
# if __name__ == '__main__':
#     directory_path = 'D:/Загрузки/Telegram Desktop/Samples'
#
#     print("Select the types of data leaks you want to find (comma-separated or 'all' for all):")
#     print("Options: account, card, passport, phone, snils, email")
#     selected_patterns_input = input().strip().lower()
#     add_pattern('manifest', 9054416624)
#     print(patterns_dict)
#     if selected_patterns_input == 'all':
#         selected_patterns = patterns_dict.keys()
#     else:
#         selected_patterns = selected_patterns_input.split(',')
#
#     main(directory_path, selected_patterns)
import re
ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
      'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

def generate_regex(example):
    regex = r'\b'
    for char in example:
        if char.isalpha():
            if char.isupper() and not (char.lower() in ru):
                regex += '[A-Z]'
            elif char.islower() and not (char.lower() in ru):
                regex += '[a-z]'
            elif char.isupper() and char.lower() in ru:
                regex += '[А-ЯЁ]'
            elif char.islower() and char.lower() in ru:
                regex += '[а-яё]'

        elif char.isdigit():
            regex += '\d'
        elif char.isspace():
            regex += '\s'
        else:
            regex += re.escape(char)
    regex += r'\b'
    return regex


text = input('Введите текст:')
text_regex = generate_regex(text)
print(f"Regex для {text}:", text_regex)
text_pattern = re.compile(text_regex)
print(text_pattern)
text_match = text_pattern.fullmatch("а000аа")
print("Соответствие шаблону: ", bool(text_match))

