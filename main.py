
# Класс Задачи - характеристики
class Task():
    def __init__(self, number, description, entry_date, dead_line, status, priority):
        self.number = number
        self.description = description
        self.entry_date = entry_date
        self.dead_line = dead_line
        self.status = status
        self.priority = priority

# Присвоение приоритета
    def set_priority(self, priority):
        self.priority = priority
# Обозначение статуса выполнения
    def update_status(self, status):
        self.status = status
# Вывод информации о задаче
    def __str__(self):
        return (f"Задача {self.number}: {self.description}, Приоритет: {self.priority}, "
                f"Дата начала: {self.entry_date}, Срок: {self.dead_line}, Статус: {self.status}")

# Класс Управления задачами - действия
class TaskManager:
    def __init__(self):
        self.tasks = []

# Добавление задачи
    def add_task(self, number, description, entry_date, dead_line, status='Не выполнена', priority=1):
        task = Task(number, description, entry_date, dead_line, status, priority)
        self.tasks.append(task)

# Выстраивание задач в соответствии с приоритетом
    def set_task_priority(self, number, priority):
        for task in self.tasks:
            if task.number == number:
                task.set_priority(priority)
                break
# Обновление статуса задачи для последующего вывода списка невыполненных задач
    def update_task_status(self, number, status):
        for task in self.tasks:
            if task.number == number:
                task.update_status(status)
                break
# Вывод задач в соответствии с приоритетом
    def display_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if task.status == 'Не выполнена']
        pending_tasks.sort(key=lambda x: (x.priority, x.entry_date))
        for task in pending_tasks:
            print(task)


# Тестирование системы управления задачами
task_manager = TaskManager()
task_manager.add_task(1, "Закончить проект", "2020-10-01", "2020-10-10", priority=1)
task_manager.add_task(2, "Написать отчет", "2020-10-01", "2020-10-12", priority=2)
task_manager.add_task(3, "Сделать задание", "2020-10-02", "2020-10-15", priority=1)
task_manager.add_task(4, "Провести переговоры", "2020-10-03", "2020-10-17", priority=2)
task_manager.add_task(5, "Сделать домашку", "2020-10-01", "2020-10-10", priority=3)


task_manager.update_task_status(2, "Выполнена")
task_manager.update_task_status(3, "Выполнена")

print("Текущие задачи:")
task_manager.display_pending_tasks()