class Room:
    def __init__(self, room_number, max_capacity):
        self.room_number = room_number
        self.max_capacity = max_capacity
        self.who_is_in_the_room = []

    def guest_list_count(self):
        return len(self.who_is_in_the_room)
    
    def check_in_guest(self, guest):
        self.who_is_in_the_room.append(guest)
        
    def check_out_guest(self, guest):
        self.who_is_in_the_room.remove(guest)
