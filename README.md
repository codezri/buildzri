# buildzri
A minimalistic build automation tool

```json
{
  "cppTarget": 17,
  "output": "neutralino_${BZ_OS}-${BZ_ARCH}",
  "include": ["."],
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
  "options": {
    "*": [],
    "linux": ["-no-pie", "-pthread"]
  },
  "definitions": [
    "TESTV=1"
  ]
}
```
