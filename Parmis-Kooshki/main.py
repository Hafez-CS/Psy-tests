from logic import MBTITest
from questions import questions


def main():
    """نقطه شروع برنامه MBTI"""
    test = MBTITest(questions)
    test.conduct_test()


if __name__ == "__main__":
    main()
