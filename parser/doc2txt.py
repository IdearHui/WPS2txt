from docx import Document
from common import *


class Doc2Txt:
    def __init__(self):
        self.doc_dir = DOC_DIR

    def main(self):
        fp_list, fn_list = get_all_files(self.doc_dir, '.doc')
        for fp in fp_list:
            document = Document(fp)
            # 读取每段资料
            paragraphs = [paragraph.text for paragraph in document.paragraphs]
            write_to_file(fp.split(".")[0]+'.txt', 'w', paragraphs)
