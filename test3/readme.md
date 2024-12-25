# 项目介绍
介绍jar包使用方法。
包括直接使用，maven使用和gradle使用
# 使用
```shell
# 直接使用
javac -encoding utf-8 -cp lib/myapp.jar src/com/example/App.java -d bin
java -cp bin;lib/myapp.jar com.example.App
# maven
确保项目的目录结构为src/main/java/com/example/App.java src/test/java/com/example/AppTest.java ... 根目录下有pom.xml
可以执行一下命令生产maven项目：
mvn archetype:generate -DgroupId=com.example -DartifactId=helloworld -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
mvn exec:java # 执行 exec-maven-plugin插件命令
mvn exec:java -Dexec.mainClass="com.example.App"
mvn package # 打包
mvn install # 安装到本地仓库
mvn clear   # 清理打包文件
# 当前项目也打了jar包的执行方法：
java -cp target/test3-1.0.0.jar;lib/myapp.jar com.example.App
java -cp target/test3-1.0.0.jar;lib/myapp.jar com.myapp.Main
java -cp target/test3-1.0.0.jar;lib/myapp.jar com.myapp.Main
java -Djava.ext.dirs=./lib -jar target/test3-1.0.0.jar
# maven创建项目方法
mvn archetype:generate -DgroupId=com.example -DartifactId=helloworld -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
```
# maven核心概念
1. Maven 的生命周期和阶段是其构建系统的核心概念。以下是 Maven 的主要生命周期及其包含的阶段：

1.1. Maven 生命周期
- default（默认）生命周期
这是 Maven 最常用的生命周期，它包含了从项目构建到部署的所有主要步骤。
- clean（清理）生命周期
该生命周期主要用于清理项目，比如删除编译生成的文件。
- site（站点）生命周期
用于生成项目的站点文档。

1.1.1. default 生命周期的阶段
default 生命周期是 Maven 中最核心的生命周期，它包含以下阶段：
- validate
验证项目是否正确，所有必要的信息是否可用。
- compile
编译项目的源代码。
- test
使用单元测试框架测试编译后的代码。
- package
将编译后的代码打包成可分发的格式，如 JAR、WAR 等。
- verify
对集成测试的结果进行检查，以确保质量标准。
- install
将包安装到本地 Maven 仓库，供其他项目使用。
- deploy
将最终的包复制到远程仓库，供其他开发人员和项目共享。

1.1.2. clean 生命周期的阶段
clean 生命周期包含以下阶段：
- pre-clean
执行项目清理前的准备工作。
- clean
删除上一次构建生成的文件。
- post-clean
执行项目清理后的清理工作。

1.1.3. site 生命周期的阶段
site 生命周期包含以下阶段：
- pre-site
执行站点生成前的准备工作。
- site
生成项目的站点文档。
- post-site
执行站点生成后的清理工作。
- site-deploy
将生成的站点文档部署到指定的服务器。

2. 插件目标和绑定
Maven 的每个生命周期阶段都可以绑定一个或多个插件目标。这些目标是在特定阶段执行的具体任务。例如，maven-compiler-plugin 的 compile 目标通常绑定到 default 生命周期的 compile 阶段。

3. 自定义生命周期和阶段
虽然 Maven 提供了默认的生命周期和阶段，但用户也可以通过配置插件来创建自定义的生命周期和阶段。

4. 总结
Maven 的生命周期和阶段提供了一种结构化的方式来组织和管理构建过程。了解这些生命周期和阶段有助于更好地理解和使用 Maven 进行项目构建。