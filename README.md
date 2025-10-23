### Hexlet tests and linter status:
[![Actions Status](https://github.com/anisimV/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/anisimV/python-project-49/actions)


![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=anisimV_python-project-49&metric=alert_status)
![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=anisimV_python-project-49&metric=sqale_rating)
![Reliability](https://sonarcloud.io/api/project_badges/measure?project=anisimV_python-project-49&metric=reliability_rating)

# 🎮 Brain Games

**Brain Games** — это набор из пяти консольных логических игр для тренировки ума и внимания.  
Проект реализован в рамках курса [Hexlet Python Developer].

Игры запускаются прямо из терминала и предлагают пользователю дать **три правильных ответа подряд**, чтобы выиграть.

---

## 🧩 Список игр

| Команда | Описание |
|----------|-----------|
| `brain-even` | Проверка: чётное ли число |
| `brain-calc` | Вычисление математического выражения |
| `brain-gcd` | Поиск наибольшего общего делителя |
| `brain-progression` | Поиск пропущенного числа в прогрессии |
| `brain-prime` | Определение, является ли число простым |

---

## ⚙️ Минимальные требования

- **Python** ≥ 3.14  
- **uv** — современная альтернатива `pip` и `venv`  
  Установка:

  ```bash
  pip install uv
  ```

---

## 🚀 Установка и запуск

### 1️⃣ Клонируйте репозиторий
```bash
git clone https://github.com/anisimV/python-project-49.git
cd python-project-49
```

### 2️⃣ Установите зависимости
```bash
uv sync
```

### 3️⃣ Соберите и установите пакет
```bash
make build
make package-install
```

### 4️⃣ Проверьте установку
```bash
brain-games
```

### 5️⃣ Запускайте любую игру
```bash
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
```

> ⚠️ После установки через `make package-install`  
> игры запускаются **без** `uv run` — просто `brain-calc`, `brain-even` и т.д.

---

## 🧰 Команды Makefile

| Команда | Описание |
|----------|-----------|
| `make install` | Устанавливает зависимости (аналог `uv sync`) |
| `make lint` | Проверяет код линтером **Ruff** |
| `make build` | Собирает дистрибутив пакета (`dist/*.whl`) |
| `make package-install` | Устанавливает пакет локально |
| `make check` | Проверяет код и запускает тесты (если есть) |

---

## 🧠 Пример игрового процесса

```bash
$ brain-even
Welcome to the Brain Games!
May I have your name? Bill
Hello, Bill!
Answer "yes" if the number is even, otherwise answer "no".
Question: 7
Your answer: no
Correct!
Question: 10
Your answer: yes
Correct!
Question: 3
Your answer: no
Correct!
Congratulations, Bill!
```

---

## 📼 Asciinema (демонстрация)

🎥 Пример запуска игр и успешного/неудачного исхода будет добавлен в ближайшее время.

---


💡 Автор: [anisimV](https://github.com/anisimV)  
