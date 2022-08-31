def func_calc():
    mathematic_action = input("Введите операцию (+, -, *, / или 0 для выхода): ")

    if mathematic_action == '0':
        return "Выход"

    else:
        if mathematic_action in "+-*/":
            try:
                num_1 = int(input("Введите первое число: "))
                num_2 = int(input("Введите второе число: "))

                if operation_type == '+':
                    result = num_1 + num_2
                    print(f"Ваш результат {result}")
                    exit(0)

                elif operation_type == '-':
                    result = num_1 - num_2
                    print(f"Ваш результат {result}")
                    exit(0)

                elif operation_type == '*':
                    result = num_1 * num_2
                    print(f"Ваш результат {result}")
                    exit(0)

                elif operation_type == '/':
                    try:
                        result = num_1 / num_2
                    except ZeroDivisionError:
                        print("Деление на 0 невозможно")
                    else:
                        print(f"Ваш результат {result}")
                    finally:
                        return func_calc()

            except ValueError:
                print("Вы вместо трехзначного числа ввели строку. Исправьтесь")
                return func_calc()

        else:
            print("Введен неверный символ, попробуйте еще раз")
            return func_calc()
func_calc()
