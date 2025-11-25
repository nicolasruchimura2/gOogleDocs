import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import threading 
import queue
import time
import json
from datetime import datetime
from pathlib import Path

# @DocumentEditor
class DocumentEditor:
  # @selfRootDocumentEditor  
    def __init__(self, root):
        self.root = root
        self.roof.title("PyThreading DocEditor 1.0")
        self.root.geometry("1000x700")
        
        # State - everything initialized from 0 (reseted pattern)
        self.content = ""
        self.save_status = "Saved"
        self.word_count = 0
        self.char_count = 0
        self.collaborators = []
        self.auto_save_enabled = True

        # $ Threading with Queue $
        self.save_queue = queue.Queue()
        self.stats_queue = queue.Queue()
        self.collab_queue = queue.Queue()
        self.stop_threads = threading.Event()

        # UI Setup
        self.setup_ui()

        # Background threads
        self.start_background_threads()

        # Schedule UI updates
        self.update_ui_from_queues()

# UI Setup (Writing Editor) func, using Tkinter
    def setup_ui(self):
         header = tk.Frame(self.root, bg='#f8f9fa', height=100)
         header.pack(fill = tk.X, padx = 10, pady= 5)

         title_frame = tk.Frame(header, bg='#f8f9fa')
         title_frame.pack(side=tk.LEFT, padx=10)

         tk.Label(title_frame, font("Arial", 25), bg='#f8f9fa').pack(side= tk.LEFT)
         self.title_entry = tk.Entry(title_frame, font("Arial", 14), width= 20, relief= tk.FLAT, bg='#f8f9fa')
         self.title_entry.insert(0, "Untitled Document")
         self.title_entry.pack(side= tk.LEFT, padx= 5)
        # Status and controls - manipulating when it is or not saved.
         controls_frame = tk.Frame(header, bg='#f8f9fa')
         controls_frame.pack(side= tk.RIGHT, padx=10)
         self.status_label = tk.Label(controls_frame, text = "Saved", font= ("Arial", 10), bg='f8f9fa', fg= 'green')
         self.status_label.pack(side= tk.LEFT, padx= 10)

        
       
