"""  Debugging Exercise 1: Passing Scores
This program is supposed to:
  1. Report the class average for ALL students.
  2. Remove every failing score (below 60) from the list.
  3. Report how many students passed and their average.
Run it and look carefully at the output. Is everything correct?   """

def remove_failing(scores):
    # Remove all scores below 60 and return the passing scores.
    for score in scores:
        if score < 60:
            scores.remove(score)
    return scores

def average(numbers):
    return sum(numbers) / len(numbers)

scores = [55, 48, 92, 61, 45, 70, 58, 88]
passing = remove_failing(scores)

print("Passing scores:", passing)
print("Number of students who passed:", len(passing))
print("Average of passing scores:", round(average(passing), 1))
print("Class average (all students):", round(average(scores), 1))
