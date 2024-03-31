# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи,
# срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, deadline, status="Incomplete"):
        self.description = description
        self.deadline = deadline
        self.status = status


list_of_tasks = []


def add_task(task):
    list_of_tasks.append(task)
    return list_of_tasks


def mark_complete(task):
    for t in list_of_tasks:
        if t == task:
            t.status = "Complete"


def display_tasks():
    for t in list_of_tasks:
        if t.status == "Incomplete":
            print(f"Task: {t.description}, Deadline: {t.deadline}, Status: {t.status}")


task1 = Task("Learn Python", "2022-01-01")
task2 = Task("Learn Django", "2022-01-02")
task3 = Task("Learn Flask", "2022-01-03")

add_task(task1)
add_task(task2)
add_task(task3)

display_tasks()

mark_complete(task2)

display_tasks()
