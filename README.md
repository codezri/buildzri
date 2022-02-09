# buildzri
A minimalistic build automation tool

```json
{
  "sourceFiles": {
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
  "flags": {
    "*": [],
    "linux": ["-DTEST_OPTION=1"]
  },
  "include": ["."],
  "output": "neutralino_${BZ_OS}-${BZ_ARCH}"
}
```
