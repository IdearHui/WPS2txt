# -*- coding: utf-8 -*-
import argparse
import os
from parser.doc2txt import Doc2Txt
from segwords import Tokenize


def parse_args():
    """
    Parses the node2vec arguments.
    """
    parser = argparse.ArgumentParser(description="Run This Project.")

    parser.add_argument('-task', help='word文档转换成txt文档 [0: 执行word文档转为txt的任务；1: 执行对txt进行分词的任务]')

    parser.add_argument('--input', help='输入文件路径')

    parser.add_argument('--output', help='输出文件路径')

    return parser.parse_args()


def main(cmd_args):
    """
    程序主入口,控制程序流程
    :return:
    """
    task = cmd_args.task
    input_fp = cmd_args.input
    output_fp = cmd_args.output

    if not task and not input_fp and not output_fp:
        os.system('python3 main.py -h')
    elif not task:
        print("参数错误！请添加task参数及其值！")
        os.system('python3 main.py -h')
    elif not input_fp or not output_fp:
        print("参数错误！请添加input和output参数及其值！")
        os.system('python3 main.py -h')
    else:
        if task == "0":
            dt = Doc2Txt()
            dt.main()
        else:
            tok = Tokenize()
            tok.main()


if __name__ == '__main__':
    main(parse_args())
