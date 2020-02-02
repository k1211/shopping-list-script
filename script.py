f = open("week1.txt", "r", encoding='utf-8')
lines = f.readlines()
items = []

for line in lines:
    if line.startswith('+'):
        items.append(line.strip().strip('+ '))

# print(items)
item_dict = {}

for item in items:
    abc = item.split(' x ')

    item_name = abc[0].split(' ')
    item_amout = abc[1].split(' ')
    item_amout = float(item_amout[1]) if len(item_amout) > 1 else 0
    # print(item_name)
    the_item_name = f"{item_name[0]} {item_name[1]}" if len(item_name) > 2 else item_name[0]
    print(the_item_name)
    print(item_amout)
    print('--')

    if the_item_name in item_dict:
        item_dict[the_item_name] += item_amout
    else:
        item_dict[the_item_name] = item_amout

print('----------')
sorted_dict = {k: item_dict[k] for k in sorted(item_dict)}
print(sorted_dict)
