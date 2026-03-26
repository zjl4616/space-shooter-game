#!/bin/bash

echo "================================================"
echo "     太空射击游戏 - 启动脚本"
echo "================================================"
echo ""
echo "检查Python和Pygame环境..."

# 检查Python版本
python3 --version

# 检查Pygame安装
python3 -c "import pygame; print('✓ Pygame版本:', pygame.version.ver)" || {
    echo "✗ Pygame未安装，正在尝试安装..."
    pip3 install pygame || {
        echo "无法安装Pygame，请手动安装"
        exit 1
    }
}

echo ""
echo "游戏信息:"
echo "  - 窗口尺寸: 800x600"
echo "  - 控制方式: 键盘"
echo "  - 游戏类型: 2D太空射击"
echo ""
echo "游戏控制:"
echo "  W/A/S/D 或方向键: 移动飞船"
echo "  空格键: 射击"
echo "  R键: 重新开始游戏"
echo ""
echo "游戏目标:"
echo "  - 射击红色敌人获得分数"
echo "  - 避免敌人碰撞和逃脱"
echo "  - 生命值降到0游戏结束"
echo ""
echo "按 Enter 键启动游戏..."
read

echo "启动游戏中..."
python3 space_shooter.py