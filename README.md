```
  ____        _ _     _ ______     _ 
 |  _ \      (_) |   | |___  /    (_)
 | |_) |_   _ _| | __| |  / / _ __ _ 
 |  _ <| | | | | |/ _` | / / | '__| |
 | |_) | |_| | | | (_| |/ /__| |  | |
 |____/ \__,_|_|_|\__,_/_____|_|  |_|
 
 BuildZri - A minimal build automation tool for C++
```

Most C++ build automation tools come with a bit complex syntax and make simple projects complex. As a result, C++ programmers often try to write shell scripts for compilation, but then they have to maintain multiple scripts for each platform.

BuildZri is a minimal cross-platform C++ build automation tool written in Python. It comes with a simple JSON-based configuration file with the features you need.

Please check the [BuildZri documentation](https://codezri.org/docs/buildzri/intro) for more details.

## Features

- Minimal JSON-based configuration
- Supports, GNU C++, Clang, and MSVC compilers
- Written in Python, works on any popular OS
- Built for both developers and CI/CD servers
- No installation required, it comes as a simple script


## Example build configuration

```json
{
    "std": "c++17",
    "name": "BuildZri Sample",
    "version": "1.0.1",
    "output": "./bin/bzsample-${BZ_OS}_${BZ_ARCH}",
    "include": {
        "*": [
            "."
        ]
    },
    "source": {
        "*": [
            "*.cpp",
            "add/*.cpp",
            "subtract/*.cpp"
        ],
        "linux": [
            "platform/linux.cpp"
        ]
    },
    "definitions": {
        "*": [
            "BZ_TESTV=1",
            "BZ_PROJ_VERSION=\\\"${BZ_VERSION}\\\""
        ]
    },
    "options": {
        "linux": [
            "-Os"
        ],
        "darwin": [
            "-Os"
        ],
        "windows": [
            "/EHsc",
            "/Os",
            "/link"
        ]
    }
}
```

The above sample configuration generates the following binaries:

- `./bin/bzsample-linux_x64` on x64 GNU/Linux machines
- `./bin/bzsample-mac_x64` on x64/arm64 macOS machines
- `./bin/bzsample-win_x64.exe` on x64 Windows machines

This repository contains a simple C++ project that uses BuildZri as the build automation tool.

## License

[MIT](LICENSE)
