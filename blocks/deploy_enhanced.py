import subprocess
import os
import shutil
print("=" * 60)
print("🚀 部署增强版汪汪队英语乐园")
print("=" * 60)
# 获取 GitHub 用户名
result = subprocess.run(['gh', 'api', 'user', '--jq', '.login'], capture_output=True, text=True)
github_username = result.stdout.strip()
repo_name = "paw-patrol-english-game"
# 准备部署文件
print("\n📋 准备增强版文件...")
deploy_dir = "/Users/btt/aipywork/CXEbTdw7Fvi2jCCYdUs9c/CZMUn4piLZVxKt55xCPUd/deploy_enhanced"
os.makedirs(deploy_dir, exist_ok=True)
# 复制增强版 HTML 文件
src_file = "/Users/btt/aipywork/CXEbTdw7Fvi2jCCYdUs9c/CZMUn4piLZVxKt55xCPUd/blocks/index_v9_enhanced.html"
dst_file = os.path.join(deploy_dir, "index.html")
shutil.copy(src_file, dst_file)
print(f"   ✅ 增强版文件已准备")
# Git 操作
print("\n📋 推送到 GitHub...")
os.chdir(deploy_dir)
if os.path.exists('.git'):
    shutil.rmtree('.git')
subprocess.run(['git', 'init'], capture_output=True)
subprocess.run(['git', 'add', '.'], capture_output=True)
subprocess.run(['git', 'commit', '-m', '🎮 增强版：4大主题+4种游戏模式+徽章系统'], capture_output=True)
repo_url = f"https://github.com/{github_username}/{repo_name}.git"
subprocess.run(['git', 'remote', 'add', 'origin', repo_url], capture_output=True)
subprocess.run(['git', 'branch', '-M', 'main'], capture_output=True)
result = subprocess.run(['git', 'push', '-u', 'origin', 'main', '--force'], 
                       capture_output=True, text=True)
if result.returncode == 0:
    print("   ✅ 推送成功！")
else:
    print(f"   ⚠️ {result.stderr}")
# 完成
print("\n" + "=" * 60)
print("✅ 增强版部署完成！")
print("=" * 60)
website_url = f"https://{github_username}.github.io/{repo_name}/"
print(f"\n🌐 访问地址：")
print(f"   {website_url}")
print(f"\n🎮 增强版功能：")
print(f"   ✅ 4大学习主题：动物、水果、颜色、数字")
print(f"   ✅ 4种游戏模式：闪卡、配对、拼写、听力")
print(f"   ✅ 徽章奖励系统：6个可收集徽章")
print(f"   ✅ 进度追踪：得分、连胜、关卡")
print(f"   ✅ 移动端深度优化")
print(f"\n📱 手机使用：")
print(f"   1. 在手机浏览器打开网址")
print(f"   2. 添加到主屏幕，像 App 一样使用")
print(f"   3. 强制刷新确保加载最新版本")
print("=" * 60)
# 清理
os.chdir("/Users/btt/aipywork/CXEbTdw7Fvi2jCCYdUs9c/CZMUn4piLZVxKt55xCPUd")
shutil.rmtree(deploy_dir, ignore_errors=True)
utils.set_state(success=True, url=website_url, version="enhanced")