🧪 Автоматизация UI-тестирования сайта saby.ru

📌 Описание

Этот проект представляет собой решение тестового задания на позицию Программист-тестировщик (разработчик автотестов). В рамках задания автоматизированы два обязательных пользовательских сценария и один дополнительный сценарий.

📂 Структура проекта
```commandline
project/
│
├── pages/                # Page Object-классы
│   ├── base_page.py
│   ├── contacts.py
│   └── download.py
│
├── tests/                # Тестовые сценарии
│   ├── test_first_scenario.py
│   ├── test_second_scenario.py
│   └── test_third_scenario.py
│
├── services/             # Утилиты и вспомогательные методы
│   └── static_methods.py
│
├── conftest.py           # Фикстуры, настройки драйвера
└── README.md
```


✅ Обязательные сценарии
1. Проверка баннера «Тензор» на странице Контакты
- Открыть https://saby.ru

- Перейти в раздел Контакты

- Найти баннер «Тензор», кликнуть по нему

- Проверить, что открылась страница https://tensor.ru

- Убедиться в наличии блока «Сила в людях»

- Перейти в Подробнее, убедиться в открытии https://tensor.ru/about

- В блоке Работаем, убедиться, что изображения в хронологии имеют одинаковые ширину и высоту

2. Проверка определения и смены региона
Перейти в раздел Контакты

- Проверить, что определён регион (например: Ярославская область)

- Убедиться в наличии списка партнёров

- Сменить регион на Камчатский край

- Убедиться, что:
регион сменился
обновился список партнёров
изменились URL и title страницы

🔁 Дополнительный сценарий (по желанию)
- Перейти на https://saby.ru

- В подвале сайта нажать Скачать локальные версии

- Скачать веб-установщик СБИС Плагина для Windows

- Убедиться, что файл скачался

- Сравнить фактический размер файла в МБ с указанным на странице


🧑‍💻 Автор
- Кэш, драйверы и виртуальные окружения не добавляются в репозиторий
- Решение выполнено как часть тестового задания на позицию программиста-тестировщика.
- Все замечания и предложения приветствуются.
