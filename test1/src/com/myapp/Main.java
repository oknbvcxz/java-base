package com.myapp;

import com.utils.StringUtils;
import model.Model;

public class Main {
    public static void main(String[] args) {
        // 使用 StringUtils 打印消息
        System.out.println("Hello from Main!");
        StringUtils.printMessage("Hello from StringUtils!");

        // 使用 Helper 类
        Helper helper = new Helper();
        helper.assist();

        // 使用 Model 类
        Model model = new Model("Sample Model");
        System.out.println("Model name: " + model.getName());
    }
}
