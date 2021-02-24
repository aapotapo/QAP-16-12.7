if __name__ == "__main__":
    money = input("Введите сумму:")
    per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
    values = per_cent.values()
    deposit = list(map(lambda n: int(n * int(money) / 100), values))
    print("Список возможных процентов по вкладам:", deposit)
    print("Максимальная сумма, которую вы можете заработать — ", max(deposit))
