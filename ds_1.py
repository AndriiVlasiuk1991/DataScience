from numpy import arange, zeros, random, dot, linalg, transpose, multiply, sum, subtract, square, sqrt


def vector_10():
    vector = arange(1, 11)
    print('1. Створіть одновимірний масив (вектор) з першими 10-ма натуральними числами та виведіть його значення.')
    print(f'Вектор: \n{vector}\n')


def matrix_3x3():
    matrix = zeros((3, 3))
    print('2. Створіть двовимірний масив (матрицю) розміром 3x3, заповніть його нулями та виведіть його значення.')
    print(f'Матриця: \n{matrix}\n')


def random_matrix_5x5():
    random_matrix = random.randint(1, 11, size=(5, 5))
    print(
        '3. Створіть масив розміром 5x5, заповніть його випадковими цілими числами в діапазоні від 1 до 10 та виведіть його значення.')
    print(f'Матриця: \n{random_matrix}\n')


def random_matrix_4x4():
    random_matrix = random.rand(4, 4)
    print(
        '4. Створіть масив розміром 4x4, заповніть його випадковими дійсними числами в діапазоні від 0 до 1 та виведіть його значення.')
    print(f'Матриця: \n{random_matrix}\n')


def vector_5_operations():
    array_1 = random.randint(1, 11, size=5)
    array_2 = random.randint(1, 11, size=5)
    sum = array_1 + array_2
    sub = array_1 - array_2
    multiplication = array_1 * array_2
    print(
        '5. Створіть два одновимірних масиви розміром 5, заповніть їх випадковими цілими числами в діапазоні від 1 до 10 та виконайте на них поелементні операції додавання, віднімання та множення.')
    print(f'Вектор 1: {array_1}')
    print(f'Вектор 2: {array_2}')
    print(f'Сума: {sum}')
    print(f'Різниця: {sub}')
    print(f'Добуток: {multiplication}\n')


def vector_7_scalar():
    vector_1 = random.randint(1, 11, size=7)
    vector_2 = random.randint(1, 11, size=7)
    scalar = dot(vector_1, vector_2)
    print('6. Створіть два вектори розміром 7, заповніть довільними числами та знайдіть їх скалярний добуток.')
    print(f'Вектор 1: {vector_1}')
    print(f'Вектор 2: {vector_2}')
    print(f'Cкалярний добуток: {scalar}\n')


def two_matrix():
    matrix_1 = random.randint(1, 11, size=(2, 2))
    matrix_2 = random.randint(1, 11, size=(2, 3))
    multiplication = dot(matrix_1, matrix_2)
    print(
        '7. Створіть дві матриці розміром 2x2 та 2x3, заповніть їх випадковими цілими числами в діапазоні від 1 до 10 та перемножте їх між собою.')
    print(f'Матриця 1: \n{matrix_1}')
    print(f'Матриця 2: \n{matrix_2}')
    print(f'Результат множення матриць: \n{multiplication}\n')


def inverse_matrix():
    matrix = random.randint(1, 11, size=(3, 3))
    print(
        '8. Створіть матрицю розміром 3x3, заповніть її випадковими цілими числами в діапазоні від 1 до 10 та знайдіть її обернену матрицю.')
    print(f'Матриця: \n{matrix}')
    try:
        inv_matrix = linalg.inv(matrix)
        print(f'Обернена матриця: \n{inv_matrix}\n')
    except linalg.LinAlgError:
        print(f'Обернена матриця не існує\n')


def transposed_matrix():
    matrix = random.randint(1, 11, size=(4, 4))
    trans_matrix = transpose(matrix)
    print(
        '9. Створіть матрицю розміром 4x4, заповніть її випадковими дійсними числами в діапазоні від 0 до 1 та транспонуйте її.')
    print(f'Матриця: \n{matrix}')
    print(f'Транспонована матриця: \n{trans_matrix}\n')


def matrix_x_vector_int():
    matrix = random.randint(1, 11, size=(3, 4))
    vector = random.randint(1, 11, size=4)
    result_vector = dot(matrix, vector)
    print(
        '10. Створіть матрицю розміром 3x4 та вектор розміром 4, заповніть їх випадковими цілими числами в діапазоні від 1 до 10 та перемножте матрицю на вектор.')
    print(f'Матриця: \n{matrix}')
    print(f'Вектор: {vector}')
    print(f'Результат множення матриці на вектор: {result_vector}\n')


def matrix_x_vector():
    matrix = random.rand(2, 3)
    vector = random.rand(3)
    result_vector = dot(matrix, vector)
    print(
        '11. Створіть матрицю розміром 2x3 та вектор розміром 3, заповніть їх випадковими дійсними числами в діапазоні від 0 до 1 та перемножте матрицю на вектор.')
    print(f'Матриця: \n{matrix}')
    print(f'Вектор: {vector}')
    print(f'Результат множення матриці на вектор: {result_vector}\n')


def elementwise_matrix():
    matrix_1 = random.randint(1, 11, size=(2, 2))
    matrix_2 = random.randint(1, 11, size=(2, 2))
    elementwise = multiply(matrix_1, matrix_2)
    print(
        '12. Створіть дві матриці розміром 2x2, заповніть їх випадковими цілими числами в діапазоні від 1 до 10 та виконайте їхнє поелементне множення.')
    print(f'Матриця 1: \n{matrix_1}')
    print(f'Матриця 2: \n{matrix_2}')
    print(f'Результат поелементного множення матриць: \n{elementwise}\n')


def product_matrix():
    matrix_1 = random.randint(1, 11, size=(2, 2))
    matrix_2 = random.randint(1, 11, size=(2, 2))
    product = dot(matrix_1, matrix_2)
    print(
        '13. Створіть дві матриці розміром 2x2, заповніть їх випадковими цілими числами в діапазоні від 1 до 10 та знайдіть їх добуток.')
    print(f'Матриця 1: \n{matrix_1}')
    print(f'Матриця 2: \n{matrix_2}')
    print(f'Добуток матриць: \n{product}\n')


def sum_matrix():
    matrix = random.randint(1, 101, size=(5, 5))
    sum_elements = sum(matrix)
    print(
        '14. Створіть матрицю розміром 5x5, заповніть її випадковими цілими числами в діапазоні від 1 до 100 та знайдіть суму елементів матриці.')
    print(f'Матриця: \n{matrix}')
    print(f'Сума елементів матриці: {sum_elements}\n')


def sub_matrix():
    matrix_1 = random.randint(1, 11, size=(4, 4))
    matrix_2 = random.randint(1, 11, size=(4, 4))
    product = subtract(matrix_1, matrix_2)
    print(
        '15. Створіть дві матриці розміром 4x4, заповніть їх випадковими цілими числами в діапазоні від 1 до 10 та знайдіть їхню різницю.')
    print(f'Матриця 1: \n{matrix_1}')
    print(f'Матриця 2: \n{matrix_2}')
    print(f'Різниця матриць: \n{product}\n')


def sums_row_matrix():
    matrix = random.rand(3, 3)
    row_sums = sum(matrix, axis=1, keepdims=True)
    print(
        '16. Створіть матрицю розміром 3x3, заповніть її випадковими дійсними числами в діапазоні від 0 до 1 та знайдіть вектор-стовпчик, що містить суму елементів кожного рядка матриці.')
    print(f'Матриця: \n{matrix}')
    print(f'Cума елементів кожного рядка матриці: \n{row_sums}\n')


def squared_matrix():
    matrix = random.randint(-10, 11, size=(3, 4))
    square_matrix = square(matrix)
    print('17. Створіть матрицю розміром 3x4 з довільними цілими числами і створінь матрицю з квадратами цих чисел.')
    print(f'Матриця: \n{matrix}')
    print(f'Матриця з квадратами чисел: \n{square_matrix}\n')


def sqrt_vector():
    vector = random.randint(1, 51, size=4)
    sqrt_vector = sqrt(vector)
    print(
        '18. Створіть вектор розміром 4, заповніть його випадковими цілими числами в діапазоні від 1 до 50 та знайдіть вектор з квадратними коренями цих чисел.')
    print(f'Вектор: {vector}')
    print(f'Вектор з квадратними коренями: \n{sqrt_vector}\n')


if __name__ == '__main__':
    vector_10()
    matrix_3x3()
    random_matrix_5x5()
    random_matrix_4x4()
    vector_5_operations()
    vector_7_scalar()
    two_matrix()
    inverse_matrix()
    transposed_matrix()
    matrix_x_vector_int()
    matrix_x_vector()
    elementwise_matrix()
    product_matrix()
    sum_matrix()
    sub_matrix()
    sums_row_matrix()
    squared_matrix()
    sqrt_vector()
