# Задача: Создай класс `Task`, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.



class Task():
    def __init__(self):
        self.tasks = []

    def add_task(self, deadline, description):
        self.tasks.append({'deadline': deadline , 'description': description, "status": "не выполнено" })

    def complete_task(self, description):
        for task in self.tasks:
            if task['description'] == description:
                task['status'] = "выполнено"
                print(f"Задача {description} выполнена")


    def show_tasks(self):
        print("Список задач:")
        for task in self.tasks:
            if task['status'] == "не выполнено":
                print(f"Задача {task['description']} - {task['deadline']}")
            else:
                print(f"Задача {task['description']} выполнена")

t = Task()
t.add_task("10.01.2023", "Заходить в магазин")
t.add_task("11.01.2023", "Купить продукты")
t.add_task("12.01.2023", "Помыть посуду")
t.add_task("13.01.2023", "Выгулять собаку")

t.show_tasks()

t.complete_task("Помыть посуду")



