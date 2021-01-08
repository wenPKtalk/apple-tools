import docx2txt
import os
import pathlib
import sys
import codecs
import click

ROOT = pathlib.Path(__file__).absolute().parents[2]
sys.path.append(str(ROOT))


def word2txt(file_path, out_path):
    try:
        text_content = docx2txt.process(file_path)
        with codecs.open(out_path, mode='w', encoding='utf-8') as wf:
            wf.write(text_content)
            return True

    except Exception as e:
        return False


@click.command()
@click.option('--path', 'path')
def main(path):
    data_path = f'{path}/word'
    save_path = f'{path}/txt'
    for item in os.listdir(data_path):
        if not (item.split('.')[-1] == 'docx' or item.split('.') == "doc"):
            continue
        file_path = os.path.join(data_path, item)
        stem, ext = os.path.splitext(item)
        out_path = os.path.join(save_path, stem + '.txt')
        info = f'{os.path.basename(file_path)} -> {os.path.basename(out_path)}'
        word2txt(file_path, out_path)


if __name__ == '__main__':
    main()
