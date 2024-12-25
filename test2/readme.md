# 项目介绍
1. 介绍打jar包方法，jar包本质就是一个压缩包。介绍jar压缩包内文件结构，主要是里面的MANIFEST.MF
2. 介绍mvn安装当前jar包方法，安装好后其他项目可以通过mvn方便使用当前项目
# 使用
```shell
javac -d bin src/com/myapp/*.java # -d：打包结果存储路径 src/com/myapp/*.java：源文件目录
jar cf lib/myapp.jar -C bin com/myapp # c：创jar包 f：jar路径 -C：打包的文件的目录和包
    生产的jar包下的MANIFEST.MF文件内容
    Manifest-Version: 1.0
    Created-By: 1.8.0_102 (Oracle Corporation)
jar cfe lib/myapp.jar com.myapp.Main -C bin com/myapp # c：创jar包 f：jar路径 e：入口类 -C：打包的文件的目录和包
    生产的jar包下的MANIFEST.MF文件内容
    Manifest-Version: 1.0
    Created-By: 1.8.0_102 (Oracle Corporation)
    Main-Class: com.myapp.Main
创建MANIFEST.MF文件，内容如下：# # 注意MANIFEST.MF最后一行必须有换行符不然最后一行打包不进去
    Manifest-Version: 1.1
    Main-Class: com.myapp.Main
    Class-Path: xxx
    www: xxx
jar cmf MANIFEST.MF lib/myapp.jar -C bin com/myapp # m：指定MANIFEST.MF，文件自己写MANIFEST.MF,指定版本号和主函数路径以及其他信息.
jar cmf 111.x lib/myapp.jar -C bin com/myapp # MANIFEST.MF可以为任意名称，不要怕写错.

java -jar lib/myapp.jar # 运行jar包
```
```shell
## maven安装
创建pom.xml文件
mvn install:install-file -Dfile=lib/myapp.jar -DgroupId=com.myapp -DartifactId=myapp -Dversion=1.0.0 -Dpackaging=jar 
```