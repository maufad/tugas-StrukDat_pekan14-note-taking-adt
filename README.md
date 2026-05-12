# tugas-StrukDat_pekan14-note-taking-adt
# Note-Taking ADT dengan Advanced Linked List

## Deskripsi
Implementasi struktur data untuk aplikasi note-taking dengan fitur:
- **Multi-linked by tag** → satu note bisa punya banyak tag
- **Doubly linked sorted** → chronological & alphabetical views
- **Sync status tracking** → circular buffer untuk perubahan terbaru

## Struktur Data yang Digunakan
| Fitur | Struktur Data |
|-------|---------------|
| Chronological view | Doubly Linked List (by timestamp) |
| Alphabetical view | Doubly Linked List (by title) |
| Multi-tag | Hash map + linked list per tag |
| Sync tracking | Circular buffer |

## Cara Menjalankan

```bash
python main.py
