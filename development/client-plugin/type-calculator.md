---
order: 10
---

# 插件类型计算器

在 `plugin-info.json` 中，`types` 字段是一个 `int32_t` 类型的按位标识值，用于标记插件所属的类型。你可以在下方勾选插件所属的类型，计算器会自动为你生成对应的 `types` 值。

## 计算器

勾选你的插件所属的类型，下方会自动显示 `types` 的值：

<div class="type-calculator">
  <div class="checkbox-group">
    <label><input type="checkbox" value="2" class="type-checkbox" /> Official（这是个官方插件）</label>
    <label><input type="checkbox" value="4" class="type-checkbox" /> Parser（这个插件新增了搜刮器）</label>
    <label><input type="checkbox" value="8" class="type-checkbox" /> Huge（这个插件规模比较大）</label>
    <label><input type="checkbox" value="16" class="type-checkbox" /> Theme（主题插件）</label>
    <label><input type="checkbox" value="32" class="type-checkbox" /> View（这个插件新增/优化了界面）</label>
    <label><input type="checkbox" value="64" class="type-checkbox" /> Utility（这个插件新增/优化了软件功能）</label>
    <label><input type="checkbox" value="128" class="type-checkbox" /> Library（这个插件提供了新的游戏库类别（例如某网盘库））</label>
  </div>
  <div class="result-area">
    <p>计算结果：<code class="result-value">0</code></p>
    <p>在 <code>plugin-info.json</code> 中填写：</p>
    <div class="language-json5"><pre><code>"types": <span class="result-value">0</span></code></pre></div>
  </div>
</div>

<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  const checkboxes = document.querySelectorAll('.type-checkbox')
  const resultValues = document.querySelectorAll('.result-value')

  function updateResult() {
    let total = 0
    checkboxes.forEach(cb => {
      if (cb.checked) {
        total |= parseInt(cb.value)
      }
    })
    resultValues.forEach(el => {
      el.textContent = total.toString()
    })
  }

  checkboxes.forEach(cb => {
    cb.addEventListener('change', updateResult)
  })
})
</script>

<style>
.type-calculator {
  margin-top: 16px;
}

.type-calculator .checkbox-group {
  display: flex;
  flex-direction: column;
  gap: 12px;
  padding: 16px;
  border: 1px solid var(--vp-c-border);
  border-radius: 8px;
  background-color: var(--vp-c-bg-soft);
}

.type-calculator .checkbox-group label {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  cursor: pointer;
}

.type-calculator .checkbox-group input[type="checkbox"] {
  width: 16px;
  height: 16px;
  cursor: pointer;
}

.type-calculator .result-area {
  margin-top: 16px;
  padding: 16px;
  border: 1px solid var(--vp-c-border);
  border-radius: 8px;
  background-color: var(--vp-c-bg-soft);
}

.type-calculator .result-value {
  font-weight: bold;
  color: var(--vp-c-brand-1);
  font-size: 18px;
}
</style>


## 类型定义

| 枚举名 | 值 | 说明 |
| --- | --- | --- |
| All | 0 | 全部（默认值） |
| Official | 2 | 官方插件 |
| Parser | 4 | 搜刮器 |
| Huge | 8 | 大型插件 |
| Theme | 16 | 主题 |
| View | 32 | 界面优化 |
| Utility | 64 | 功能优化 |
| Library | 128 | 库 |