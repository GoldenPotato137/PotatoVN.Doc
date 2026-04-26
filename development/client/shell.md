---
order: 4
---

# 侧边栏按钮

要新增内置侧边栏跳转按钮，请按照以下步骤操作：

1. 在`SidebarButtonIds`中新增这个内置按钮的静态id。
2. 在`SidebarService`中把这个内置按钮注册到`_builtInButtons`中，让设置界面可以选择不显示这个按钮。
3. 在`ShellPage`的`_builtInNavItems`新增这个内置按钮的注册，让不显示这个按钮的设置能够生效。
