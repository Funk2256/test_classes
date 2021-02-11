class Number:

    @staticmethod
    def user_input():
        while True:
            try:
                x = int(input())
                return x
                break
            except ValueError:
                print(f'Введите число а не буквы!')
                continue
