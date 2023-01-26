# открываем файл для чтения
with open('TeskeEA_ZIT-22_vvod.txt', 'r') as in_file:
    # открываем файл для записи
    out_file = open('TeskeEA_ZIT-22_vivod.txt', 'w')
    # считываем строку
    x = in_file.readline()
    element = 0
    # создаём матрицу
    matrix = []
    while x != '':
        # убираем лишний символ переноса строки
        if x[-1] == '\n':
            x = x[:-1]
        # преобразуем строку в массив символов
        line = x.split(' ')
        # создаём массив который будет строкой в матрице и заполняем его числами
        mas = []
        for i in line:
            mas.append(int(i))
        # находим максимальный элемент в строке и сравниваем с макс из прошлой строки
        element = max(max(mas), element)
        # запоняем матрицу
        matrix.append(mas)
        # считываем новую строку
        x = in_file.readline()
    b = 0
    m = 0
    r = 0
    for i in matrix:
        for j in i:
            if j > element:
                b += 1
            elif j < element:
                m += 1
            elif j == element:
                r += 1
    out_file.write("максимальный элемент матрицы - "+str(element)+'\n')
    out_file.write("элементов > "+str(b)+'\n')
    out_file.write("элементов < " + str(m) + '\n')
    out_file.write("элементов = " + str(r) + '\n')
    # закрываем файлы
    out_file.close()
    in_file.close()
