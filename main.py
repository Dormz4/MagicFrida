import platform

import fire as fire

os_name = platform.system().lower()

def help():
    if os_name == 'darwin':
        print("操作系统:"+os_name+",魔改frida自定义编译:\n"+
              "/* gum */\n"
              "gum-macos                  Build for macOS\n" +
              "gum-ios                    Build for iOS\n" +
              "gum-android-x86            Build for Android/x86\n" +
              "gum-android-x86_64         Build for Android/x86-64\n" +
              "gum-android-arm            Build for Android/arm\n" +
              "gum-android-arm64          Build for Android/arm64\n" +
              "check-gum-macos            Run tests for macOS\n" +
              "\n" +
              "/* core */\n" +
              "core-macos                 Build for macOS" +
              "core-ios                   Build for iOS\n" +
              "core-android-x86           Build for Android/x86\n" +
              "core-android-x86_64        Build for Android/x86-64\n" +
              "core-android-arm           Build for Android/arm\n" +
              "core-android-arm64         Build for Android/arm64\n" +
              "check-core-macos           Run tests for macOS\n" +
              "\n" +
              "/* gadget */\n" +
              "gadget-macos               Build for macOS\n" +
              "gadget-ios                 Build for iOS\n" +
              "\n" +
              "/* python */\n" +
              "python-macos               Build Python bindings for macOS\n" +
              "check-python-macos         Test Python bindings for macOS\n" +
              "\n" +
              "/* node */\n" +
              "node-macos                 Build Node.js bindings for macOS\n" +
              "check-node-macos           Test Node.js bindings for macOS\n" +
              "\n" +
              "/* tools */\n" +
              "tools-macos                Build CLI tools for macOS\n" +
              "check-tools-macos          Test CLI tools for macOS\n"
              )
    if os_name == 'linux':
        print("操作系统:"+os_name+",魔改frida自定义编译:"
              "")
    if os_name == 'windows':
        print("操作系统:"+os_name+",魔改frida自定义编译:"
              "")




if __name__ == '__main__':
    # 进行编译
    fire.Fire()
    print()
