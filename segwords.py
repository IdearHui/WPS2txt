#!/usr/bin/env Python
# coding=utf-8

import jieba.analyse
import os
import xlwt  # 写入Excel表的库
import sys
import importlib
importlib.reload(sys)


class Tokenize:
    def __init__(self):
        self.base_dir = os.getcwd() + '/doc/'

    def get_all_files(self, fp, suffix):
        """
        获取所有fp目录下的文件名,存入file_list列表中
        :param suffix: 后缀名
        :param fp:     目录
        :return:
        """
        file_names = []
        for f in os.listdir(fp):
            if suffix:
                if f.find(suffix) != -1:
                    file_names.append(f)
        return file_names

    def tokenizer(self, fp):
        """
        分词
        :param fp: txt文件路径
        :return:
        """
        word_list = []
        with open(fp) as f:
            for line in f:  # 1.txt是需要分词统计的文档
                line = line.encode("utf-8").decode()
                item = line.strip('\n\r').split('\t')  # 制表格切分
                tags = jieba.analyse.extract_tags(item[0])  # jieba分词
                for t in tags:
                    word_list.append(t)
        return word_list

    def write_to_txt(self, fp, word_lst):
        """
        保存到文件
        :param fp:
        :param word_lst:
        :return:
        """
        # 判断路径是否存在
        if not os.path.exists(self.base_dir + 'result/'):
            os.mkdir(self.base_dir + 'result/')
        word_dict = {}
        # 创建单元格
        wbk = xlwt.Workbook(encoding='ascii')
        sheet = wbk.add_sheet("wordCount")  # Excel单元格名字
        # 统计词数量并按个数降序排序
        for word in word_lst:
            word_dict[word] = word_dict.get(word, 0) + 1
        order_list = sorted(word_dict.items(), key=lambda d: d[1], reverse=True)
        # 保存到txt文件
        with open(fp, 'w') as wf2:  # 打开文件
            for k, v in order_list:
                wf2.write(k + ' ' + str(v) + '\n')  # 写入txt文档
        # 保存到xls文件
        for i, item in enumerate(order_list):
            sheet.write(i, 1, label=item[0])
            sheet.write(i, 0, label=item[1])
        wbk.save(fp.split('.')[-2] + '.xls')  # 保存为 wordCount.xls文件

    def main(self):
        file_list = self.get_all_files(self.base_dir, '.txt')
        if file_list:
            for fn in file_list:
                fp = self.base_dir + fn
                words = self.tokenizer(fp)
                self.write_to_txt(self.base_dir + '/result/' + fn.split("/")[-1], words)
