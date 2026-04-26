---
order: 3
---

# 调用PotatoVN API

调用 PotatoVN 应用本体提供的功能主要通过 `HostApi` 实现。

当你的插件被加载和启用时，PotatoVN 会调用你的插件主类（实现了 `IPlugin` 接口的类）中的 `InitializeAsync(IPotatoVnApi hostApi)` 方法。

这个方法会传入一个 `IPotatoVnApi` 接口的实例，它就是 `HostApi`。你需要在你的插件代码中找到一个合适的位置（例如，一个静态字段或单例属性）来保存这个 `hostApi` 对象的引用，以便在插件的生命周期内随时调用其提供的方法。

```csharp
// In your Plugin.cs
public class Plugin : IPlugin
{
    public static IPotatoVnApi? HostApi;

    public async Task InitializeAsync(IPotatoVnApi hostApi)
    {
        HostApi = hostApi;
        // Other initialization logic...
        await Task.CompletedTask;
    }
    
    // ... other methods
}
```

## 页面跳转

`HostApi` 现在支持两种导航方式：

- `NavigateTo(PageEnum page, object? parameter = null)`：跳转到 PotatoVN 内置页面。
- `NavigateTo(Type pageType, string? title = null, object? parameter = null, bool clearNavigation = false)`：跳转到当前插件自己的 `Page`。

例如：

```csharp
HostApi?.NavigateTo(typeof(MyPluginPage), title: "My Plugin");
```

注意：

1. `pageType` 必须是当前插件程序集里的 `Microsoft.UI.Xaml.Controls.Page` 类型。
2. 如果不传 `title`，宿主会默认使用插件名作为页面标题。
3. 如果你的插件页面使用 XAML，仍然要遵循 [插件UI](/development/client-plugin/ui.md) 中的 `XamlResourceLocatorFactory.PluginControlInit()` 约定。
