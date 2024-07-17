def opposite_face(face):
    if face < 1 or face > 6:
        return "Invalid face number"
    else:
        return 7 - face

face_number = int(input("Enter the face number of the dice: "))
print("The opposite face of number is:", opposite_face(face_number))