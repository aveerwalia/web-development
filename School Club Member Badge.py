name = input("Enter yor name, Member:")
clubs = input("Enter your club:")

code = 8
points = 9.5

print("Member:", name, "-> type:", type(name))
print("Club:", clubs, "-> type:", type(clubs))
print("Code:", code, "-> type:", type(code))
print("Points:", points, "-> type:", type(points))

code_number_text = str(code)
points_count_text = str(points)

print("Code Number as text:", code_number_text, "-> type", type(code_number_text))
print("Points Count as text:", points_count_text, "-> type", type(points_count_text))


first_three = name[0:3]
last_letter = name[-1:]
code_name = first_three + last_letter
print("First 3 letters of name", first_three)
print("Last letter of name", last_letter)
print("Secret Code Name", code_name)

reversed_gadget = clubs[::-1]
print("Reversed Gadget Name:", reversed_gadget)

badge_line_1 = "MEMBER :" + code_name.upper()
badge_line_2 = "CLUB: " + clubs
badge_line_3 = "CODE: " + code_number_text
badge_line_4 = "POINTS: " + points_count_text  + " | ACTIVE: " + "Yes"

print("")
print("==== CLUB BADGE ====")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("====================")