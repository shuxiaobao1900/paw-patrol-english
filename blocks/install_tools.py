import subprocess
import sys
print("=" * 60)
print("🔧 安装 GitHub 部署所需工具")
print("=" * 60)
# 检查 Homebrew
print("\n📋 检查 Homebrew...")
result = subprocess.run(['which', 'brew'], capture_output=True, text=True)
if result.returncode != 0:
    print("   ⚠️ Homebrew 未安装")
    print("   正在安装 Homebrew（可能需要几分钟）...")
    install_cmd = '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
    print("\n   请在终端手动运行以下命令安装 Homebrew：")
    print(f"   {install_cmd}")
    print("\n   安装完成后，请回复【继续】")
    utils.set_state(success=False, need_homebrew=True)
    exit(1)
else:
    print("   ✅ Homebrew 已安装")
# 安装 GitHub CLI
print("\n📋 安装 GitHub CLI...")
result = subprocess.run(['brew', 'install', 'gh'], capture_output=True, text=True)
if result.returncode == 0:
    print("   ✅ GitHub CLI 安装成功！")
else:
    if 'already installed' in result.stderr or 'already installed' in result.stdout:
        print("   ✅ GitHub CLI 已安装")
    else:
        print(f"   ⚠️ 安装结果: {result.stderr}")
# 验证安装
print("\n📋 验证安装...")
result = subprocess.run(['gh', '--version'], capture_output=True, text=True)
if result.returncode == 0:
    print(f"   ✅ {result.stdout.strip().split()[0]} 已就绪")
    print("\n" + "=" * 60)
    print("✅ 工具安装完成！")
    print("=" * 60)
    print("\n接下来需要登录 GitHub，请按以下步骤操作：")
    print("\n1️⃣ 在终端运行命令：gh auth login")
    print("2️⃣ 选择 GitHub.com")
    print("3️⃣ 选择 HTTPS")
    print("4️⃣ 选择 Login with a web browser")
    print("5️⃣ 按提示在浏览器中完成授权")
    print("\n完成登录后，请回复【继续】，我将帮您完成部署！")
    print("=" * 60)
    utils.set_state(success=True, need_login=True)
else:
    print("   ❌ 安装验证失败")
    utils.set_state(success=False, error="安装验证失败")