@echo off
chcp 65001 >nul
echo ═══════════════════════════════════════════════════════════════
echo 💝 Love Message 自动打包脚本
echo ═══════════════════════════════════════════════════════════════
echo.

echo [1/3] 检查 PyInstaller...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller 未安装，正在安装...
    pip install pyinstaller
) else (
    echo ✓ PyInstaller 已安装
)
echo.

echo [2/3] 开始打包程序...
echo 这可能需要几分钟时间，请耐心等待...
pyinstaller --onefile --noconsole --name "爱的祝福" love.py
echo.

if exist "dist\爱的祝福.exe" (
    echo [3/3] ✓ 打包成功！
    echo.
    echo ═══════════════════════════════════════════════════════════════
    echo 🎉 生成的文件位置：
    echo    dist\爱的祝福.exe
    echo.
    echo 💝 现在你可以把这个文件发送给你的朋友了！
    echo ═══════════════════════════════════════════════════════════════
    echo.
    echo 是否打开文件所在位置？
    pause
    explorer dist
) else (
    echo [3/3] ✗ 打包失败
    echo 请查看上方错误信息或参考"打包说明.txt"
    echo.
    pause
)


