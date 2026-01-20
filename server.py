import http.server
import socketserver
import sys
import os

# 默认端口
DEFAULT_PORT = 8000

def run_server(port):
    """启动服务器"""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    Handler = http.server.SimpleHTTPRequestHandler
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"✅ 服务器启动成功！")
            print(f"📁 服务目录: {os.getcwd()}")
            print(f"🌐 访问地址: http://localhost:{port}")
            print("🛑 按 Ctrl+C 停止服务器\n")
            httpd.serve_forever()
    except OSError as e:
        if "10048" in str(e):
            print(f"⚠️  端口 {port} 被占用，尝试 {port + 1}...")
            run_server(port + 1)  # 自动尝试下一个端口
        else:
            raise e

def main():
    # 获取命令行参数或使用默认端口
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"⚠️  无效的端口号: {sys.argv[1]}，使用默认端口 {DEFAULT_PORT}")
            port = DEFAULT_PORT
    else:
        port = DEFAULT_PORT
    
    run_server(port)

if __name__ == "__main__":
    main()