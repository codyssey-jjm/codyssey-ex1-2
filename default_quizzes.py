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
