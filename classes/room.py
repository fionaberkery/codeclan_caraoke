class Room:
    def __init__(self, name, max_capacity, entry_fee):
        self.name = name
        self.max_capacity = max_capacity
        self.entry_fee = entry_fee
        self.guests_in_room = []
        self.songs_to_sing= []
        self.queue = []
        self.cash = 0

    def how_many_guests(self):
        return len(self.guests_in_room)
    
    def check_in_guest(self, guest):
        if len(self.guests_in_room) >= self.max_capacity:
            self.queue.append(guest)
        else:
            self.guests_in_room.append(guest)
        
    def check_out_guest(self, guest):
        self.guests_in_room.remove(guest)

    def how_many_songs(self):
        return len(self.songs_to_sing)

    def add_song(self, song):
        self.songs_to_sing.append(song)

    def queue_length(self):
        return len(self.queue)

    def add_money(self, amount):
        self.cash += amount 
        return self.cash
