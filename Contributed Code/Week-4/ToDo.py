class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        if task_index >=1 and task_index <= len(self.tasks):
            remove_task = self.tasks.pop(task_index - 1)
            print(f"{remove_task}가 할 일 목록에서 삭제되었습니다.")
        else:
            print("잘못된 번호입니다. 다시 시도하세요.")

    def view_tasks(self):
        if not self.tasks:
            print("할 일이 없습니다.")
        else:
            print("할 일 목록:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def edit_task(self, task_index, new_task):
        if task_index >= 1 and task_index <= len(self.tasks):
            self.tasks[task_index - 1] = new_task
    
    def revise_task(self): # 함수 추가
        if not self.tasks:
            print("할 일이 없습니다.")
        else:
            print("할 일 목록:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
            task_index = int(input("수정할 할 일의 번호를 입력하세요: "))
            new_task = input("새로운 할 일을 입력하세요: ")
            self.edit_task(task_index, new_task)
            
    def switch_task(self):
        if not self.tasks:
            return
        
        task_index = int(input("순서를 변경할 할 일을 선택하세요: "))
        if task_index < 1 or task_index > len(self.tasks):
            print("해당 번호에는 변경할 할 일이 없습니다.")
            return
        else:
            task = self.tasks[task_index-1]

        new_index = int(input("옮기고 싶은 순서번호를 입력해주세요: "))
        if new_index < 1 or new_index > len(self.tasks):
            print("해당 번호로는 변경할 수 없습니다.")
            return
        
        self.tasks.insert(new_index-1, task)
        del self.tasks[task_index]
        print("수정 완료!")


def main():
    to_do_list = ToDoList()
    
    while True:
        print("\n할 일을 선택하세요:")
        print("1. 할 일 추가")
        print("2. 할 일 삭제")
        print("3. 할 일 목록 보기")
        print("4. 할 일 수정")
        print("5. 할 일 순서 변경")
        print("6. 종료")

        choice = input("선택: ")

        if choice == "1":
            task = input("추가할 할 일을 입력하세요: ")
            to_do_list.add_task(task)
        elif choice == "2":
            to_do_list.view_tasks()
            try:
                task_index = int(input("삭제할 할 일의 번호를 입력하세요: "))
                to_do_list.remove_task(task_index)
            except ValueError:
                print("잘못된 입력입니다. 숫자를 입력하세요.")
        elif choice == "3":
            to_do_list.view_tasks()
        elif choice == "4":
            to_do_list.revise_task() # 함수 추가
        elif choice == "5":
            to_do_list.view_tasks()
            to_do_list.switch_task()
        elif choice == "6":
            print("애플리케이션을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
