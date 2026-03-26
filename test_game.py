#!/usr/bin/env python3
"""
快速测试游戏是否能正常启动
"""
import subprocess
import time
import signal
import sys

def test_game():
    print("正在测试太空射击游戏...")
    
    try:
        # 启动游戏进程
        proc = subprocess.Popen(
            [sys.executable, "space_shooter.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        print("游戏进程已启动，等待3秒...")
        time.sleep(3)
        
        # 发送退出信号
        proc.send_signal(signal.SIGINT)
        
        # 等待进程结束
        stdout, stderr = proc.communicate(timeout=5)
        
        if proc.returncode == 0 or proc.returncode == -2:  # -2 通常是Ctrl+C
            print("✅ 游戏测试成功！游戏可以正常启动和退出。")
            print("\n游戏输出:")
            print(stdout[:500] + "..." if len(stdout) > 500 else stdout)
        else:
            print(f"❌ 游戏进程异常退出，返回码: {proc.returncode}")
            if stderr:
                print("错误信息:")
                print(stderr[:500])
                
    except subprocess.TimeoutExpired:
        print("❌ 游戏进程超时")
        proc.kill()
    except Exception as e:
        print(f"❌ 测试过程中发生错误: {e}")

if __name__ == "__main__":
    test_game()