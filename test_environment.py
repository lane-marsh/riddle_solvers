import random

"""
Riddle:
100 people are waiting to board a plane. The first person’s
ticket says Seat 1; the second person in line has a ticket
that says Seat 2, and so on until the 100th person, whose
ticket says Seat 100. The first person ignores the fact that
his ticket says Seat 1, and randomly chooses one of the
hundred seats (note: he might randomly choose to sit in Seat
1). From this point on, the next 98 people will always sit
in their assigned seats if possible; if their seat is taken,
they will randomly choose one of the remaining seats (after
the first person, the second person takes a seat; after the
second person, the third person takes a seat, and so on).
What is the probability the 100th person sits in Seat 100?
"""


seats_input = 100
iterations = 10 ** 5


def remove_random(seat_list):

    choice = random.choice(seat_list)
    seat_list.remove(choice)

    return seat_list


def seat_taken_test(seats):

    # return variables
    seat_is_taken = False
    random_choice_count = 1

    available_seats = []
    for seat in range(seats):
        available_seats.append(seat + 1)

    for passenger in range(seats - 1):
        passenger += 1
        if passenger in available_seats and passenger != 1:
            available_seats.remove(passenger)
        else:
            random_choice_count += 1
            remove_random(available_seats)

    if available_seats[0] == seats:
        seat_is_taken = True

    return seat_is_taken, random_choice_count


seat_taken_count = 0
average_choices_sum = 0
for iteration in range(iterations):
    realization_result, realization_random_choices = seat_taken_test(seats_input)
    average_choices_sum += realization_random_choices
    if realization_result:
        seat_taken_count += 1

print('Percentage of realizations with final seat taken: ' + "{:.1%}".format(seat_taken_count / iterations * 1.0))
print('Average random choices per realization: ' + str(average_choices_sum / iterations))
