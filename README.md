# 💝 爱的祝福 - Love Message

一个浪漫温馨的祝福弹窗程序，送给你最在意的人 ✨

## 🎁 介绍

这是一个精心制作的祝福程序，会在屏幕上随机弹出温馨的祝福语，配上美丽的渐变色彩和动画效果。

**特点：**
- 💕 可爱的心形图标
- 🎨 10种精选渐变配色
- ✨ 优雅的淡入淡出动画
- 📱 支持手机和电脑浏览器
- 🎮 可暂停、清空、自定义配置

## 🚀 使用方法

### 方法一：直接访问（推荐）

部署到 GitHub Pages 后，你的朋友可以直接通过链接访问！

**步骤：**
1. 将代码上传到 GitHub 仓库
2. 在仓库设置中开启 GitHub Pages
3. 分享链接给朋友：`https://lifei121.github.io/love_xiaoxiao/love_xiaoxiao.html`

### 方法二：本地使用

1. 下载 `love.html` 文件
2. 双击打开（会在浏览器中运行）
3. 尽情享受祝福吧！

### 方法三：Python版本

如果你想要桌面应用版本，可以使用 `love.py`：

```bash
python love.py
```

## ⚙️ 自定义配置

你可以修改 `love.html` 中的配置区域：

```javascript
// 修改提示语
const messages = [
    "好好爱自己", "保持好心情", "金榜题名", 
    // 添加你自己的祝福语...
];

// 修改弹窗参数
const CONFIG = {
    popupInterval: 200,      // 弹窗间隔（毫秒）
    maxPopups: 100,          // 最大弹窗数
    popupLifetime: 10000,    // 弹窗生存时间（毫秒）
};
```

## 📦 文件说明

- `love.html` - HTML网页版本（推荐）
- `love.py` - Python桌面版本
- `快速打包.bat` - 自动打包Python版本为exe
- `打包说明.txt` - 详细打包说明

## 🎮 控制说明

- **暂停/继续按钮** - 控制弹窗生成
- **清空按钮** - 清除所有当前弹窗
- **点击弹窗** - 关闭单个弹窗
- **✕ 按钮** - 关闭单个弹窗

## 📱 兼容性

- ✅ Chrome / Edge
- ✅ Firefox
- ✅ Safari
- ✅ 手机浏览器
- ✅ 平板电脑

## 💡 部署到 GitHub Pages

### 快速部署步骤：

1. **创建 GitHub 仓库**
   - 登录 GitHub
   - 点击 New Repository
   - 输入仓库名（如：love-message）

2. **上传文件**
   - 上传 `love.html` 和 `README.md`

3. **开启 GitHub Pages**
   - 进入仓库 Settings
   - 找到 Pages 选项
   - Source 选择 main 分支
   - 保存

4. **访问你的网站**
   - 等待几分钟
   - 访问：`https://你的用户名.github.io/仓库名/love.html`

5. **分享给朋友**
   - 把链接发给 TA
   - 或者生成二维码让 TA 扫描

## 🎨 效果预览

程序运行后会显示：
- 随机位置的彩色弹窗
- 带有心形图标的温馨提示
- 平滑的动画效果
- 美观的渐变背景

## ❤️ 适用场景

- 送给朋友的生日礼物
- 表白神器
- 纪念日惊喜
- 考试加油鼓励
- 日常温馨问候

## 📝 许可证

MIT License - 随意使用、修改和分享！

## 🌟 Star

如果你喜欢这个项目，请给个 Star ⭐️

---

**制作不易，用心制作 💝**

如有问题或建议，欢迎提 Issue 或 PR！

