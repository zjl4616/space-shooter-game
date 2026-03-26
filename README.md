# 🚀 Space Shooter Game

一个使用Python和Pygame开发的2D太空射击游戏。玩家控制飞船，射击敌人获得分数，同时避免碰撞。

![游戏截图](https://img.shields.io/badge/Game-2D%20Shooter-blue)
![Python](https://img.shields.io/badge/Python-3.6%2B-green)
![Pygame](https://img.shields.io/badge/Pygame-2.5.2-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎮 游戏演示

```
太空射击游戏启动中...
游戏控制:
  - W/A/S/D 或方向键: 移动飞船
  - 空格键: 射击
  - R键: 重新开始游戏

游戏目标:
  - 射击红色敌人获得分数
  - 避免敌人碰撞和逃脱
  - 生命值降到0游戏结束
```

## ✨ 功能特性

### 🎯 核心功能
- **玩家控制**：8方向移动 + 射击系统
- **敌人系统**：自动生成 + 随机移动
- **碰撞检测**：子弹vs敌人，玩家vs敌人
- **游戏机制**：生命值管理 + 得分系统 + 难度递增

### 🎨 视觉效果
- 动态星空背景
- 彩色游戏对象（飞船、敌人、子弹）
- 实时UI显示（分数、生命值）
- 游戏结束画面

### ⚙️ 技术特性
- 面向对象设计
- 模块化代码结构
- 可配置的游戏参数
- 完善的错误处理

## 🚀 快速开始

### 系统要求
- Python 3.6+
- Pygame 2.0+
- 支持800×600分辨率的显示器

### 安装步骤

1. **克隆仓库**
```bash
git clone https://github.com/zjl4616/space-shooter-game.git
cd space-shooter-game
```

2. **安装依赖**
```bash
# Ubuntu/Debian
sudo apt-get install python3-pygame

# macOS
brew install pygame

# Windows
pip install pygame

# 通用方法
pip3 install pygame
```

3. **运行游戏**
```bash
# 方法1：直接运行
python3 space_shooter.py

# 方法2：使用启动脚本（Linux/macOS）
chmod +x run_game.sh
./run_game.sh
```

## 🎮 游戏控制

| 按键 | 功能 | 说明 |
|------|------|------|
| **W / ↑** | 向上移动 | 飞船向上移动 |
| **A / ←** | 向左移动 | 飞船向左移动 |
| **S / ↓** | 向下移动 | 飞船向下移动 |
| **D / →** | 向右移动 | 飞船向右移动 |
| **空格键** | 发射子弹 | 向敌人射击 |
| **R键** | 重新开始 | 游戏结束后重新开始 |

## 📊 游戏规则

### 得分规则
- ✅ **击中敌人**：+10分
- ❌ **敌人逃脱**：-5生命值
- 💥 **与敌人碰撞**：-20生命值

### 难度系统
- 初始敌人生成频率：60帧/敌
- 每获得10分，生成频率减少1帧
- 最高难度：30帧/敌

### 胜利条件
- 尽可能获得高分
- 避免生命值降至0
- 挑战自己的极限

## 🏗️ 项目结构

```
space-shooter-game/
├── space_shooter.py      # 主游戏文件
├── run_game.sh          # 启动脚本
├── game_guide.md        # 详细游戏指南
├── requirements.txt     # Python依赖
├── LICENSE             # MIT许可证
└── README.md           # 项目说明
```

## 🔧 自定义修改

### 调整游戏参数
在 `space_shooter.py` 中修改以下变量：

```python
# 窗口大小
WIDTH, HEIGHT = 800, 600

# 玩家属性
PLAYER_SPEED = 5
PLAYER_HEALTH = 100

# 游戏平衡
ENEMY_HIT_SCORE = 10
ENEMY_ESCAPE_DAMAGE = 5
PLAYER_COLLISION_DAMAGE = 20
```

### 修改外观
```python
# 颜色定义
PLAYER_COLOR = (50, 150, 255)    # 蓝色飞船
ENEMY_COLOR = (255, 50, 50)      # 红色敌人
BULLET_COLOR = (50, 255, 50)     # 绿色子弹
```

## 🧪 测试游戏

### 快速测试
```bash
python3 test_game.py
```

### 手动测试
1. 启动游戏
2. 测试所有控制按键
3. 验证碰撞检测
4. 检查游戏结束逻辑

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

### 贡献方向
- 🎨 改进视觉效果
- 🎵 添加音效和音乐
- 🔧 优化游戏性能
- 🐛 修复已知问题
- 📚 改进文档

## 🐛 故障排除

### 常见问题

**问题1：无法导入Pygame**
```bash
# 解决方案
pip3 install --upgrade pip
pip3 install pygame
```

**问题2：窗口无法显示**
```bash
# 在服务器环境使用虚拟显示
apt-get install xvfb
xvfb-run python3 space_shooter.py
```

**问题3：游戏运行缓慢**
- 降低窗口分辨率
- 减少同时显示的敌人数量
- 关闭不必要的后台程序

### 调试帮助
- 按 `Escape` 键退出游戏
- 控制台会显示游戏状态信息
- 检查Python错误输出

## 📈 开发路线图

- [x] 基础游戏框架
- [x] 玩家控制和射击
- [x] 敌人生成系统
- [x] 碰撞检测
- [ ] 音效系统
- [ ] 多种武器类型
- [ ] 关卡系统
- [ ] 在线排行榜
- [ ] 移动端适配

## 🧑‍💻 开发者

### 核心开发者
- **张金龙** - 项目创建者
- **OpenClaw AI助手** - 代码实现

### 致谢
#### 使用的技术
- [Python](https://www.python.org/) - 编程语言
- [Pygame](https://www.pygame.org/) - 游戏开发库
- [GitHub](https://github.com/) - 代码托管

#### 灵感来源
- 经典太空射击游戏
- Pygame官方示例
- 游戏开发社区

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式

- **GitHub**: [@zjl4616](https://github.com/zjl4616)
- **项目链接**: [https://github.com/zjl4616/space-shooter-game](https://github.com/zjl4616/space-shooter-game)
- **游戏链接**: [https://shooter.1993921.xyz/](https://shooter.1993921.xyz/)

## ⭐️ 支持项目

如果你喜欢这个项目，请：
1. ⭐️ 给个Star
2. 🔗 分享给朋友
3. 🐛 报告问题
4. 💡 提出建议
5. 🔧 贡献代码

---

**快乐游戏，快乐编程！** 🚀

> *"游戏不仅仅是娱乐，更是学习和创造的平台。"*

---

*最后更新: 2026年3月26日*  
*版本: 1.0.0*  
*状态: 🟢 稳定运行*