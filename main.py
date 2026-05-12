from note_manager import NoteManager
from sync_buffer import SyncBuffer
import time


def main():
    print("=" * 60)
    print("NOTE-TAKING APP dengan Advanced Linked List")
    print("=" * 60)

    # Inisialisasi
    app = NoteManager()
    sync = SyncBuffer(capacity=5)

    # Buat beberapa note
    print("\n📝 MEMBUAT NOTE:")
    note1 = app.create_note(
        title="Belajar Struktur Data",
        content="Linked List, Queue, Stack",
        tags=["kuliah", "python"],
        timestamp=time.time() - 3600
    )
    sync.add_change(note1, "create")
    print(f"✓ {note1.title}")

    time.sleep(1)

    note2 = app.create_note(
        title="Tugas Advanced Linked List",
        content="Multi-linked, doubly linked, circular buffer",
        tags=["tugas", "struktur_data"],
        timestamp=time.time()
    )
    sync.add_change(note2, "create")
    print(f"✓ {note2.title}")

    time.sleep(1)

    note3 = app.create_note(
        title="Review Materi",
        content="Review linked list untuk ujian",
        tags=["review", "kuliah"],
        timestamp=time.time()
    )
    sync.add_change(note3, "create")
    print(f"✓ {note3.title}")

    # Update note
    print("\n✏️ UPDATE NOTE:")
    app.update_note(note2, new_title="Tugas Advanced Linked List - DONE")
    sync.add_change(note2, "update")
    print(f"✓ {note2.title} (updated)")

    # Tampilkan views
    print("\n" + "=" * 60)
    print("📚 CHRONOLOGICAL VIEW (terlama → terbaru):")
    print("=" * 60)
    for note in app.get_chronological_view():
        print(f"  [{time.ctime(note.timestamp)}] {note.title}")

    print("\n" + "=" * 60)
    print("🔤 ALPHABETICAL VIEW (A → Z):")
    print("=" * 60)
    for note in app.get_alphabetical_view():
        print(f"  {note.title}")

    print("\n" + "=" * 60)
    print("🏷️ NOTES BY TAG 'kuliah':")
    print("=" * 60)
    for note in app.get_notes_by_tag("kuliah"):
        print(f"  {note.title}")

    # Tampilkan sync buffer
    print("\n" + "=" * 60)
    print("🔄 RECENT CHANGES (Circular Buffer, cap=5):")
    print("=" * 60)
    for change in sync.get_recent_changes():
        status = "✅ synced" if change['synced'] else "⏳ pending"
        print(f"  [{change['change_type']}] {change['note_title']} - {status}")

    print("\n" + "=" * 60)
    print("✅ SIMULASI SELESAI")
    print("=" * 60)


if __name__ == "__main__":
    main()
