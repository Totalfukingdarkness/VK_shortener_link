# VK_shortener_link

Данная программа позволяет удобно управлять ссылками VK и отслеживать статистику переходов.

### Зависимости

- Python3 должен быть установлен
- Затем используйте `pip` для установки зависимостей:
```
pip install -r requirements.txt
```

### Переменные окружения

- VK_API_TOKEN
1. Расположите файл `.env` в папке проекта рядом с файлом `main.py`.
2. Файл `.env` должен содержать сервисный ключ доступа.

Пример содержимого файла `.env`:

```
VK_API_TOKEN='7dsa5hfd676c1280676c12806b075fd447c776c176c128061fc60e9aaebd00bda8ddjasnwmsa'
```

### Запуск

- Для сокращеного варианта перейдайте полную ссылку на сокращение:
```
pynton main.py https://www.example.com
```
Пример вывода в консоль:

<img width="263" height="33" alt="image" src="https://github.com/user-attachments/assets/c090ea43-ab40-4871-8dbf-4248d85ce4fc" />

-Для получения информации о колличестве переходов используйте:
```
main.py https://vk.cc/6YpJQE
```
Пример вывода в консоль:

<img width="406" height="32" alt="image" src="https://github.com/user-attachments/assets/76e860bf-1158-4f25-91f0-f579e9e22b60" />


