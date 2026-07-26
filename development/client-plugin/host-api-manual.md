---
order: 4
---

# PotatoVN API手册

## 游戏与本地安装

`IPotatoVnApi.GetAllGames()` 返回逻辑游戏快照。一个 `Galgame` 可以同时关联多个
LocalFolder 或 Steam 安装；游戏元数据与游玩记录属于逻辑游戏，路径和启动配置属于安装实例。

`AddGameInstallation(path)` 在识别到已有逻辑游戏时会把路径关联为新的安装，而不会创建重复游戏。
同一个游戏在同一个游戏库中最多关联一个路径。

`Galgame.LocalPath`、`ExePath` 等废弃属性只代表当前首选安装，新插件不应再使用。
安装实例接口已经直接包含在当前版本的 `IPotatoVnApi` 中：

```csharp
IReadOnlyList<GameInstallationInfo> installations =
    hostApi.GetGameInstallations(game);

GameInstallationInfo? target = installations.FirstOrDefault();
if (target is not null)
    await hostApi.LaunchGameAsync(game, target.EntryId);
```

`GameInstallationInfo` 是只读快照，包含安装 ID、源 ID/类型、库名、路径、可用状态及是否首选。
安装路径和启动配置仅保存在本机及数据导出中，不会上传到 PotatoVN 同步服务器。
旧版 `AddGame(path)` 已标记废弃，请改用 `AddGameInstallation(path)`。