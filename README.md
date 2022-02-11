```
  ____        _ _     _ ______     _ 
 |  _ \      (_) |   | |___  /    (_)
 | |_) |_   _ _| | __| |  / / _ __ _ 
 |  _ <| | | | | |/ _` | / / | '__| |
 | |_) | |_| | | | (_| |/ /__| |  | |
 |____/ \__,_|_|_|\__,_/_____|_|  |_|
 
 BuildZri - A minimalistic build automation tool
```

- Minimalist JSON-based configuration
- Supports, GNU C++, Clang, and MSVC compilers
- Written in Python, works on any popular OS
- Built for both developers and CI/CD servers

```json
{
  "cppTarget": 17,
  "output": "neutralino_${BZ_OS}-${BZ_ARCH}",
  "include": ["."],
  "source": {
    "*": [
      "app/.*",
      "os/.*"
    ],
    "linux": [
      "test_linux.cpp"
    ],
    "windows": [
      "test_win.cpp"
    ],
    "darwin": [
      "test_mac.mm"
    ] 
  },
  "options": {
    "*": [],
    "linux": ["-no-pie", "-pthread"]
  },
  "definitions": [
    "TESTV=1"
  ]
}
```
