from datetime import datetime

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Виконано" if self.is_completed else "Не виконано"
        return f"Назва: {self.title}, Опис: {self.description}, Дедлайн: {self.deadline}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_title):
        self.tasks = [task for task in self.tasks if task.title != task_title]

    def mark_task_as_completed(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.mark_as_completed()
                break

    def list_tasks(self):
        if not self.tasks:
            print("Немає завдань.")
        else:
            for task in self.tasks:
                print(task)

# Приклад використання
manager = TaskManager()

# Додаємо завдання
task1 = Task("Завершити проект", "Завершити роботу над проектом", "2024-10-01")
task2 = Task("Написати звіт", "Написати фінальний звіт", "2024-09-30")

manager.add_task(task1)
manager.add_task(task2)

# Виводимо список завдань
print("Список завдань:")
manager.list_tasks()

# Відмічаємо завдання як виконане
manager.mark_task_as_completed("Завершити проект")

# Виводимо оновлений список завдань
print("\nОновлений список завдань:")
manager.list_tasks()
