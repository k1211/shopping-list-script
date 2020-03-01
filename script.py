##############################################################
# generate shopping list from weekly menu from my dietitian
##############################################################


def parse_pdf_file_to_txt(pdf_file):
    return 'week.txt'


def generate_shopping_list(menu_file_in_pdf):
    menu_file = parse_pdf_file_to_txt(menu_file_in_pdf)

    f = open(menu_file, "r", encoding='utf-8')
    lines = f.readlines()
    items = []

    for line in lines:
        if line.startswith('+'):
            items.append(line.strip().strip('+ '))

    item_dict = {}

    for item in items:
        abc = item.split(' x ')

        item_name = abc[0].split(' ')
        item_amout = abc[1].split(' ')
        item_amout = float(item_amout[1]) if len(item_amout) > 1 else 0
        the_item_name = f"{' '.join(item_name[:-1])}" if len(item_name) > 2 else item_name[0]

        if the_item_name in item_dict:
            item_dict[the_item_name] += item_amout
        else:
            item_dict[the_item_name] = item_amout

    print('----------')
    sorted_dict = {k: item_dict[k] for k in sorted(item_dict)}
    print(sorted_dict)


if __name__== "__main__":
    file_name = input("Please enter file name: ")
    print("You entered: " + file_name)
    generate_shopping_list(file_name)
