Форматирование с учетом flake8. Создать папку .vscode и в ней файл settings.json:
```
{
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length=100"],
    "editor.formatOnSave": true,
}
