class TagNode:
    """Node untuk menyimpan tag dengan linked list of notes"""

    def __init__(self, name):
        self.name = name
        self.notes_head = None   # Head linked list note dalam tag ini
        self.next_tag = None     # Untuk linked list antar tag

    def add_note(self, note):
        """Tambahkan note ke tag ini (di awal)"""
        new_node = NoteRef(note)
        new_node.next = self.notes_head
        self.notes_head = new_node

    def remove_note(self, note):
        """Hapus note dari tag ini"""
        current = self.notes_head
        prev = None
        while current:
            if current.note is note:
                if prev:
                    prev.next = current.next
                else:
                    self.notes_head = current.next
                return True
            prev = current
            current = current.next
        return False


class NoteRef:
    """Referensi ke note dalam linked list tag"""

    def __init__(self, note):
        self.note = note
        self.next = None
