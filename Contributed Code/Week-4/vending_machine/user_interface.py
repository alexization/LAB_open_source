from vending_machine import VendingMachine

def main():
    vending_machine = VendingMachine()

    while True:
        print("\n자판기 메뉴:")
        print("1. 음료수 목록 표시")
        print("2. 금액 투입")
        print("3. 음료수 구매")
        print("4. 잔액 확인")
        print("5. 거스름돈 반환")
        print("6. 음료수 추가 (관리자 모드)")
        print("7. 종료")
        choice = input("작업을 선택하세요: ")


        if choice == '1':
            vending_machine.display_products()
        elif choice == '2':
            # 양수 금액만 넣을 수 있도록 코드를 수정하였음.
            while True:
                amount = int(input("투입할 금액을 입력하세요: "))
                if amount > 0:
                    break
                else:
                    print("옳바른 돈을 투입하지 않았습니다.")
            vending_machine.insert_money(amount)
            print("금액이 투입되었습니다.")
        elif choice == '3':
            product_number = int(input("구매할 음료수 번호를 입력하세요: "))
            result = vending_machine.purchase(product_number)
            print(result)
        elif choice == '4':
            balance = vending_machine.check_balance()
            print(balance)
        elif choice == '5':
            change = vending_machine.return_change()
            print(f"거스름돈: {change}이 반환 되었습니다.")
        elif choice == '6':
            # 음료수를 추가할 수 있는 관리자 모드
            product_name = input("추가할 음료수 이름을 입력하세요: ")
            product_price = input("추가할 음료수 금액을 입력하세요: ")
            vending_machine.add_drink(product_name, product_price)
        elif choice == '7':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 선택이 아닙니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()