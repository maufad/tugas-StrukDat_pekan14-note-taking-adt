class Note:
    """Node untuk menyimpan satu note dalam doubly linked list"""

    def __init__(self, title, content, timestamp):
        self.title = title          # Judul note
        self.content = content      # Isi note
        self.timestamp = timestamp  # Waktu dibuat/diedit
        self.tags = []              # List of tag names

        # Untuk doubly linked list (chronological order)
        self.prev_time = None
        self.next_time = None

        # Untuk doubly linked list (alphabetical order)
        self.prev_alpha = None
        self.next_alpha = None

        # Sync status
        self.is_synced = True

    def __str__(self):
        return f"Note(title={self.title}, timestamp={self.timestamp}, tags={self.tags})"
