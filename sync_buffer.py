class SyncBuffer:
    """
    Circular buffer untuk tracking sync status perubahan terbaru
    """

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0          # Posisi untuk write berikutnya
        self.count = 0         # Jumlah item terisi
        self.changes = []      # Untuk menyimpan perubahan terbaru (opsional)

    def add_change(self, note, change_type):
        """Tambahkan perubahan ke circular buffer"""
        change = {
            'note_title': note.title,
            'change_type': change_type,  # 'create', 'update', 'delete'
            'timestamp': note.timestamp,
            'synced': note.is_synced
        }

        self.buffer[self.head] = change
        self.head = (self.head + 1) % self.capacity

        if self.count < self.capacity:
            self.count += 1

        # Tandai note sebagai belum sync
        note.is_synced = False

    def get_recent_changes(self):
        """Dapatkan perubahan terbaru (dari yang terlama ke terbaru)"""
        if self.count == 0:
            return []

        result = []
        start = (self.head - self.count) % self.capacity

        for i in range(self.count):
            idx = (start + i) % self.capacity
            if self.buffer[idx]:
                result.append(self.buffer[idx])

        return result

    def mark_all_synced(self):
        """Tandai semua perubahan sebagai sudah disync"""
        for i in range(self.capacity):
            if self.buffer[i]:
                self.buffer[i]['synced'] = True

    def get_unsynced_changes(self):
        """Dapatkan perubahan yang belum disync"""
        return [c for c in self.get_recent_changes() if not c['synced']]
