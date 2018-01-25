import os
import platform

BASE_DIR = os.getcwd()
seg = ''


def check_platform():
    """
    获取操作系统类型
    :return:
    """
    return platform.system()


def get_seg():
    """
    根据操作系统类型返回文件夹分隔符
    :return:
    """
    if check_platform().find('Windows') != -1:
        return "\\"
    else:
        return "/"


DOC_DIR = BASE_DIR + get_seg()


def get_all_files(fp, suffix):
    """
    获取所有fp目录下的文件名,存入file_list列表中
    :param suffix: 后缀名
    :param fp:     目录
    :return:
    """
    file_name_list, file_names = [], []
    for root_dir, fp, files in os.walk(fp):
        for file in files:
            if suffix and file.find(suffix) != -1:
                file_name_list.append(root_dir + get_seg() + file)
                file_names.append(file)
    return file_name_list, file_names


def write_to_file(fp, mode, content):
    """
    公共方法,用于写数据到文件
    :param mode:
    :param fp:
    :param content:
    :return:
    """
    with open(fp, mode) as f:
        if mode == 'w':
            for line in content:
                f.write(str(line) + "\n")
        else:
            f.write(str(content) + "\n")
