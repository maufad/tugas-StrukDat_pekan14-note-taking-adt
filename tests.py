from note_manager import NoteManager
from sync_buffer import SyncBuffer
import time


def test_circular_buffer():
    print("🧪 TEST CIRCULAR BUFFER")
    buf = SyncBuffer(capacity=3)

    for i in range(5):
        dummy = type('Note', (), {})()
        dummy.title = f"Note{i}"
        dummy.timestamp = time.time()
        dummy.is_synced = False
        buf.add_change(dummy, "create")

    changes = buf.get_recent_changes()
    print(f"Jumlah perubahan (max 3): {len(changes)}")
    assert len(changes) == 3
    print("✓ Circular buffer test passed\n")


def test_multi_tag():
    print("🧪 TEST MULTI-TAG")
    app = NoteManager()

    note = app.create_note(
        title="Test Note",
        content="Testing tags",
        tags=["python", "struktur data", "tugas"]
    )

    assert len(app.get_notes_by_tag("python")) == 1
    assert len(app.get_notes_by_tag("struktur data")) == 1
    assert len(app.get_notes_by_tag("tugas")) == 1
    print("✓ Multi-tag test passed\n")


def test_doubly_linked_views():
    print("🧪 TEST DOUBLY LINKED VIEWS")
    app = NoteManager()

    app.create_note("C Note", "Content C", timestamp=100)
    app.create_note("A Note", "Content A", timestamp=300)
    app.create_note("B Note", "Content B", timestamp=200)

    chron = app.get_chronological_view()
    alpha = app.get_alphabetical_view()

    assert chron[0].title == "C Note"
    assert chron[1].title == "B Note"
    assert chron[2].title == "A Note"

    assert alpha[0].title == "A Note"
    assert alpha[1].title == "B Note"
    assert alpha[2].title == "C Note"

    print("✓ Doubly linked views test passed\n")


def test_sync_status():
    print("🧪 TEST SYNC STATUS")
    app = NoteManager()
    buf = SyncBuffer(capacity=5)

    note = app.create_note("Sync Test", "Content")
    buf.add_change(note, "create")

    assert note.is_synced == False
    assert len(buf.get_unsynced_changes()) == 1

    buf.mark_all_synced()
    assert len(buf.get_unsynced_changes()) == 0

    print("✓ Sync status test passed\n")


if __name__ == "__main__":
    print("=" * 40)
    print("RUNNING TESTS")
    print("=" * 40)
    test_circular_buffer()
    test_multi_tag()
    test_doubly_linked_views()
    test_sync_status()
    print("=" * 40)
    print("ALL TESTS PASSED! ✅")
