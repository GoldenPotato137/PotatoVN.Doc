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