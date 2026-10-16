"""  Debugging Exercise 1: Passing Scores
This program is supposed to:
  1. Report the class average for ALL students.
  2. Remove every failing score (below 60) from the list.
  3. Report how many students passed and their average.
Run it and look carefully at the output. Is everything correct?   """

def remove_failing(scores):
    # Remove all scores below 60 and return the passing scores.
    if scores[0] < 60:
        scores.remove(scores[0])
        return remove_failing(scores) if len(scores) > 0 else scores
    else:
        return [scores[0]] + remove_failing(scores[1:]) if len(scores) > 1 else [scores[0]]

def average(numbers):
    return sum(numbers) / len(numbers)

scores = [55, 48, 92, 61, 45, 70, 58, 88]
passing = remove_failing(scores)

print("Passing scores:", passing)
print("Number of students who passed:", len(passing))
print("Average of passing scores:", round(average(passing), 1))
print("Class average (all students):", round(average(scores), 1))
