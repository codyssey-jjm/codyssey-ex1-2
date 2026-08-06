"""퀴즈 게임의 메뉴와 공통 입력 흐름 관리."""

from pathlib import Path

import quiz_storage
from default_quizzes import create_default_quizzes
from quiz import Quiz


class QuizGame:
    """퀴즈 목록, 최고 점수, 메뉴 실행 흐름 관리."""

    def __init__(self) -> None:
        """기본 상태를 준비하고 저장된 상태 불러오기."""
        # 실행 위치와 관계없이 프로젝트 루트의 state.json 경로 설정
        self.state_file: Path = Path(__file__).with_name("state.json")
        self.quizzes: list[Quiz] = create_default_quizzes()
        self.best_score: int = 0
        self.load_state()

    def reset_to_default(self) -> None:
        """퀴즈 목록과 최고 점수를 기본 상태로 초기화."""
        self.quizzes = create_default_quizzes()
        self.best_score = 0

    def load_state(self) -> None:
        """state.json에서 퀴즈 목록과 최고 점수 불러오기."""
        state = quiz_storage.load_state(self.state_file)

        # 파일이 없거나 데이터를 사용할 수 없으면 기본 상태로 복구
        if state is None:
            self.reset_to_default()
            return

        self.quizzes, self.best_score = state

    def save_state(self) -> bool:
        """현재 퀴즈 목록과 최고 점수를 state.json에 저장."""
        return quiz_storage.save_state(
            self.state_file,
            self.quizzes,
            self.best_score,
        )

    def show_menu(self) -> None:
        """사용자가 선택할 수 있는 전체 메뉴 출력."""
        print("\n===== Python 기초 퀴즈 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    def read_number(
        self,
        prompt: str,
        minimum: int,
        maximum: int,
    ) -> int:
        """사용자가 올바른 범위의 숫자를 입력할 때까지 반복."""
        while True:
            # 사용자 입력을 받은 뒤 앞뒤 공백 제거
            # input()의 결과는 항상 문자열
            value = input(prompt).strip()

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

            return number

    def read_text(self, prompt: str) -> str:
        """사용자가 비어 있지 않은 문자열을 입력할 때까지 반복."""
        while True:
            value = input(prompt).strip()

            if value:
                return value

            print("값을 입력해 주세요.")

    def play_quiz(self) -> None:
        """저장된 퀴즈를 순서대로 출제하고 정답 수와 최종 점수 출력."""
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        total_count = len(self.quizzes)
        correct_count = 0

        print(f"\n퀴즈를 시작합니다. 총 {total_count}문제입니다.")

        for question_number, quiz in enumerate(self.quizzes, start=1):
            print("\n------------------------------")
            print(f"[문제 {question_number}]")
            quiz.display()

            selected_answer = self.read_number("정답 입력: ", 1, 4)

            if quiz.is_correct(selected_answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        score = self.calculate_score(correct_count, total_count)

        print("\n===== 퀴즈 결과 =====")
        print(f"전체 문제: {total_count}개")
        print(f"정답: {correct_count}개")
        print(f"점수: {score}점")

        if self.update_best_score(score):
            print("새로운 최고 점수입니다!")

    def calculate_score(self, correct_count: int, total_count: int) -> int:
        """정답 수를 100점 기준의 정수 점수로 계산."""
        # 정답 비율에서 소수점 아래를 버린 0~100점 반환
        return (correct_count * 100) // total_count

    def update_best_score(self, score: int) -> bool:
        """기존 점수보다 높은 점수를 최고 점수로 저장."""
        # 최고 점수를 넘지 못하면 값 변경 없이 False 반환
        if score <= self.best_score:
            return False

        # 새로운 최고 점수로 변경한 뒤 state.json에 저장
        self.best_score = score
        self.save_state()
        return True

    def add_quiz(self) -> None:
        """새 퀴즈 정보를 입력받아 현재 퀴즈 목록에 추가."""
        print("\n===== $$새로운 퀴즈 추가$$ =====")

        question = self.read_text("문제: ")

        choices: list[str] = []
        for choice_number in range(1, 5):
            choice = self.read_text(f"선택지 {choice_number}: ")
            choices.append(choice)

        answer = self.read_number("정답 번호 (1~4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        # 새 퀴즈가 재실행 후에도 유지되도록 현재 상태 저장
        self.save_state()

        print("퀴즈가 추가되었습니다!")
        print(f"현재 등록된 퀴즈: {len(self.quizzes)}개")

    def show_quizzes(self) -> None:
        """현재 등록된 모든 퀴즈의 문제와 선택지 출력."""
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return

        print(f"\n===== 등록된 퀴즈 목록: 총 {len(self.quizzes)}개 =====")

        for question_number, quiz in enumerate(self.quizzes, start=1):
            print("\n------------------------------")
            print(f"[문제 {question_number}]")
            quiz.display()

    def show_best_score(self) -> None:
        """현재까지 기록된 최고 점수 출력."""
        print(f"\n최고 점수: {self.best_score}점")

    def run(self) -> None:
        """종료 메뉴를 선택할 때까지 메뉴 실행 반복."""
        try:
            while True:
                self.show_menu()

                selected_menu = self.read_number("메뉴 선택: ", 1, 5)

                if selected_menu == 1:
                    self.play_quiz()
                elif selected_menu == 2:
                    self.add_quiz()
                elif selected_menu == 3:
                    self.show_quizzes()
                elif selected_menu == 4:
                    self.show_best_score()
                else:
                    print("\n퀴즈 게임을 종료합니다.")
                    break

        # Ctrl+C 또는 입력 스트림 종료 시 현재 상태 저장 후 종료
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되었습니다. 현재 상태를 저장하고 종료합니다.")
            self.save_state()
            print("퀴즈 게임을 종료합니다.")
