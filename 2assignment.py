class Students:
    def __init__(self, student_id: int, first_name: str, last_name: str):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.exam_scores = []

    def add_score(self, score: int):
        if 0 <= score <= 100:
            self.exam_scores.append(score)

    def show_scores(self):
        print("Exam Scores:", end=" ")
        for score in self.exam_scores:
            print(score, end=" ")
        print()

    def score_average(self):
        if len(self.exam_scores) == 0:
            print("This student hasn't taken any exams yet.")
        else:
            average = sum(self.exam_scores) / len(self.exam_scores)
            return average

    def course_passed(self):
        passed_scores = [score for score in self.exam_scores if score > 60]
        return len(passed_scores) >= 3
# Create the Student objects
student_1 = Students(1, "John", "Doe")
student_1.add_score(100)
student_1.add_score(95)

student_2 = Students(2, "Linda", "Jones")
student_2.add_score(25)
student_2.add_score(65)
student_2.add_score(80)
student_2.add_score(75)

student_3 = Students(3, "Jason", "Kirk")
student_3.add_score(50)
student_3.add_score(60)
student_3.add_score(55)

student_4 = Students(4, "Jane", "Doe")
student_4.add_score(95)
student_4.add_score(80)
student_4.add_score(100)

# Test the methods for each student
print("Student 1:")
student_1.show_scores()
print("Average score:", student_1.score_average())
print("Course passed?", student_1.course_passed())

print("Student 2:")
student_2.show_scores()
print("Average score:", student_2.score_average())
print("Course passed?", student_2.course_passed())

print("Student 3:")
student_3.show_scores()
print("Average score:", student_3.score_average())
print("Course passed?", student_3.course_passed())

print("Student 4:")
student_4.show_scores()
print("Average score:", student_4.score_average())
print("Course passed?", student_4.course_passed())