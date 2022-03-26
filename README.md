```
  ____        _ _     _ ______     _ 
 |  _ \      (_) |   | |___  /    (_)
 | |_) |_   _ _| | __| |  / / _ __ _ 
 |  _ <| | | | | |/ _` | / / | '__| |
 | |_) | |_| | | | (_| |/ /__| |  | |
 |____/ \__,_|_|_|\__,_/_____|_|  |_|
 
 BuildZri - A minimal build automation tool for C++
```

- Minimal JSON-based configuration
- Supports, GNU C++, Clang, and MSVC compilers
- Written in Python, works on any popular OS
- Built for both developers and CI/CD servers
- No installation required, it comes as a simple script


## Example build configuration

_file: buildzri.config.json_

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
        "windows": [
            "/EHsc"
        ],
        "linux": [
            "-Os"
        ]
    }
}
```

## License

[MIT](LICENSE)
