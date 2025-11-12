---
order: 2
---

# 插件项目结构

在插件解决方案（`.sln` 文件）中，通常包含两个项目（project）：

1.  **应用公开库 (Git Submodule)**: 这是主项目 (PotatoVN 应用本体) 的一部分，通过 `git submodule` 的方式引入。
2.  **插件本体**: 这是你编写插件代码的核心项目。

## 应用公开库 (`GalgameManager.WinApp.Base`)

插件本体项目依赖于应用公开库中的 `GalgameManager.WinApp.Base` 项目。这个项目至关重要，因为它定义了：

*   **基础模型**: 如游戏类 ([`Galgame.cs`](PotatoVN/GalgameManager.WinApp.Base/Models/Galgame.cs))、游戏库类 ([`GalgameSourceBase.cs`](PotatoVN/GalgameManager.WinApp.Base/Models/Sources/GalgameSourceBase.cs)) 等。
*   **功能接口**: 以接口形式定义了插件能够注入的各种功能。
*   **应用 API**: 定义了应用本体暴露给插件调用的 API。

**重要提示**:
*   在任何时候，你都 **不应该** 编辑 `GalgameManager.WinApp.Base` 项目中的任何内容。
*   虽然 PotatoVN 会尽可能保证插件的兼容性，但我们仍然建议插件开发者定期通过 `git submodule update --remote` 命令获取最新的 `WinApp.Base`，以避免潜在的兼容性问题。

## 插件本体

在插件本体项目中：

*   **插件主类**: 必须包含一个插件主类（如此模板中的 [`Plugin.cs`](PotatoVN.App.PluginBase/Plugin.cs)），这个类 **至少** 要实现 `IPlugin` 接口，以表明它是一个插件。
*   **功能实现**: 如果插件希望实现其他功能，请实现公开库中定义的各种功能接口。例如：
    *   实现 `IParserProvider` 接口表示插件能提供一个游戏数据搜刮器。
    *   实现 `IPluginSetting` 接口表示插件能提供一个设置 UI，应用会将其展示在插件管理界面（详见第五节）。
*   **预设文件**: 项目中包含一些预设的 UI 控件（位于 `Controls/Prefabs` 文件夹下）以及 UI 注入所需的基础类（如 [`XamlResourceLocatorFactory.cs`](PotatoVN.App.PluginBase/XamlResourceLocatorFactory.cs)）。

理论上，要让插件工作起来，只需要一个实现了 `IPlugin` 接口的主类即可。但为了更好的可维护性，我们强烈推荐你后续阅读下面的小节，了解插件开发的最佳实践。

## 插件开发最佳实践

*本节内容待补充。*