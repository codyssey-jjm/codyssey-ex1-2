"""퀴즈 한 문제의 데이터와 동작 정의."""

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

        question = question.strip()

        # 빈 문자열은 False로 취급
        if not question:
            raise ValueError("문제는 비어 있을 수 없습니다.")
        if len(choices) != 4:
            raise ValueError("선택지는 정확히 4개여야 합니다.")

        # 원본 목록을 바꾸지 않고 공백을 제거한 새 선택지 목록 생성
        normalized_choices: list[str] = []
        for choice in choices:
            if not isinstance(choice, str):
                raise TypeError("각 선택지는 문자열이어야 합니다.")

            normalized_choice = choice.strip()
            if not normalized_choice:
                raise ValueError("선택지는 비어 있을 수 없습니다.")
            normalized_choices.append(normalized_choice)

        if answer not in range(1, 5):
            raise ValueError("정답 번호는 1부터 4 사이여야 합니다.")

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

    def to_dict(self) -> dict:
        """Quiz 객체를 JSON 저장용 딕셔너리로 변환."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Quiz":
        """JSON에서 읽은 딕셔너리를 Quiz 객체로 변환."""
        # 생성자를 다시 거쳐 저장 데이터에도 동일한 값 검증 적용
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
        )
