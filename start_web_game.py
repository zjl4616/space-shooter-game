#!/usr/bin/env python3
"""
太空射击游戏 - 网页版启动器

这个脚本会启动一个简单的HTTP服务器来运行HTML5游戏。
可以直接在浏览器中打开游戏网页。
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import time
import threading

class GameHTTPServer(http.server.SimpleHTTPRequestHandler):
    """自定义HTTP服务器，添加跨域支持"""
    
    def do_GET(self):
        # 设置响应头
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.end_headers()
        
        # 处理根路径
        if self.path == '/' or self.path == '/index.html':
            self.path = '/space_shooter_web.html'
        
        # 调用父类方法处理文件
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
    def log_message(self, format, *args):
        """自定义日志格式"""
        print(f"[HTTP Server] {format % args}")

def start_server(port=8000):
    """启动HTTP服务器"""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    handler = GameHTTPServer
    httpd = socketserver.TCPServer(("", port), handler)
    
    print("\n" + "="*60)
    print("🚀 太空射击游戏 - 网页版服务器")
    print("="*60)
    print(f"📂 工作目录: {os.getcwd()}")
    print(f"🌐 服务器地址: http://localhost:{port}")
    print(f"🕹️ 游戏文件: space_shooter_web.html")
    print("="*60)
    print("\n🎮 游戏信息:")
    print("  - 游戏类型: 2D太空射击")
    print("  - 控制方式: 键盘（WASD/方向键 + 空格）")
    print("  - 开发技术: HTML5 Canvas + JavaScript")
    print("\n🎯 游戏目标:")
    print("  - 射击红色敌人获得分数")
    print("  - 避免敌人碰撞和逃脱")
    print("  - 生命值降到0游戏结束")
    print("\n⌨️ 游戏控制:")
    print("  W / ↑ : 向上移动")
    print("  A / ← : 向左移动")
    print("  S / ↓ : 向下移动")
    print("  D / → : 向右移动")
    print("  空格键 : 发射子弹")
    print("  R键 : 重新开始游戏")
    print("\n⚠️  按 Ctrl+C 停止服务器")
    print("="*60)
    
    # 尝试自动打开浏览器
    def open_browser():
        time.sleep(1.5)
        webbrowser.open(f"http://localhost:{port}")
    
    threading.Thread(target=open_browser, daemon=True).start()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 服务器已停止")
        httpd.shutdown()
        sys.exit(0)

def main():
    """主函数"""
    print("太空射击游戏 - 网页版启动中...")
    print(f"当前Python版本: {sys.version}")
    
    # 检查游戏文件是否存在
    game_file = "space_shooter_web.html"
    if not os.path.exists(game_file):
        print(f"❌ 错误: 游戏文件 '{game_file}' 不存在！")
        print("请确保以下文件存在:")
        print("  - space_shooter_web.html (HTML5游戏)")
        print("  - start_web_game.py (本启动器)")
        return 1
    
    # 获取可用端口
    port = 8000
    max_port = 8010
    
    while port <= max_port:
        try:
            start_server(port)
            break
        except OSError as e:
            if "Address already in use" in str(e):
                print(f"⚠️  端口 {port} 已被占用，尝试端口 {port+1}...")
                port += 1
            else:
                print(f"❌ 服务器启动错误: {e}")
                return 1
    else:
        print(f"❌ 无法找到可用端口 ({port}-{max_port})")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)