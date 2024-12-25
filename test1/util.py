# -*- coding: gbk -*-
# 上一行：当前文件编码
import os
import sys
import re
import shutil
os.chdir(sys.path[0])
encoding='gbk'# java文件编码'utf-8'
def copy_non_java_files(src_dir, bin_dir):
    """
    复制 src_dir 下所有非 .java 文件到 bin_dir 中相应的位置。
    """
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if not file.endswith('.java'):
                # 源文件的完整路径
                src_file = os.path.join(root, file)
                # 目标文件的相对路径
                relative_path = os.path.relpath(root, src_dir)
                # 目标文件的完整路径
                dest_dir = os.path.join(bin_dir, relative_path)
                # 如果目标目录不存在，则创建
                os.makedirs(dest_dir, exist_ok=True)
                dest_file = os.path.join(dest_dir, file)
                # 复制文件
                shutil.copy2(src_file, dest_file)
                print(f"Copied {src_file} to {dest_file}")

def find_main_class(file_path):
    main_class = None
    with open(file_path, 'r', encoding=encoding) as file:
        content = file.read()
        if re.search(r'public\s+static\s+void\s+main\s*\(', content):
            match = re.search(r'package\s+([a-zA-Z0-9._]+)\s*;', content)
            if match:
                package = match.group(1)
                class_name = os.path.splitext(os.path.basename(file_path))[0]
                main_class = f"{package}.{class_name}"
    return main_class

def generate_javac_command(src_dir):
    java_files_by_dir = {}
    for root, dirs, files in os.walk(src_dir):
        java_files = [os.path.join(root, file) for file in files if file.endswith('.java')]
        if java_files:
            relative_path = os.path.relpath(root, src_dir)
            java_files_by_dir[relative_path] = java_files

    bin_dir = os.path.join(os.path.dirname(src_dir), 'bin')
    javac_command = ["javac", "-d", bin_dir, "-encoding", encoding] # "-sourcepath", src_dir, 

    for relative_path, java_files in java_files_by_dir.items():
        if len(java_files) > 1:
            javac_command.append(os.path.join(src_dir, relative_path, "*.java"))
        else:
            javac_command.append(java_files[0])

    return " ".join(javac_command)

def generate_java_command(main_class, bin_dir):
    return f"java -cp {bin_dir};lib/* {main_class}"

def main(src_dir):
    # 复制非 Java 文件到 bin 目录
    copy_non_java_files(src_dir, os.path.join(os.path.dirname(src_dir), 'bin'))

    javac_command = generate_javac_command(src_dir)
    print(f"## {javac_command}")

    main_class = None
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                found_main_class = find_main_class(file_path)
                if found_main_class:
                    main_class = found_main_class
                    break
        if main_class:
            break

    if main_class:
        bin_dir = os.path.join(os.path.dirname(src_dir), 'bin')
        java_command = generate_java_command(main_class, bin_dir)
        print(f"## {java_command}")
    else:
        print("No main method found in any Java file.")

if __name__ == "__main__":
    src_dir = input("Enter the path to the src directory: ").strip()
    main(src_dir)

## javac -d bin src\indi\wrenn\studentsystem\bean\*.java src\indi\wrenn\studentsystem\dao\*.java src\indi\wrenn\studentsystem\frame\*.java src\indi\wrenn\studentsystem\model\*.java src\indi\wrenn\studentsystem\run\TestLogin.java src\indi\wrenn\studentsystem\util\*.java
## java -cp bin;lib/mysql-connector-java-5.1.6-bin.jar indi.wrenn.studentsystem.run.TestLogin

## javac -d bin -encoding gbk src\indi\wrenn\studentsystem\bean\*.java src\indi\wrenn\studentsystem\dao\*.java src\indi\wrenn\studentsystem\frame\*.java src\indi\wrenn\studentsystem\model\*.java src\indi\wrenn\studentsystem\run\TestLogin.java src\indi\wrenn\studentsystem\util\*.java
## java -cp bin;lib/mysql-connector-java-5.1.6-bin.jar indi.wrenn.studentsystem.run.TestLogin
## java -cp bin;lib/* indi.wrenn.studentsystem.run.TestLogin
