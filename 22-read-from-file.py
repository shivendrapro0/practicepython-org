# names_fo = open('tmp_dir/nameslist.txt')
# name_dict = {}
# for name in names_fo.readlines():
#     name = name.rstrip()
#     name_dict.setdefault(name,0)
#     name_dict[name] = name_dict[name] + 1
# for name in name_dict:
#     print(" Name = ",name,", Count = ",name_dict[name])
#

counter_dict = {}
with open('tmp_dir/Training_01.txt','r') as f:
    for image_path in f.readlines():
        category_name = image_path[3:-26]
        counter_dict.setdefault(category_name,0)
        counter_dict[category_name] = counter_dict[category_name] + 1
print(counter_dict)
