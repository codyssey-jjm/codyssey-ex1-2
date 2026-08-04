"""퀴즈 한 문제의 데이터와 기본 퀴즈 목록 정의."""

class Quiz:
    """문제 하나와 선택지, 정답 관리.

    속성:
        question: 사용자에게 보여줄 문제 내용
        choices: 문제와 함께 보여줄 네 개의 선택지
        answer: 1부터 시작하는 정답 선택지 번호
    """

    def __init__(
        self,
        question: str,
        choices: list[str],
        answer: int,
    ) -> None:
        """객체 생성에 필요한 값 검증 및 속성 저장."""
        if not isinstance(question, str):
            raise TypeError("문제는 문자열이어야 합니다.")
        if not isinstance(choices, list):
            raise TypeError("선택지는 목록이어야 합니다.")

        # bool은 int의 하위 타입이므로 True와 False를 정답 번호에서 제외
        if isinstance(answer, bool) or not isinstance(answer, int):
            raise TypeError("정답 번호는 정수여야 합니다.")

        # 문제 앞뒤 공백 제거 및 실제 내용 존재 여부 확인
        question = question.strip()
        # 빈 문자열은 False로 취급
        if not question:
            raise ValueError("문제는 비어 있을 수 없습니다.")
        if len(choices) != 4:
            raise ValueError("선택지는 정확히 4개여야 합니다.")

        # 모든 선택지의 문자열 여부 확인 및 앞뒤 공백을 제거한 새 목록 생성
        # 정리된 선택지를 저장할 빈 리스트 생성
        normalized_choices: list[str] = []
        for choice in choices:
            if not isinstance(choice, str):
                raise TypeError("각 선택지는 문자열이어야 합니다.")

            normalized_choice = choice.strip()
            if not normalized_choice:
                raise ValueError("선택지는 비어 있을 수 없습니다.")
            normalized_choices.append(normalized_choice)

        # 네 개의 선택지에 맞춘 정답 번호 범위 1~4 검사
        if answer not in range(1, 5):
            raise ValueError("정답 번호는 1부터 4 사이여야 합니다.")

        # 검증을 통과한 값만 객체의 최종 속성으로 저장
        self.question = question
        self.choices = normalized_choices
        self.answer = answer

    def display(self) -> None:
        """문제와 네 개의 선택지 출력."""
        print(self.question)

        # enumerate의 시작값을 1로 지정해 선택지 번호를 1부터 출력
        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")

    def is_correct(self, selected_answer: int) -> bool:
        """사용자가 선택한 번호와 정답 번호의 일치 여부 반환."""
        return selected_answer == self.answer


def create_default_quizzes() -> list[Quiz]:
    """Python 기초 주제의 기본 퀴즈 객체 다섯 개 생성 및 반환."""
    # 호출마다 새 목록과 Quiz 객체를 생성해 호출 간 변경 공유 방지
    return [
        Quiz(
            question="Python에서 함수를 정의할 때 사용하는 키워드는?",
            choices=["def", "function", "func", "lambda"],
            answer=1,
        ),
        Quiz(
            question="여러 값을 순서대로 저장하며 내용을 변경할 수 있는 자료형은?",
            choices=["tuple", "list", "set", "str"],
            answer=2,
        ),
        Quiz(
            question="len() 함수의 역할은?",
            choices=[
                "값의 자료형을 확인한다.",
                "값을 문자열로 변환한다.",
                "객체에 포함된 항목의 개수를 반환한다.",
                "숫자를 반올림한다.",
            ],
            answer=3,
        ),
        Quiz(
            question="조건문에서 앞선 조건이 거짓일 때 다른 조건을 검사하는 키워드는?",
            choices=["else", "elif", "then", "switch"],
            answer=2,
        ),
        Quiz(
            question="키와 값의 쌍으로 데이터를 저장하는 자료형은?",
            choices=["list", "tuple", "dict", "bool"],
            answer=3,
        ),
    ]
