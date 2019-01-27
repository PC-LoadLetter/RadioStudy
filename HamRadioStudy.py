import random
import time
from questionpool import technician_class_pool as exam

def main():
    try:
        from progress import score
    except:
        update_score(dict())
        score = dict()
    pool = list(exam.keys())
    correct, incorrect = 0, 0
    qs = input("How many ham radio questions do you want to practice?: ")

    for i in range(int(qs)):
        ask = random.choice(pool)
        pool.remove(ask)
        score.setdefault(ask, dict())
        print(exam[ask]["Question"])
        for j in ["A","B","C","D"]:
            print(exam[ask][j])

        response = input("? ")
        if response.upper() == exam[ask]["Answer"]:
            score[ask].setdefault("Correct", 1)
            correct += 1
            print("Correct")
        else:
            score[ask].setdefault("Incorrect", 1)
            incorrect += 1
            print("The correct answer is: "+exam[ask]["Answer"])

    update_score(score)
    total = correct + incorrect
    grade = round((correct/total*100),0)
    print(f"You attempted {total} questions answering {correct} correctly for a score of {grade}.")
    time.sleep(5)

def update_score(score):
    progress_file = open(r"progress.py", "w")
    progress_file.write("score = "+score.__str__())
    progress_file.close()


if __name__ == "__main__":
    main()

    

