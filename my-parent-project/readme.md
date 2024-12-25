# 项目介绍
介绍maven父项目子项目。
# 使用
```shell
# 创建父项目
mvn archetype:generate -DgroupId=com.example -DartifactId=my-parent-project -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
修改pom文件<packaging>pom</packaging> 然后就可以删除src文件夹了
cd my-parent-project

# 创建子项目
mvn archetype:generate -DgroupId=com.example -DartifactId=module1 -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
# 创建子项目2
mvn archetype:generate -DgroupId=com.example -DartifactId=module2 -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
# 创建子项目3
mvn archetype:generate -DgroupId=com.example -DartifactId=module3 -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

# 父项目应用子项目
<modules>
    <module>module1</module>
    <module>module2</module>
    <module>module3</module>
</modules>
mvn clean install

# 运行单个模块
cd module2
mvn exec:java -Dexec.mainClass="com.example.App"
```