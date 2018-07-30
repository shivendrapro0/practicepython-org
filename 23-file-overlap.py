happy_num_list = []
prime_num_list = []

with open('tmp_dir/primenumbers.txt') as fo:
    prime_num_list = set(fo.read().split())
with open('tmp_dir/happynumbers.txt') as fo:
    happy_num_list = set(fo.read().split())

intersection_list = prime_num_list | happy_num_list