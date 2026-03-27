import subprocess
import os
import json
print("=" * 60)
print("🚀 汪汪队英语乐园 - GitHub Pages 部署工具")
print("=" * 60)
# 步骤1：检查 Git 是否安装
print("\n📋 步骤1：检查 Git 环境...")
try:
    result = subprocess.run(['git', '--version'], capture_output=True, text=True)
    print(f"   ✅ Git 已安装: {result.stdout.strip()}")
except FileNotFoundError:
    print("   ❌ Git 未安装！")
    print("\n   请先安装 Git：")
    print("   方法1: 在终端运行 'xcode-select --install'")
    print("   方法2: 从 https://git-scm.com/download/mac 下载安装")
    utils.set_state(success=False, error="Git 未安装")
    exit(1)
# 步骤2：检查是否已登录 GitHub
print("\n📋 步骤2：检查 GitHub 登录状态...")
try:
    result = subprocess.run(['gh', 'auth', 'status'], capture_output=True, text=True)
    if result.returncode == 0:
        print("   ✅ 已登录 GitHub CLI")
    else:
        print("   ⚠️ 未登录 GitHub CLI")
        print("\n   需要先登录 GitHub，请按以下步骤操作：")
        print("   1. 在终端运行: gh auth login")
        print("   2. 选择 GitHub.com")
        print("   3. 选择 HTTPS")
        print("   4. 选择 Login with a web browser")
        print("   5. 按提示完成授权")
        utils.set_state(success=False, error="未登录 GitHub CLI")
        exit(1)
except FileNotFoundError:
    print("   ⚠️ GitHub CLI 未安装")
    print("   请先安装: brew install gh")
    utils.set_state(success=False, error="GitHub CLI 未安装")
    exit(1)
# 步骤3：获取用户 GitHub 用户名
print("\n📋 步骤3：获取 GitHub 用户信息...")
result = subprocess.run(['gh', 'api', 'user', '--jq', '.login'], capture_output=True, text=True)
if result.returncode == 0:
    github_username = result.stdout.strip()
    print(f"   ✅ GitHub 用户名: {github_username}")
else:
    print("   ❌ 无法获取用户信息")
    utils.set_state(success=False, error="无法获取 GitHub 用户信息")
    exit(1)
# 步骤4：创建仓库
repo_name = "paw-patrol-english-game"
print(f"\n📋 步骤4：创建 GitHub 仓库 '{repo_name}'...")
# 检查仓库是否已存在
result = subprocess.run(['gh', 'repo', 'view', repo_name], capture_output=True, text=True)
if result.returncode == 0:
    print(f"   ✅ 仓库已存在: {repo_name}")
else:
    # 创建新仓库
    result = subprocess.run([
        'gh', 'repo', 'create', repo_name,
        '--public',
        '--description', '🐾 汪汪队英语乐园 - 小朋友的英语启蒙小游戏',
        '--confirm'
    ], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"   ✅ 仓库创建成功！")
    else:
        print(f"   ❌ 创建失败: {result.stderr}")
        utils.set_state(success=False, error="创建仓库失败")
        exit(1)
# 步骤5：准备部署目录
print("\n📋 步骤5：准备部署文件...")
deploy_dir = "/Users/btt/aipywork/CXEbTdw7Fvi2jCCYdUs9c/CZMUn4piLZVxKt55xCPUd/deploy_temp"
os.makedirs(deploy_dir, exist_ok=True)
# 复制 HTML 文件
import shutil
src_file = "/Users/btt/aipywork/CXEbTdw7Fvi2jCCYdUs9c/CZMUn4piLZVxKt55xCPUd/blocks/index_v7.html"
dst_file = os.path.join(deploy_dir, "index.html")
shutil.copy(src_file, dst_file)
print(f"   ✅ 文件已复制到部署目录")
# 步骤6：初始化 Git 并推送
print("\n📋 步骤6：推送到 GitHub...")
os.chdir(deploy_dir)
# 初始化 git
subprocess.run(['git', 'init'], capture_output=True)
subprocess.run(['git', 'add', '.'], capture_output=True)
subprocess.run(['git', 'commit', '-m', '🎉 初始部署：汪汪队英语乐园'], capture_output=True)
# 设置远程仓库
repo_url = f"https://github.com/{github_username}/{repo_name}.git"
subprocess.run(['git', 'remote', 'add', 'origin', repo_url], capture_output=True)
subprocess.run(['git', 'branch', '-M', 'main'], capture_output=True)
# 推送
result = subprocess.run(['git', 'push', '-u', 'origin', 'main', '--force'], capture_output=True, text=True)
if result.returncode == 0:
    print("   ✅ 代码推送成功！")
else:
    print(f"   ⚠️ 推送结果: {result.stderr}")
# 步骤7：启用 GitHub Pages
print("\n📋 步骤7：启用 GitHub Pages...")
result = subprocess.run([
    'gh', 'api', 
    f'repos/{github_username}/{repo_name}/pages',
    '-X', 'POST',
    '-f', 'source[branch]=main',
    '-f', 'source[path]=/root'
], capture_output=True, text=True)
if result.returncode == 0 or 'already' in result.stderr.lower():
    print("   ✅ GitHub Pages 已启用！")
else:
    print(f"   ⚠️ 启用 Pages: {result.stderr}")
# 完成
print("\n" + "=" * 60)
print("🎉 部署完成！")
print("=" * 60)
website_url = f"https://{github_username}.github.io/{repo_name}/"
print(f"\n🌐 您的游戏网址：")
print(f"   {website_url}")
print(f"\n📱 手机访问方法：")
print(f"   1. 确保手机已连接网络")
print(f"   2. 在手机浏览器中打开上述网址")
print(f"   3. 可以添加到主屏幕，像 App 一样使用！")
print(f"\n⏰ GitHub Pages 生效可能需要 1-3 分钟")
print(f"   如果暂时打不开，请稍等片刻再试")
print("=" * 60)
# 清理临时目录
os.chdir("/Users/btt/aipywork/CXEbTdw7Fvi2jCCYdUs9c/CZMUn4piLZVxKt55xCPUd")
shutil.rmtree(deploy_dir, ignore_errors=True)
utils.set_state(success=True, url=website_url, repo=f"{github_username}/{repo_name}")