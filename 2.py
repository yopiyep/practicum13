students = int(input())
common_courses = set(input().split())

for i in range(students - 1):
    student_courses = set(input().split())
    common_courses &= student_courses

print(len(common_courses))