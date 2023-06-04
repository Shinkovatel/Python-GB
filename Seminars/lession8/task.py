# path = 'phones.txt'
# data = open(path, 'w')
# for line in data:
#
#
# print(line)
# data.close()
#


def open_file_read(path):
    with open(path, 'r') as file:
        main_list = (file.readlines())
        # main_list_str = [x.rstrip().split(',') for x in main_list]
    return main_list

#
print(open_file_read('phones.txt'))


def open_file_write(path, list_file):
    with open(path, 'a') as file:
        file.writelines(list_file + '\n')

#
list_for_look = [['Ivanov', 'Ivan', '123456', 'comment'], ['Petrov', 'Petr', '456789', 'comment'],
                 ['Chudilov', 'Sasha', '987654', 'comment']]

#
def look_list(list_for_look):
    print([' '.join(x) for x in list_for_look], end='\n')
#
#

def file_delite(path, text_delite):
    with open(path, 'r') as file:
        lines = file.readlines()
    with open(path,'w') as file:
        for line in lines:
            if line.strip('\n') != text_delite:
                file.write(line)

# look_list(list_for_look)

# list_file = [['wqweqwe','ewew','wewewe','wewew'],['fsdfsdfsdf','fsdfsdf','dsfdsf','dfdf']]
# open_file_write('phones1.txt', list_file)

