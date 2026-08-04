"""퀴즈 게임의 메뉴와 공통 입력 흐름 관리."""

# quiz.py에 작성한 Quiz 클래스와 기본 퀴즈 생성 함수 가져오기
from quiz import Quiz, create_default_quizzes


class QuizGame:
    """퀴즈 목록, 최고 점수, 메뉴 실행 흐름 관리."""

    def __init__(self) -> None:
        """기본 퀴즈 목록과 최고 점수 초기화."""
        # 기본 퀴즈 다섯 개를 생성해 게임의 퀴즈 목록으로 저장
        self.quizzes: list[Quiz] = create_default_quizzes()

        # 아직 퀴즈를 풀지 않은 상태이므로 최고 점수를 0점으로 저장
        self.best_score: int = 0

    def show_menu(self) -> None:
        """사용자가 선택할 수 있는 전체 메뉴 출력."""
        print("\n===== Python 기초 퀴즈 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    # 사용자가 올바른 범위의 숫자를 입력할 때 까지 계속 입력받는 메서드
    def read_number(
        self,
        prompt: str,
        minimum: int,
        maximum: int,
    ) -> int:
        """지정한 범위의 숫자를 입력할 때까지 반복."""
        # 올바른 숫자를 입력하면 return으로 끝나는 입력 반복
        while True:
            # 사용자 입력을 받은 뒤 앞뒤 공백 제거
            # input()의 결과는 항상 문자열
            value = input(prompt).strip()

            # 아무것도 입력하지 않은 경우 안내 후 반복문의 처음으로 이동
            if not value:
                print("값을 입력해 주세요.")
                continue

            # 입력한 문자열을 정수로 변환 시도
            try:
                number = int(value)

            # 정수로 바꿀 수 없는 입력이면 안내 후 다시 입력
            except ValueError:
                print("숫자를 입력해 주세요.")
                continue

            # 변환한 숫자가 허용 범위를 벗어났는지 검사
            if number < minimum or number > maximum:
                print(f"{minimum}부터 {maximum} 사이의 숫자를 입력해 주세요.")
                continue

            # 모든 검사를 통과한 숫자를 메서드 호출 위치로 반환
            return number

    def play_quiz(self) -> None:
        """퀴즈 풀기 메뉴의 현재 상태 안내."""
        print("\n퀴즈 풀기 기능은 아직 준비 중입니다.")

    def add_quiz(self) -> None:
        """퀴즈 추가 메뉴의 현재 상태 안내."""
        print("\n퀴즈 추가 기능은 아직 준비 중입니다.")

    def show_quizzes(self) -> None:
        """퀴즈 목록 메뉴의 현재 상태 안내."""
        print("\n퀴즈 목록 기능은 아직 준비 중입니다.")

    def show_best_score(self) -> None:
        """점수 확인 메뉴의 현재 상태 안내."""
        print("\n점수 확인 기능은 아직 준비 중입니다.")

    def run(self) -> None:
        """종료 메뉴를 선택할 때까지 메뉴 실행 반복."""
        # 사용자가 5번을 선택할 때까지 메뉴 반복
        while True:
            self.show_menu()

            # 공통 숫자 입력 메서드로 1~5 범위의 메뉴 번호 입력
            selected_menu = self.read_number("메뉴 선택: ", 1, 5)

            # 입력한 메뉴 번호에 맞는 메서드 호출
            if selected_menu == 1:
                self.play_quiz()
            elif selected_menu == 2:
                self.add_quiz()
            elif selected_menu == 3:
                self.show_quizzes()
            elif selected_menu == 4:
                self.show_best_score()
            else:
                # 5번 선택 시 안내 문구 출력 후 while 반복 종료
                print("\n퀴즈 게임을 종료합니다.")
                break
