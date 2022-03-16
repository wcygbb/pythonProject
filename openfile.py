import os.path
from uuid import uuid4


def make_file(base_path, num, suffix):
    """
    :param base_path: 需要生成文件的目录
    :param num: 需要生成文件的个数
    :param suffix: 文件名后缀
    :return:
    """
    for i in range(num):
        path = os.path.join(base_path,f'{str(uuid4())}.{suffix}')
        open (path, "w")




# 1、获取到path所有的文件名
# 2、定义一个new_fule_name = 1
# 3、如果suffix存在
#     循环files
#         如果file是已suffix结尾
#             修改文件名
#             new_fule_name + 1
# 4、如果suffix不存在
#     循环files
#         修改文件名
#         new_fule_name + 1

# def rename_file(base_path, suffix=None):
def rename_file(base_path, *args):
    """
    :param base_path: 需要替换文件名称的目录
    :param suffix: 需要修改那种文件的名字、为None修改所有文件
    :return:
    """
    newname = 500
    fileList = os.listdir(base_path)  # 获取该目录下所有文件，存入列表中
    for i in fileList:
        if args:
            if not i.endswith (args):
                continue
        suffix = i.split(".")[1]
        os.rename(os.path.join(base_path, i), os.path.join(base_path, f'{newname}.{suffix}'))
        newname += 1
    # fileList = os.listdir(base_path)#获取该目录下所有文件，存入列表中
    # newname = 100
    # if args:
    #     for i in fileList:
    #         if i.endswith(args):
    #             suffix = i.split(".")[1]
    #             os.rename(os.path.join(base_path, i), os.path.join(base_path, f'{newname}.{suffix}'))
    #             newname += 1
    #
    # else:
    #     for i in fileList:
    #         suffix = i.split(".")[1]
    #         os.rename(os.path.join(base_path, i), os.path.join(base_path, f'{newname}.{suffix}'))
    #         newname += 1

base_path = r"D:\pythonProject\file"
# make_file(base_path, 10, "md")
# make_file(base_path, 10, "py")
# make_file(base_path, 10, "txt")
rename_file(base_path,"txt")