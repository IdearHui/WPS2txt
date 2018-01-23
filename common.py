import os


def get_all_files(fp, suffix):
    """
    获取所有fp目录下的文件名,存入file_list列表中
    :param suffix: 后缀名
    :param fp:     目录
    :return:
    """
    file_name_list = []
    for f in os.listdir(fp):
        if suffix and f.find(suffix) != -1:
                file_name_list.append(f)
    return file_name_list


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
