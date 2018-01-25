# -*- coding: utf-8 -*-
import argparse
import os
import sys
from parser.doc2txt import Doc2Txt
from segwords import Tokenize


def parse_args():
    """
    Parses the node2vec arguments.
    """
    parser = argparse.ArgumentParser(description="Run This Project.")

    parser.add_argument('-task', help='[0: 执行word文档转为txt的任务；1: 执行对txt进行分词的任务]')

    return parser.parse_args()


def main(cmd_args):
    """
    程序主入口,控制程序流程
    :return:
    """
    if not cmd_args.task:
        print("Error: 参数错误！请添加task参数及其值！")
        # os.system('python3 main.py -h')
        sys.exit(1)
    if cmd_args.task == "0":
        dt = Doc2Txt()
        dt.main()
    else:
        tok = Tokenize()
        tok.main()


if __name__ == '__main__':
    main(parse_args())
