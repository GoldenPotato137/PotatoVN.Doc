---
order: 7
---

# 各UI接口介绍

插件 UI 接口位于 `GalgameManager.WinApp.Base.Contracts.PluginUi` 命名空间。返回的 UI 会在主程序 UI 线程中创建，使用 XAML 编写插件控件时请参考模板中的 `XamlResourceLocatorFactory.PluginControlInit()` 初始化方式。

## IPluginSetting

在插件管理页为插件提供设置界面。

```csharp
public interface IPluginSetting
{
    FrameworkElement CreateSettingUi();
}
```

## IPluginAccount

在账号页追加插件账号或登录相关 UI。多个插件可以同时提供账号 UI。

```csharp
public interface IPluginAccount
{
    FrameworkElement CreateAccountUi();
}
```

## IGalgamePage

提供完整自定义游戏详情页。实现该接口后，主程序会使用插件返回的 UI 替换原版游戏详情页主体。

```csharp
public interface IGalgamePage
{
    Task<FrameworkElement> CreateUiAsync(Galgame game);
}
```

## IGalgamePageLeftPanel

在原版游戏详情页左侧面板追加 UI。适合显示游戏简介补充信息、外部资料、插件分析结果等内容。

```csharp
public interface IGalgamePageLeftPanel
{
    Task<FrameworkElement> CreateLeftPanelUiAsync(Galgame game);
}
```

## IGalgamePageRightPanel

在原版游戏详情页右侧面板追加 UI。适合显示状态、操作按钮、同步信息、插件快捷入口等内容。

```csharp
public interface IGalgamePageRightPanel
{
    Task<FrameworkElement> CreateRightPanelUiAsync(Galgame game);
}
```

## IGalgamePageSetting

当插件提供游戏详情页相关设置时实现。用户在游戏详情页点击“自定义页面布局”时，主程序会调用该方法。

```csharp
public interface IGalgamePageSetting
{
    Task SettingAsync();
}
```

如果插件只实现左右面板接口，主程序仍会保留原版布局管理入口；如果同时实现 `IGalgamePage` 和 `IGalgamePageSetting`，该入口会交给插件处理。
