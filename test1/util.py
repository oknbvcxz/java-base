import os
import re
# 函数：查找包含 main 方法的类名
def find_main_class(file_path):
    main_class = None
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # 使用正则表达式查找 main 方法
        if re.search(r'public\s+static\s+void\s+main\s*\(', content):
            # 提取类名（假设文件名与类名相同）
            match = re.search(r'package\s+([a-zA-Z0-9._]+)\s*;', content)
            if match:
                package = match.group(1)
                class_name = os.path.splitext(os.path.basename(file_path))[0]
                main_class = f"{package}.{class_name}"
    return main_class

# 函数：生成 javac 命令
def generate_javac_command(src_dir):
    java_files_by_dir = {}

    # 遍历目录结构并收集 .java 文件
    for root, dirs, files in os.walk(src_dir):
        java_files = [os.path.join(root, file) for file in files if file.endswith('.java')]
        
        if java_files:
            relative_path = os.path.relpath(root, src_dir)  # 获取相对路径
            java_files_by_dir[relative_path] = java_files

    # 计算 bin 目录路径
    bin_dir = os.path.join(os.path.dirname(src_dir), 'bin')

    # 构建 javac 命令
    javac_command = ["javac", "-d", bin_dir, "-sourcepath", src_dir, "-encoding", "UTF-8"]

    # 逐个目录构建 *.java 命令参数
    for relative_path, java_files in java_files_by_dir.items():
        if len(java_files) > 1:
            # 如果目录下有多个 .java 文件，使用 *.java 通配符
            javac_command.append(os.path.join(src_dir, relative_path, "*.java"))
        else:
            # 如果只有一个 .java 文件，直接列出文件路径
            javac_command.append(java_files[0])

    return " ".join(javac_command)

# 函数：生成 java 命令
def generate_java_command(main_class, bin_dir):
    return f"java -cp {bin_dir} {main_class}"

# 主函数：生成命令
def main(src_dir):
    # 找到所有 Java 文件并生成 javac 命令
    javac_command = generate_javac_command(src_dir)
    print(f"## {javac_command}")

    # 查找包含 main 方法的类
    main_class = None
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                found_main_class = find_main_class(file_path)
                if found_main_class:
                    main_class = found_main_class
                    break

    # 如果找到 main 方法所在的类，生成 java 命令
    if main_class:
        # 计算 bin 目录路径
        bin_dir = os.path.join(os.path.dirname(src_dir), 'bin')
        java_command = generate_java_command(main_class, bin_dir)
        print(f"## {java_command}")
    else:
        print("No main method found in any Java file.")

# 执行主程序
if __name__ == "__main__":
    src_dir = input("Enter the path to the src directory: ").strip()
    main(src_dir)


## javac -d test1\bin -sourcepath test1/src -encoding UTF-8 test1/src\com\myapp\*.java test1/src\com\utils\StringUtils.java test1/src\model\Model.java
## java -cp test1\bin com.myapp.Main