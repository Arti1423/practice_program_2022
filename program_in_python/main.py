import patterns.pyramid as p
import patterns.reverse_pyramid as rev
import patterns.right_angle as rig
# from patterns import reverse_pyramid as rev

pyramid_list = ["Pyramid", "Reverse Pyramid", "Right Angle Triangle"]
obj_list = {
    "Pyramid": p.pyramid,
    "Reverse Pyramid": rev.reverse_pyramid,
    "Right Angle Triangle": rig.right_angle
}

print("Pyramid patterns List:")
for index, i in enumerate(pyramid_list):
    index = index + 1
    print(f"{index}. {i}.")

x = input("Please enter the number from list to run the coresponding program.\n")
n = input("Enter the number of row value.\n")

obj_list[pyramid_list[int(x)-1]](int(n))
