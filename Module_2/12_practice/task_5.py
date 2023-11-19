class TaskManager:
    def __init__(self):
        self.stack = Stack()

    def new_task(self, task, priority):
        self.stack.append((task, priority))

    def __str__(self):
        sorted_stack = sorted(self.stack.items, key=lambda x: x[1])
        q = sorted_stack[0][1]
        message = f"{q} -"
        for task in sorted_stack:
            if task[1] != q:
                message += "\n"
                message += f"{task[1]} - {task[0]};"
                q = task[1]
            else:
                message += f" {task[0]};"
        return message


class Stack:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print(manager)
