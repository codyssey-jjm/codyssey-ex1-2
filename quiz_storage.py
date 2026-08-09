"""퀴즈와 최고 점수의 JSON 저장 및 불러오기."""

import json
from pathlib import Path

from quiz import Quiz


def _validate_integer(
    value: object, field: str, minimum: int, maximum: int | None = None
) -> int:
    """bool을 제외한 정수 형식과 허용 범위를 검증."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{field}는 정수여야 합니다.")
    if value < minimum or (maximum is not None and value > maximum):
        raise ValueError(f"{field}의 값 범위가 올바르지 않습니다.")
    return value


def validate_history(history_data: object) -> list[dict]:
    """JSON의 게임 기록 목록을 검증하고 정리된 목록 반환."""
    if not isinstance(history_data, list):
        raise TypeError("history는 목록이어야 합니다.")

    history: list[dict] = []
    for record_data in history_data:
        if not isinstance(record_data, dict):
            raise TypeError("각 게임 기록은 딕셔너리여야 합니다.")

        played_at = record_data["played_at"]
        total_count = _validate_integer(record_data["total_count"], "total_count", 1)
        correct_count = _validate_integer(
            record_data["correct_count"], "correct_count", 0, total_count
        )
        score = _validate_integer(record_data["score"], "score", 0, 100)

        if not isinstance(played_at, str):
            raise TypeError("played_at은 문자열이어야 합니다.")
        played_at = played_at.strip()
        if not played_at:
            raise ValueError("played_at은 비어 있을 수 없습니다.")
        history.append(
            {
                "played_at": played_at,
                "total_count": total_count,
                "correct_count": correct_count,
                "score": score,
            }
        )

    return history


def validate_state(data: object) -> tuple[list[Quiz], int, list[dict]]:
    """JSON 전체 구조를 검증하고 사용할 게임 상태 반환."""
    if not isinstance(data, dict):
        raise TypeError("저장 데이터는 딕셔너리여야 합니다.")

    # 필수 키를 가져오며 키가 없으면 KeyError 발생
    quizzes_data = data["quizzes"]
    best_score = _validate_integer(data["best_score"], "best_score", 0, 100)
    history_data = data.get("history", [])

    if not isinstance(quizzes_data, list):
        raise TypeError("quizzes는 목록이어야 합니다.")

    quizzes: list[Quiz] = []
    for quiz_data in quizzes_data:
        if not isinstance(quiz_data, dict):
            raise TypeError("각 퀴즈 데이터는 딕셔너리여야 합니다.")
        quizzes.append(Quiz.from_dict(quiz_data))

    history = validate_history(history_data)
    return quizzes, best_score, history


def load_state(state_file: Path) -> tuple[list[Quiz], int, list[dict]] | None:
    """JSON 파일에서 검증된 퀴즈 목록, 최고 점수, 기록 불러오기."""
    try:
        # 저장 파일이 없으면 호출 위치에서 기본 상태 사용
        if not state_file.exists():
            return None

        # with 문으로 파일을 사용한 뒤 자동으로 닫기
        with state_file.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return validate_state(data)

    except json.JSONDecodeError as error:
        print(f"\n저장 파일의 JSON 형식이 손상되었습니다: {error}")
        print("기본 퀴즈로 시작합니다.")

    except UnicodeDecodeError as error:
        print(f"\n저장 파일을 UTF-8로 읽을 수 없습니다: {error}")
        print("기본 퀴즈로 시작합니다.")

    except OSError as error:
        print(f"\n저장 파일을 읽을 수 없습니다: {error}")
        print("기본 퀴즈로 시작합니다.")

    except (KeyError, TypeError, ValueError) as error:
        print(f"\n저장 데이터의 구조가 올바르지 않습니다: {error}")
        print("기본 퀴즈로 시작합니다.")

    return None


def save_state(
    state_file: Path,
    quizzes: list[Quiz],
    best_score: int,
    history: list[dict],
) -> bool:
    """퀴즈 목록, 최고 점수, 게임 기록을 JSON 파일에 저장."""
    # Quiz 객체 목록을 JSON에 저장할 수 있는 딕셔너리 목록으로 변환
    data = {
        "quizzes": [quiz.to_dict() for quiz in quizzes],
        "best_score": best_score,
        "history": history,
    }

    # 한글을 유지하고 읽기 쉬운 형태로 JSON 파일 작성
    try:
        with state_file.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except OSError as error:
        print(f"\n현재 상태를 저장할 수 없습니다: {error}")
        return False

    return True
