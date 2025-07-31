def is_strange_number(n):
    """
    G'aroyib son tekshirish funksiyasi
    G'aroyib son - raqamlarining kvadratlari yig'indisi 
    raqamlar yig'indisining kvadratiga teng bo'lgan son
    """
    digits = [int(d) for d in str(n)]
    sum_of_squares = sum(d**2 for d in digits)
    square_of_sum = (sum(digits))**2
    return sum_of_squares == square_of_sum

def count_strange_numbers(n):
    """
    1 dan N gacha bo'lgan g'aroyib sonlar sonini hisoblash
    """
    count = 0
    for i in range(1, n + 1):
        if is_strange_number(i):
            count += 1
    return count

# Test funksiyasi
def test_solution():
    print("G'aroyib sonlarni tekshirish:")
    
    # 162 sonini tekshirish (masalada berilgan misol)
    print(f"162 g'aroyib son: {is_strange_number(162)}")
    
    # Birinchi bir nechta g'aroyib sonlarni topish
    print("\nBirinchi g'aroyib sonlar:")
    strange_numbers = []
    for i in range(1, 1000):
        if is_strange_number(i):
            strange_numbers.append(i)
            if len(strange_numbers) <= 10:
                digits = [int(d) for d in str(i)]
                sum_of_squares = sum(d**2 for d in digits)
                square_of_sum = (sum(digits))**2
                print(f"{i}: {digits} -> {sum_of_squares} = {square_of_sum}")
    
    print(f"\n1000 gacha {len(strange_numbers)} ta g'aroyib son bor")

# Asosiy dastur
def main():
    # Test
    test_solution()
    
    # Foydalanuvchidan kirish olish
    try:
        n = int(input("\nN ni kiriting (1 <= N <= 30000): "))
        if 1 <= n <= 30000:
            result = count_strange_numbers(n)
            print(f"1 dan {n} gacha {result} ta g'aroyib son bor")
        else:
            print("N 1 dan 30000 gacha bo'lishi kerak!")
    except ValueError:
        print("Iltimos, to'g'ri son kiriting!")

if __name__ == "__main__":
    main()