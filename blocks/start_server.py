import http.server
import socketserver
import os
import socket
# 获取本机 IP 地址
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"
# 切换到工作目录
os.chdir("/Users/btt/aipywork/CXEbTdw7Fvi2jCCYdUs9c/CZMUn4piLZVxKt55xCPUd")
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
print("=" * 50)
print("🐾 汪汪队英语乐园 - 本地服务器")
print("=" * 50)
print(f"\n📱 手机访问地址：")
print(f"   http://{get_local_ip()}:{PORT}")
print(f"\n💻 电脑访问地址：")
print(f"   http://localhost:{PORT}")
print(f"\n📂 服务目录：{os.getcwd()}")
print("\n⚠️  按 Ctrl+C 停止服务器")
print("=" * 50)
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()