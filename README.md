
# Playwright UI Tests

![Tests](https://github.com/Qut77/Store-pytest-playwright/actions/workflows/tests.yml/badge.svg)

Проект по автоматизации UI-тестирования на Python с использованием Playwright и Pytest.

## Стек технологий

- Python 3.13
- Pytest
- Playwright
- Page Object Model (POM)
- GitHub Actions (CI)

---

## Структура проекта

```text
project/
│
├── pages/
│   ├── base_page.py
│   └── login_page.py
│
├── tests/
│   └── ui/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── conftest.py
├── pytest.ini
└── requirements.txt
````

---

## Установка проекта

Клонировать репозиторий:

```bash
git clone https://github.com/Qut77/Store-pytest-playwright.git
cd Store-pytest-playwright
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Установить браузеры Playwright:

```bash
playwright install
```

---

## Запуск тестов

Запуск всех тестов:

```bash
pytest
```

Запуск только UI тестов:

```bash
pytest tests/ui -v
```

---

## CI/CD

Проект использует GitHub Actions для автоматического запуска тестов при:

* push

---

## Реализовано

* UI тесты на Playwright
* Архитектура Page Object Model
* Pytest fixtures
* GitHub Actions CI

---

## Планы по развитию проекта

В дальнейшем планируется добавить:

* API тестирование
* Allure отчёты
* Параметризацию тестов
* Кроссбраузерное тестирование
* Docker
* Test data management
* Faker
* Скриншоты и trace при падениях тестов

```
