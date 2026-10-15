import random

def generate_numbers_v2(a_student_id, num_reqs):
    # Check that there are at least two requirements available to assign
    if num_reqs < 2:
       raise ValueError("Invalid number of requirements. Must have at  least 2")
    
    # Remove any dashes or spaces from the student_id
    student_id = ''.join(filter(str.isdigit, a_student_id))
      
    # Ensure the student_id is valid (8 digits)
    if len(student_id) != 8:
       raise ValueError("Invalid student ID. It should be 8 digits.")
    
    # Generate two unique random numbers from 1 to num_reqs
    random.seed(student_id)  # Seed the random number generator with the student ID for reproducibility

    return random.sample(range(1, num_reqs+1), 2)
    

def generate_numbers(a_student_id, num_reqs):
   # Check that there are at least two requirements available to assign
   if num_reqs < 2:
       raise ValueError("Invalid number of requirements. Must have at  least 2")
   # Remove any dashes or spaces from the student_id
   id = ''.join(filter(str.isdigit, a_student_id))
  
   # Ensure the student_id is valid (8 digits)
   if len(id) != 8:
       raise ValueError("Invalid student ID. It should be 8 digits.")

   # Use a simple algorithm to generate two unique numbers from 1 to num_reqs
   sum_digits = sum(int(digit) for digit in id)
   first_num = (sum_digits % num_reqs) + 1

   product_digits = 1
   for digit in id:
       if int(digit) != 0:  # Avoid multiplying by zero
           product_digits *= int(digit)
   second_num = (product_digits % num_reqs) + 1

   # Ensure the numbers are different
   while second_num == first_num:
       second_num = (second_num % num_reqs) + 1

   return first_num, second_num


def test_harness(num_ids=100, num_reqs=10):
   from collections import Counter

   # Use an isolated RNG so v2's reseeding of the global RNG doesn't affect ID generation
   rng = random.Random()
   ids = [''.join(rng.choice('0123456789') for _ in range(8)) for _ in range(num_ids)]

   for name, func in (("generate_numbers", generate_numbers),
                      ("generate_numbers_v2", generate_numbers_v2)):
       counts = Counter()
       first_counts = Counter()
       second_counts = Counter()
       for sid in ids:
           n1, n2 = func(sid, num_reqs)
           assert n1 != n2, f"{name} produced duplicates for {sid}"
           counts.update((n1, n2))
           first_counts[n1] += 1
           second_counts[n2] += 1

       total = sum(counts.values())
       print(f"\n{name}: distribution over {num_ids} random IDs (numbers 1-{num_reqs})")
       print(f"{'Num':>3} {'Total':>6} {'%':>6} {'First':>6} {'Second':>6}")
       for n in range(1, num_reqs + 1):
           pct = 100 * counts[n] / total
           print(f"{n:>3} {counts[n]:>6} {pct:>5.1f}% {first_counts[n]:>6} {second_counts[n]:>6}  {'#' * counts[n]}")


if __name__ == "__main__":
#   Uncomment the following lines to run the test harness
#   test_harness()
#   exit(0)

#  Otherwise this program runs in interactive mode.
   try:
      student_id = input("Enter your student id (XXX-XX-XXX): ")
      num1, num2 = generate_numbers(student_id, 10)
      print(f"Your two numbers are: {num1} and {num2}")
      num1, num2 = generate_numbers_v2(student_id, 10)
      print(f"Your two numbers from v2 are: {num1} and {num2}")
   except ValueError as e:
      print(f"Error: {e}")
