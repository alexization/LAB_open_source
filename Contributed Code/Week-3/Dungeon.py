"""
텍스트 기반 던전 크롤러 게임을 만들려고 합니다. 
이 게임에는 플레이어와 몬스터가 등장하며, 플레이어는 몬스터를 공격하여 처치하거나 회복하여 생존해야 합니다. 
아래는 게임을 구현하기 위한 파이썬 코드의 일부입니다.
"""

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def attack(self):
        return random.randint(10, 20)

    def heal(self):
        self.health += random.randint(10, 20)

    def take_damage(self, damage):
        self.health -= damage

class Monster:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(50, 100)
        self.attack_damage = random.randint(5, 15)

    def attack(self):
        return self.attack_damage

    def take_damage(self, damage):
        """
        Monster 클래스한테도 take_damage() 함수를 추가했습니다.
        """
        self.health -= damage

def main():
    player_name = input("플레이어 이름을 입력하세요: ")
    player = Player(player_name)

    monsters = [Monster("고블린"), Monster("드래곤"), Monster("스켈레톤")]

    print(f"{player.name}님, 던전 크롤러에 오신 것을 환영합니다!")

    while player.health > 0:
        command = input("어떤 행동을 하시겠습니까? (공격/회복/나가기): ").lower()

        if command == "나가기":
            print("게임을 종료합니다.")
            break
        elif command == "공격":
            choice = random.randrange(0, len(monsters))
            print(choice) # 이거 이따가 지우기!
            monster = monsters[choice]
            #monster = random.choice(monsters)
            print(f"{player.name}님이 {monster.name}을(를) 공격합니다!")
            damage = player.attack()
            monster.take_damage(damage)
            print(f"{monster.name}에게 {damage}의 데미지를 입혔습니다.")
            if monster.health <= 0:
                print(f"{monster.name}을(를) 처치하였습니다!")
                player.inventory.append(f"{monster.name}의 아이템")
                del monsters[choice] # 몬스터를 monsters에서 삭제하기 
            else: # 아직 monster가 죽지 않았다면, monster가 공격할 차례
                print(f"{monster.name}가 {player.name}님을 공격합니다!")
                monster_damage = monster.attack()
                player.take_damage(monster_damage)
                print(f"{player.name}님에게 {monster_damage}의 데미지를 입혔습니다. 현재 체력: {player.health}")
                
        elif command == "회복":
            player.heal()
            print(f"{player.name}님이 회복하였습니다. 현재 체력: {player.health}")
        
        if not monsters: # 모든 몬스터를 처치했을 경우, 자동으로 게임이 끝나게 코드를 추가했습니다.
            print("모든 몬스터를 처치했습니다!")
            break

    print("게임이 종료되었습니다.")

    if player.health > 0:
        print(f"{player.name}님의 승리! 획득한 아이템: {', '.join(player.inventory)}")
    else:
        print(f"{player.name}님의 패배!")

if __name__ == "__main__":
    main()
