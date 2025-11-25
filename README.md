# Python Threaded Document Editor

A lightweight, Google Docs-inspired collaborative document editor built with Python's `tkinter` and `threading` libraries. This project demonstrates best practices for building responsive GUI applications using background threads.

**The development was, primarily, designed with Visual Paradigm, and previous researches around.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

### Core Functionality
- 📝 **Rich Text Editing** - Clean, distraction-free writing interface
- 💾 **Auto-Save** - Automatic background saving every 2 seconds
- 📊 **Real-time Statistics** - Live word and character counting
- 👥 **Collaborative Indicators** - Visual representation of active collaborators
- 📤 **Document Export** - Save documents to any location
- 🎨 **Text Formatting** - Bold, italic, and underline support

### Technical Highlights
- **Multi-threaded Architecture** - Non-blocking UI with background workers
- **Thread-Safe Communication** - Queue-based inter-thread messaging
- **Graceful Shutdown** - Proper cleanup of all threads
- **No External Dependencies** - Pure Python standard library

## Installation

### Requirements
- Python 3.7 or higher
- No additional packages required (uses standard library)

### Setup

1. Clone or download the repository:
```bash
git clone https://github.com/yourusername/python-doc-editor.git
cd python-doc-editor
```

2. Run the application:
```bash
python document_editor.py
```

That's it! No virtual environment or dependency installation needed.

## Usage

### Basic Operations

**Starting a New Document**
1. Launch the application
2. Start typing in the editor
3. The document auto-saves to `~/.doc_editor/autosave.json`

**Formatting Text**
1. Select the text you want to format
2. Click the toolbar buttons:
   - **B** - Bold (wraps in `**text**`)
   - **I** - Italic (wraps in `*text*`)
   - **U** - Underline (wraps in `__text__`)

**Exporting Documents**
1. Click the "Export" button
2. Choose a location and filename
3. Save as `.txt` or any format you prefer

**Monitoring Statistics**
- View real-time word and character count in the footer
- Updates automatically as you type

**Collaborators**
- Simulated collaborators appear every 8 seconds
- Shows up to 3 active users with colored avatars

## Architecture

### Threading Model

#### 1. Main Thread (UI Thread)
- Handles all GUI rendering and user interactions
- Updates display based on messages from worker threads
- Never performs blocking operations

**Features:**
- Demonstrates multi-user simulation
- Thread-safe UI updates
- Realistic collaboration feel

### Thread Communication

The application uses Python's `queue.Queue` for thread-safe communication:

```python
# Queues for inter-thread communication
self.save_queue = queue.Queue()      # Main → Auto-save
self.stats_queue = queue.Queue()     # Main → Statistics
self.collab_queue = queue.Queue()    # Collaborator → Main
```

**Why Queues?**
- Thread-safe by design
- FIFO (First In, First Out) ordering
- Blocking/non-blocking options
- Built-in synchronization

### GUI Thread Safety

`tkinter` is **not thread-safe**. All GUI updates must occur on the main thread:

```python
# ✅ CORRECT: Schedule UI update on main thread
self.root.after(0, lambda: self.update_status("Saved", "green"))

## Advanced Topics

### Adding Real Collaboration

To make this a true collaborative editor, you would need:

1. **WebSocket Server** - For real-time communication
   ```python
   import asyncio
   import websockets
   ```

2. **Operational Transformation (OT)** - For conflict resolution
   - Or use CRDTs (Conflict-free Replicated Data Types)

3. **User Authentication** - Track who's editing
4. **Cursor Position Sync** - Show where others are typing

### Database Integration

Replace JSON file storage with a database:

```python
import sqlite3

def save_to_db(content, title):
    conn = sqlite3.connect('documents.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO documents (title, content, timestamp)
        VALUES (?, ?, ?)
    ''', (title, content, datetime.now()))
    conn.commit()
    conn.close()
```

### Debug Mode

Add logging to track thread behavior:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# In worker threads
logger.debug(f"Auto-save triggered for content length: {len(content)}")
```

## Performance Tips

1. **Debouncing** - Already implemented for auto-save
2. **Queue Draining** - Get latest data before processing
3. **Daemon Threads** - Worker threads are marked as daemon for clean exit
4. **Minimal UI Updates** - Only update when values change

## License

MIT License - feel free to use this project for learning or commercial purposes.

## Acknowledgments

- Inspired by Google Docs and collaborative editing tools
- Built with Python's excellent standard library
- Threading patterns based on Python's official documentation

## Contact

For questions, issues, or suggestions:
- Open an issue on GitHub
- Email: nicolasruchimura@gmail.com
