##############################################################
# generate shopping list from weekly menu from my dietitian
##############################################################

import argparse
import os

DAYS = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']


def handle_menu_file(menu_file):
    if os.path.isfile(menu_file):
        if menu_file.find('.'):
            file_name, extension = menu_file.split('.')
            if extension == 'txt':
                return menu_file
            print(menu_file)
            # TODO convert pdf file to txt
    raise Exception(f"'{menu_file}' file does not exist in this directory!")


def generate_shopping_list(menu_file_in_pdf):
    menu_file = handle_menu_file(menu_file_in_pdf)
    f = open(menu_file, "r", encoding='utf-8')
    items = [line.strip().strip('+ ') for line in f.readlines() if line.startswith('+')]
    item_dict = {}

    for item in items:
        item_info = item.split(' x ')

        item_name_info = item_info[0].split(' ')
        item_name = f"{' '.join(item_name_info[:-1])}" if len(item_name_info) > 2 else item_name_info[0]

        if len(item_info) == 1:
            print(f"Undisclosed item amount for: {item_info[0]}")
            item_amount = 0
        else:
            item_amount = item_info[1].split(' ')
            try:
                item_amount = float(item_amount[-2]) if len(item_amount) > 1 else 0
            except:
                print(f"Unidentifiable item amount: {item_amount[1]}")
                _item_amount = item_amount[1].replace('g', '')
                item_amount = float(_item_amount) if len(item_amount) > 1 else 0

        if item_name in item_dict:
            item_dict[item_name] += item_amount
        else:
            item_dict[item_name] = item_amount

    sorted_dict = {k: item_dict[k] for k in sorted(item_dict)}
    return sorted_dict


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", "-f", default="week.txt", help="File name with extension name.")
    args = parser.parse_args()
    shopping_list = generate_shopping_list(str(args.file_name))
    print(shopping_list)
