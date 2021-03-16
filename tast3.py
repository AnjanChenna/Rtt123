data_about_rooms = [
    [7.11, 8, '9:00', '9:15', '14:30', '15:00'],
    [8.23, 6, '10:00', '11:00', '14:00', '15:00'],
    [8.43, 7, '11:30', '12:30', '17:00', '17:30'],
    [9.511, 9, '9:30', '10:30', '12:00', '12:15', '15:15', '16:15', "1:00", "6:00"],
    [9.527, 4, '9:00', '11:00', '14:00', '16:00'],
    [9.547, 8, '10:30', '11:30', '13:30', '15:30', '16:30', '17:30', '9:30', '10:30', '12:00', '12:15', '15:15', '16:15', "1:00", "6:00"]
]
# members , in_time , out_time
## floor_no, members , in_time , out_time ------
def best_room(members, in_time, out_time):
    for item in data_about_rooms:
        # print(item[1]) #-- [7.11, 8, '9:00', '9:15', '14:30', '15:00']
        if item[1] >=members:
            # loop each subitem starting from index 2: max
            # for in_out_time in item[2:]:    # ['9:00', '9:15', '14:30', '15:00']
            for time_item in range(2, len(item),2):
                if in_time == item[time_item] and out_time == item[time_item+1]:
                    return "best room is {}".format(item[0])
    return "No rooms"


print(best_room(5, "1:00", "6:00"))
# best_room(9, 4, '12:00', '12:15')

a = [1,2,3,4,5,6]
# for i in a:
i = 10
if i ==2:
    if i+1 == 3:
        print('222')
    elif i+1 == 4:
        print('33333')
elif i ==4:


