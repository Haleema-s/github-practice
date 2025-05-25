mathematics=int(input('enter your mathematics score'))
english=int(input('enter your english score'))
physics=int(input('enter your physics score'))
chemistry=int(input('enter your chemistry score'))
literature=int(input('enter your literature score'))

total = mathematics+english+physics+chemistry+literature
average = total/5

cgpa = average / 9.5

print(f"\nTotal: {total}")
print(f"Average: {average}")
print(f"CGPA: {cgpa}")