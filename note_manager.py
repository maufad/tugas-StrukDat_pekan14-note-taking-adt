from note import Note
from tag import TagNode


class NoteManager:
    """Manajer utama note-taking dengan multi-linked structure"""

    def __init__(self):
        # Chronological doubly linked list (by time)
        self.chron_head = None      # oldest
        self.chron_tail = None      # newest

        # Alphabetical doubly linked list (by title)
        self.alpha_head = None
        self.alpha_tail = None

        # Tag index: tag_name -> TagNode
        self.tag_index = {}

    # ========== OPERASI CHRONOLOGICAL ==========

    def _insert_chronological(self, note):
        """Sisipkan note ke chronological linked list (sorted by time)"""
        if not self.chron_head:
            self.chron_head = self.chron_tail = note
            return

        if note.timestamp <= self.chron_head.timestamp:
            # Insert di awal
            note.next_time = self.chron_head
            self.chron_head.prev_time = note
            self.chron_head = note
            return

        current = self.chron_head
        while current.next_time and current.next_time.timestamp < note.timestamp:
            current = current.next_time

        # Insert after current
        note.next_time = current.next_time
        note.prev_time = current

        if current.next_time:
            current.next_time.prev_time = note
        else:
            self.chron_tail = note

        current.next_time = note

    # ========== OPERASI ALPHABETICAL ==========

    def _insert_alphabetical(self, note):
        """Sisipkan note ke alphabetical linked list (sorted by title)"""
        if not self.alpha_head:
            self.alpha_head = self.alpha_tail = note
            return

        if note.title.lower() <= self.alpha_head.title.lower():
            note.next_alpha = self.alpha_head
            self.alpha_head.prev_alpha = note
            self.alpha_head = note
            return

        current = self.alpha_head
        while current.next_alpha and current.next_alpha.title.lower() < note.title.lower():
            current = current.next_alpha

        note.next_alpha = current.next_alpha
        note.prev_alpha = current

        if current.next_alpha:
            current.next_alpha.prev_alpha = note
        else:
            self.alpha_tail = note

        current.next_alpha = note

    # ========== TAG MANAGEMENT ==========

    def _add_note_to_tag(self, note, tag_name):
        """Tambahkan note ke tag tertentu"""
        if tag_name not in self.tag_index:
            self.tag_index[tag_name] = TagNode(tag_name)

        self.tag_index[tag_name].add_note(note)

        if tag_name not in note.tags:
            note.tags.append(tag_name)

    # ========== OPERASI CRUD NOTE ==========

    def create_note(self, title, content, tags=None, timestamp=None):
        """Buat note baru"""
        import time
        if timestamp is None:
            timestamp = time.time()

        new_note = Note(title, content, timestamp)

        # Insert ke kedua list
        self._insert_chronological(new_note)
        self._insert_alphabetical(new_note)

        # Tambahkan ke tag
        if tags:
            for tag in tags:
                self._add_note_to_tag(new_note, tag)

        return new_note

    def update_note(self, note, new_title=None, new_content=None):
        """Update note dan tandai sebagai belum sync"""
        if new_title:
            # Hapus dari alphabetical list
            self._remove_from_alphabetical(note)
            note.title = new_title
            self._insert_alphabetical(note)

        if new_content:
            note.content = new_content

        # Update timestamp
        import time
        note.timestamp = time.time()

        # Update chronological position
        self._remove_from_chronological(note)
        self._insert_chronological(note)

        note.is_synced = False

    def _remove_from_chronological(self, note):
        """Hapus note dari chronological linked list"""
        if note.prev_time:
            note.prev_time.next_time = note.next_time
        else:
            self.chron_head = note.next_time

        if note.next_time:
            note.next_time.prev_time = note.prev_time
        else:
            self.chron_tail = note.prev_time

        note.prev_time = None
        note.next_time = None

    def _remove_from_alphabetical(self, note):
        """Hapus note dari alphabetical linked list"""
        if note.prev_alpha:
            note.prev_alpha.next_alpha = note.next_alpha
        else:
            self.alpha_head = note.next_alpha

        if note.next_alpha:
            note.next_alpha.prev_alpha = note.prev_alpha
        else:
            self.alpha_tail = note.prev_alpha

        note.prev_alpha = None
        note.next_alpha = None

    def delete_note(self, note):
        """Hapus note"""
        self._remove_from_chronological(note)
        self._remove_from_alphabetical(note)

        # Hapus dari semua tag
        for tag_name in note.tags[:]:
            if tag_name in self.tag_index:
                self.tag_index[tag_name].remove_note(note)

        note.tags = []

    # ========== VIEWS ==========

    def get_chronological_view(self):
        """Tampilkan note secara kronologis (terlama ke terbaru)"""
        result = []
        current = self.chron_head
        while current:
            result.append(current)
            current = current.next_time
        return result

    def get_alphabetical_view(self):
        """Tampilkan note secara alfabetis (A-Z)"""
        result = []
        current = self.alpha_head
        while current:
            result.append(current)
            current = current.next_alpha
        return result

    def get_notes_by_tag(self, tag_name):
        """Tampilkan note berdasarkan tag"""
        result = []
        if tag_name in self.tag_index:
            current = self.tag_index[tag_name].notes_head
            while current:
                result.append(current.note)
                current = current.next
        return result
