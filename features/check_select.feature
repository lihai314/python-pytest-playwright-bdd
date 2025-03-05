Feature: 筛选功能验证
  作为用户
  我想要使用筛选功能
  以便快速找到所需信息

  Background:
    Given 我已登录系统

  Scenario Outline: 成功筛选
    When 我在筛选栏输入 "<condition>"
    Then 我应该看到 "<expected_result>"

    Examples:
      | condition | expected_result |
      | 有效条件 | 符合条件的结果 |
