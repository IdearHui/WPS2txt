from docx import Document
from common import *

BASE_DIR = os.getcwd()


class Doc2Txt:
    def __init__(self):
        self.doc_dir = BASE_DIR + '/doc/'

    def main(self):
        files = get_all_files(self.doc_dir, '.doc') + get_all_files(self.doc_dir, '.docx')
        for fn in files:
            fp = self.doc_dir + fn
            document = Document(fp)
            # 读取每段资料
            paragraphs = [paragraph.text for paragraph in document.paragraphs]
            write_to_file(fp.split(".")[0]+'.txt', 'w', paragraphs)
