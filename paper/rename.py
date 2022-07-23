import os
import sys

paper_list:list = os.listdir('paper')
path = r'C:\\Users\\songqi\\Documents\\dehazing\\paper\\'

paper_list.remove('rename.py')
c = 0
for p in paper_list:
    src = os.path.join(os.path.abspath(path), p)
    dst = os.path.join(os.path.abspath(path), p.replace('_', ' '))
    try:
        os.rename(src, dst)
        c += 1
    except:
        continue

    print(dst)
    print('\n')


print(f'Total {paper_list.__len__()} to rename & converted {c} files')