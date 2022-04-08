class Room:
    def __init__(self, room_number, max_capacity):
        self.room_number = room_number
        self.max_capacity = max_capacity
        self.who_is_in_the_room = []

    def guest_list_count(self):
        return len(self.who_is_in_the_room)
    
    def add_guest(self, guest_to_add):
        self.who_is_in_the_room.append(guest_to_add)
        
    