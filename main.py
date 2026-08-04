"""Python 기초 퀴즈 게임 실행."""

from quiz_game import QuizGame


def main() -> None:
    """퀴즈 게임 객체 생성 및 실행."""
    game = QuizGame()
    game.run()


# 다른 파일에서 main.py를 불러올 때 게임이 자동으로 시작되는 것을 방지
# main.py를 직접 실행했을 때만 main() 함수 호출
if __name__ == "__main__":
    main()
