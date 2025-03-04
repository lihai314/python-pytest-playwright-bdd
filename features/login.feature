Feature: 登录
  作为用户
  我想要能够登录到系统
  以便使用后续功能

  Background:
    Given 我在登录页面

    Scenario Outline: 成功登录
      When 我输入用户名 "<username>"
      When 我输入密码 "<password>"
      And 点击登录按钮
      Then 我应该看到 Dashboard 页面
      Examples:
        | username | password |
        | 13226689104 | max888888 |
    
    Scenario Outline: 失败登录
      When 我输入用户名 "<username>"
      When 我输入密码 "<password>"
      And 点击登录按钮
      Then 我应该看到登录失败提示 "<error_message>"
      Examples:
        | username | password | error_message |
        | 13226689104 | error_password | 密码错误 |