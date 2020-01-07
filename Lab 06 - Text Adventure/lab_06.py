def main():

    done = False
    room_list = []

    room = ["You are in the kitchen, there is a passage east and south", None, 1, 2, None]
    room_list.append(room)
    room = ["You are in the dining room, there is a passage west and south", None, None, 3, 0]
    room_list.append(room)
    room = ["You are in the walk-in entrance, there is a passage north, east and south", 0, 3, 4, None]
    room_list.append(room)
    room = ["You are in the living room, there is a passage north and west", 1, None, None, 2]
    room_list.append(room)
    room = ["You are in the first half of the hall, there is a passage north, east and south", 2, 5, 6, None]
    room_list.append(room)
    room = ["You are in the first bedroom, there is a passage west", None, None, None, 4]
    room_list.append(room)
    room = ["You are in the second half of the hall, there is a passage east and south", 4, 7, 8, None]
    room_list.append(room)
    room = ["You are in the master bedroom, there is a passage west", None, None, None, 6]
    room_list.append(room)
    room = ["You are in the second bedroom, there is a passage north", 6, None, None, None]
    room_list.append(room)

    current_room = room_list[0]

    print(current_room[0])


main()