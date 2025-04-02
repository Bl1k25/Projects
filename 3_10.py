# Функция для сравнения элементов кучи
# Определяет, нужно ли поменять местами родителя и ребенка
def is_child_less(child, parent):
    if child[1] < parent[1]:  # Если у ребенка меньше решенных задач, он "меньше"
        return True
    elif child[1] == parent[1]:  # Если задачи равны, проверяем штраф
        if child[2] > parent[2]:  # Больше штраф - "меньше"
            return True
        elif child[2] == parent[2]:  # Если штрафы равны, проверяем логин
            if child[0] > parent[0]:  # Логин стоит позже в алфавитном порядке - "меньше"
                return True
    return False  # Иначе родитель меньше

# Функция для поддержания свойств кучи
# Преобразует поддерево с корнем в i в min-кучу
def heapify(array, i, n):
    smallest = i  # Начинаем с корневого узла
    left = 2 * i + 1  # Левый потомок
    right = 2 * i + 2  # Правый потомок

    # Проверяем, является ли левый потомок меньше родителя
    if left < n and is_child_less(array[left], array[smallest]):
        smallest = left

    # Проверяем, является ли правый потомок меньше текущего "наименьшего"
    if right < n and is_child_less(array[right], array[smallest]):
        smallest = right

    # Если "наименьший" элемент не родитель, меняем местами и рекурсивно вызываем heapify
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        heapify(array, smallest, n)

# Основная функция сортировки кучей
def heap_sort(array):
    n = len(array)

    # Построение min-кучи (перестраиваем массив)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, i, n)

    # Извлечение элементов из кучи по одному
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # Меняем корень с последним элементом
        heapify(array, 0, i)  # Восстанавливаем свойства кучи


n = int(input())  # Количество участников
players = []  # Список участников
for _ in range(n):
    log, p, f = input().split()
    players.append((log, int(p), int(f)))  # Сохраняем данные как кортеж

# Сортировка
heap_sort(players)

# Вывод результатов
for player in players:
    print(player[0], sep='\n')
