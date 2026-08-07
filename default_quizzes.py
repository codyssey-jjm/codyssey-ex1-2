"""Python 기초 주제의 기본 퀴즈 데이터 정의."""

from quiz import Quiz


def create_default_quizzes() -> list[Quiz]:
    """Python 기초 주제의 기본 퀴즈 객체 다섯 개 생성 및 반환."""
    # 호출마다 새 목록과 Quiz 객체를 생성해 호출 간 변경 공유 방지
    return [
        Quiz(
            question="Python에서 함수를 정의할 때 사용하는 키워드는?",
            choices=["def", "function", "func", "lambda"],
            answer=1,
            hint="함수를 정의한다는 뜻의 영어 단어 define을 줄여 생각해 보세요.",
        ),
        Quiz(
            question="여러 값을 순서대로 저장하며 내용을 변경할 수 있는 자료형은?",
            choices=["tuple", "list", "set", "str"],
            answer=2,
            hint="대괄호로 만들며 append()로 항목을 추가할 수 있습니다.",
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
            hint="문자열이나 목록의 길이를 확인할 때 자주 사용합니다.",
        ),
        Quiz(
            question="조건문에서 앞선 조건이 거짓일 때 다른 조건을 검사하는 키워드는?",
            choices=["else", "elif", "then", "switch"],
            answer=2,
            hint="else if를 줄여 쓴 형태입니다.",
        ),
        Quiz(
            question="키와 값의 쌍으로 데이터를 저장하는 자료형은?",
            choices=["list", "tuple", "dict", "bool"],
            answer=3,
            hint="중괄호 안에 키와 값을 콜론으로 연결해 저장합니다.",
        ),
    ]
