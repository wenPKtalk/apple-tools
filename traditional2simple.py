import codecs
import os
import pathlib
import sys

import click
import opencc

_this_dir = os.path.dirname(os.path.abspath(__file__))
_opencc_rootdir = os.path.abspath(os.path.join(_this_dir, '..', '..'))
_test_assets_dir = os.path.join(_this_dir, 'txt')

ROOT = pathlib.Path(__file__).absolute().parents[2]
sys.path.append(str(ROOT))


def traditional2simple(file_path, out_path):
    try:
        cc = opencc.OpenCC("t2s")
        with codecs.open(file_path, mode='r', encoding='utf-8') as rf:
            text_content = cc.convert(rf.read())
        with codecs.open(out_path, mode='w', encoding='utf-8') as wf:
            wf.write(text_content)
            return True

    except Exception as e:
        return False


def main():
    data_path = f'{_this_dir}/txt'
    save_path = f'{_this_dir}/simpleTxt'
    for item in os.listdir(data_path):
        if not (item.split('.')[-1] == 'txt' or item.split('.') == "txt"):
            continue
        file_path = os.path.join(data_path, item)
        stem, ext = os.path.splitext(item)
        out_path = os.path.join(save_path, stem + '.txt')
        traditional2simple(file_path, out_path)


if __name__ == '__main__':
    main()
