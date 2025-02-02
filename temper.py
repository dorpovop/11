def celsius_to_fahrenheit(celsius):
    """Конвертирует температуру из Цельсия в Фаренгейт"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Конвертирует температуру из Фаренгейта в Цельсий"""
    return (fahrenheit - 32) * 5/9

def main():
    print("Конвертер ")
    print("1: Цельсий → Фаренгейт")
    print("2: Фар → Цел")
    print("Следующий ")
    choice = input("вариант (1 или 2): ")

    if choice == "1":
        celsius = float(input("Введите температуру в Цельсиях: "))
        print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == "2":
        fahrenheit = float(input("Введите температуру в Фаренгейтах: "))
        print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    else:
        print("Ошибка: выберите 1 или 2.")

if __name__ == "__main__":
    main()
