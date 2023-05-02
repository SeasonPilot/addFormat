# 导入 os 模块，用于操作文件系统
import os

# 定义要遍历的文件夹路径
folder = "."

# 使用 os.walk 函数遍历文件夹及其子文件夹
for folder_path, subfolders, files in os.walk(folder):
    # 获取当前文件夹的名称
    folder_name = os.path.basename(folder_path)
    # 生成要添加的内容，以文件夹名称作为 categories 的值
    content = "---\nlayout: post\ncategories: {}\n---\n".format(folder_name)
    # 遍历当前文件夹中的所有文件
    for file in files:
        # 如果文件是 markdown 文件
        if file.endswith(".md"):
            # 获取文件的完整路径
            file_path = os.path.join(folder_path, file)
            # 打开文件
            with open(file_path, "r+") as f:
                # 读取文件的原始内容
                original = f.read()
                # 如果文件已经包含了要添加的内容，就跳过这个文件
                if "---\nlayout: post\n" in original:
                    continue
                # 否则，将文件指针移动到开头
                f.seek(0)
                # 写入要添加的内容
                f.write(content)
                # 写入原始内容
                f.write(original)
