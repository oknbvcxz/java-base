# 项目介绍
介绍java项目的构成以及运行方法
# 使用
```shell
python util.py 
    输出：
    Enter the path to the src directory: test1/src
    ## javac -d test1\bin -sourcepath test1/src -encoding UTF-8 test1/src\com\myapp\*.java test1/src\com\utils\StringUtils.java test1/src\model\Model.java
    ## java -cp test1\bin com.myapp.Main
javac -d test1\bin -sourcepath test1/src -encoding UTF-8 test1/src\com\myapp\*.java test1/src\com\utils\StringUtils.java test1/src\model\Model.java
java -cp test1\bin com.myapp.Main
```