from core.data import get_constellation, zodiac_from_birthday
from core.scaler import scale_coords
from core.renderer import render

WIDTH = 160
HEIGHT = 50

FAMOUS = [
    ("카시오페아자리", "famous_cassiopeia"),
    ("큰곰자리(북두칠성)", "famous_ursa_major"),
    ("오리온자리", "famous_orion"),
    ("큰개자리", "famous_canis_major"),
    ("센타우르스자리", "famous_centaurus"),
]


def show_constellation(key):
    coords, desc = get_constellation(key)
    if coords is None:
        print("별자리 데이터를 찾을 수 없습니다.\n")
        return

    points = scale_coords(coords, WIDTH, HEIGHT, padding=2)
    print(render(points, WIDTH, HEIGHT))
    print()
    print(desc)
    print("-" * 40)
    print()


def birthday_flow():
    raw = input("생일을 입력하세요 (MM DD): ").strip()
    parts = raw.split()

    if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
        print("입력 형식이 잘못되었습니다.\n")
        return

    month, day = int(parts[0]), int(parts[1])
    key = zodiac_from_birthday(month, day)

    if key is None:
        print("잘못된 생일입니다.\n")
        return

    show_constellation(key)


def famous_flow():
    print("유명한 별자리를 선택하세요:")
    for i, (kor, _) in enumerate(FAMOUS, start=1):
        print(f"{i}. {kor}")

    choice = input("번호 입력: ").strip()
    if not choice.isdigit():
        print("숫자를 입력하세요.\n")
        return

    idx = int(choice) - 1
    if idx < 0 or idx >= len(FAMOUS):
        print("잘못된 번호입니다.\n")
        return

    _, key = FAMOUS[idx]
    show_constellation(key)


def menu():
    print("1. 생일에 따른 별자리 보기")
    print("2. 유명한 별자리 보기")
    print("3. 종료하기")


def main():
    while True:
        menu()
        choice = input("선택: ").strip()
        print()

        if choice == "1":
            birthday_flow()
        elif choice == "2":
            famous_flow()
        elif choice == "3":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
