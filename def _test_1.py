def caption():
    print(f"{'Total bayaran':<15}{'jumlah orang':^15}{'tip':^15}{'total split bayaran':<15}")
def line():
    print("================================================================")
def calculate_split_bill(total_bill, number_of_people, tip_percentage):
    split_bill = (total_bill + (total_bill * tip_percentage)) / number_of_people
    return split_bill
total_bill = 300000
number_of_people = 4
tip_percentage = 0.10
total_split_bill = calculate_split_bill(total_bill, number_of_people, tip_percentage)

caption()
line()
print(f"{total_bill:<15}{number_of_people:^15}{tip_percentage:^15}{total_split_bill:<15}")