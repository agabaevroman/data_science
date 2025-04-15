
# 🎯 Проект 0: Угадай число

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Numpy](https://img.shields.io/badge/Library-numpy-informational)
![Game](https://img.shields.io/badge/Game-Guessing-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Описание проекта
Учебный проект на Python, в котором реализована игра **«Угадай число»** двумя способами:
- 👤 Вручную — пользователь вводит число с подсказками.
- 🤖 Автоматически — алгоритм сам подбирает число, включая реализацию бинарного поиска.

---

## 💡 Какой кейс решаем?
Проект демонстрирует:
- основы работы с циклами, условиями и функциями;
- использование библиотек `numpy` и `matplotlib`;
- сравнение эффективности разных стратегий угадывания;
- визуализацию данных.

---

## 📊 Краткая информация о данных
- Число выбирается случайно в диапазоне от 1 до 100.
- Алгоритмы тестируются на **1000 случайных чисел**.
- Метрика — **среднее количество попыток до угадывания**.

---

## 🛠️ Этапы работы над проектом

### 1. Ручная игра
Пользователь вводит числа, а программа подсказывает: больше или меньше.

### 2. Рандомный алгоритм
Алгоритм угадывает случайным образом. Средний результат: **~99.8 попыток**.

### 3. Бинарный поиск
Улучшенный алгоритм с отсечением половины интервала. Средний результат: **~5.9 попытки**.

---

## 📈 Результаты

| Алгоритм         | Среднее | Макс. | Мин. |
|------------------|---------|-------|------|
| 🎲 Random         | 99.78   | 854   | 1    |
| 🧠 Binary Search | 5.86    | 7     | 1    |

---

## 📉 Визуализация

![График распределения попыток](attempts_distribution.png)

---

## 📎 Файлы в репозитории

| Файл | Описание |
|------|----------|
| [`guessing_game.py`](https://github.com/agabaevroman/data_science/blob/main/project_0/guessing_game.py) | Ручная игра |
| [`auto_guessing_game.py`](https://github.com/agabaevroman/data_science/blob/main/project_0/auto_guessing_game.py) | Автоматический рандомный подбор |
| [`smart_guessing_game.py`](https://github.com/agabaevroman/data_science/blob/main/project_0/smart_guessing_game.py) | Умный алгоритм + график |
| [`attempts_distribution.png`](https://github.com/agabaevroman/data_science/blob/main/project_0/attempts_distribution.png) | График сравнения алгоритмов |
| [`requirements.txt`](https://github.com/agabaevroman/data_science/blob/main/project_0/requirements.txt) | Версии библиотек |
