from utils import get_valid_answer
from questions import questions

def calculate_scores(answers, questions):
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    for ans, q in zip(answers, questions):
        dim = q["dimension"]
        if dim == "E/I":
            if ans == 1: scores["E"] += 1
            elif ans == 3: scores["I"] += 1
        elif dim == "S/N":
            if ans == 1: scores["S"] += 1
            elif ans == 3: scores["N"] += 1
        elif dim == "T/F":
            if ans == 1: scores["T"] += 1
            elif ans == 3: scores["F"] += 1
        elif dim == "J/P":
            if ans == 1: scores["J"] += 1
            elif ans == 3: scores["P"] += 1
    return scores


def determine_personality(scores):
    personality = ""
    personality += "E" if scores["E"] >= scores["I"] else "I"
    personality += "S" if scores["S"] >= scores["N"] else "N"
    personality += "T" if scores["T"] >= scores["F"] else "F"
    personality += "J" if scores["J"] >= scores["P"] else "P"
    return personality


def run_test():
    print(" تست شخصیتی MBTI آغاز شد!\n")

    answers = []
    for i, q in enumerate(questions):
        print(f"\n سوال {i+1}: {q['question']}")
        answer = get_valid_answer(["موافقم", "تاحدی", "مخالفم"])
        answers.append(answer)

    scores = calculate_scores(answers, questions)
    personality = determine_personality(scores)

    print("\n تست شما به پایان رسید!")
    print(f" تیپ شخصیتی شما: {personality}")
    print(" ممنون که در تست MBTI شرکت کردید ")


if __name__ == "__main__":
    run_test()