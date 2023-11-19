class Node:
    def __init__(self, item):
        self.item = item
        self.link = None


class LinkedList:
    def __init__(self):
        self.last_node = None

    def append(self, item):
        create_node = Node(item)
        if not self.last_node:  # создает элемент для списка без элементов
            self.last_node = create_node
        else:
            current = self.last_node
            while current.link:  # не остановится пока не найдет элемента без привязки
                current = current.link
            current.link = create_node  # добавляет к последнему элементу ссылку на новый элемент

    def get(self, index):
        if index < 0:
            raise IndexError  # у эл. нет ссылки на предыдущий элемент так что без отрицательных индексов
        current = self.last_node
        for i in range(index):
            if current.link:
                current = current.link
            else:
                raise IndexError  # индекс превышает длину листа
        return current.item

    def remove(self, index):
        if index < 0 or not self.last_node:
            raise IndexError
        if index == 0:
            self.last_node = self.last_node.link
            return
        current = self.last_node
        for i in range(index - 1):
            if current.link:
                current = current.link
            else:
                raise IndexError
        if current.link:
            current.link = current.link.link

    def __iter__(self):
        current = self.last_node
        while current:
            yield current.item
            current = current.link

    def __repr__(self):
        return f'[{" ".join(str(item) for item in self)}]'


# Пример использования
my_list = LinkedList()
for i in range(10):
    my_list.append(i ** 2)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
