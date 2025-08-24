import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import pillow_heif
import os
import threading

class HEICConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("HEIC to JPG/PNG Converter")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Register HEIF opener with Pillow
        pillow_heif.register_heif_opener()
        
        # Variables
        self.files_to_convert = []
        self.output_format = tk.StringVar(value="JPG")
        self.output_folder = tk.StringVar(value=os.getcwd())
        
        # Create UI
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="HEIC to JPG/PNG Converter", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Select files button
        select_btn = tk.Button(self.root, text="Select HEIC Files", command=self.select_files, 
                              bg="#4CAF50", fg="white", font=("Arial", 12), width=20)
        select_btn.pack(pady=10)
        
        # File list
        list_frame = tk.Frame(self.root)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        list_label = tk.Label(list_frame, text="Selected Files:", font=("Arial", 10))
        list_label.pack(anchor=tk.W)
        
        self.file_listbox = tk.Listbox(list_frame, selectmode=tk.EXTENDED, height=8)
        self.file_listbox.pack(fill=tk.BOTH, expand=True, pady=5)
        
        scrollbar = tk.Scrollbar(self.file_listbox)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.file_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.file_listbox.yview)
        
        # Output format selection
        format_frame = tk.Frame(self.root)
        format_frame.pack(fill=tk.X, padx=20, pady=10)
        
        format_label = tk.Label(format_frame, text="Output Format:", font=("Arial", 10))
        format_label.pack(side=tk.LEFT)
        
        jpg_radio = tk.Radiobutton(format_frame, text="JPG", variable=self.output_format, value="JPG")
        jpg_radio.pack(side=tk.LEFT, padx=10)
        
        png_radio = tk.Radiobutton(format_frame, text="PNG", variable=self.output_format, value="PNG")
        png_radio.pack(side=tk.LEFT, padx=10)
        
        # Output folder selection
        folder_frame = tk.Frame(self.root)
        folder_frame.pack(fill=tk.X, padx=20, pady=10)
        
        folder_label = tk.Label(folder_frame, text="Output Folder:", font=("Arial", 10))
        folder_label.pack(anchor=tk.W)
        
        folder_select_frame = tk.Frame(folder_frame)
        folder_select_frame.pack(fill=tk.X, pady=5)
        
        folder_entry = tk.Entry(folder_select_frame, textvariable=self.output_folder, font=("Arial", 10))
        folder_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        folder_btn = tk.Button(folder_select_frame, text="Browse", command=self.select_output_folder, width=10)
        folder_btn.pack(side=tk.RIGHT, padx=(5, 0))
        
        # Progress bar
        self.progress = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=500, mode='determinate')
        self.progress.pack(pady=10)
        
        # Convert button
        self.convert_btn = tk.Button(self.root, text="Convert", command=self.start_conversion, 
                                    bg="#2196F3", fg="white", font=("Arial", 12), width=20, state=tk.DISABLED)
        self.convert_btn.pack(pady=10)
        
        # Status label
        self.status_label = tk.Label(self.root, text="Select HEIC files to begin", font=("Arial", 10))
        self.status_label.pack(pady=5)
    
    def select_files(self):
        filetypes = [("HEIC files", "*.heic"), ("HEIC files", "*.HEIC"), ("All files", "*.*")]
        filenames = filedialog.askopenfilenames(title="Select HEIC files", filetypes=filetypes)
        
        if filenames:
            self.files_to_convert = list(filenames)
            self.file_listbox.delete(0, tk.END)
            for file in self.files_to_convert:
                self.file_listbox.insert(tk.END, os.path.basename(file))
            
            self.convert_btn.config(state=tk.NORMAL)
            self.status_label.config(text=f"Selected {len(self.files_to_convert)} file(s)")
    
    def select_output_folder(self):
        folder = filedialog.askdirectory(title="Select output folder")
        if folder:
            self.output_folder.set(folder)
    
    def start_conversion(self):
        if not self.files_to_convert:
            messagebox.showerror("Error", "No files selected for conversion")
            return
            
        # Disable convert button during conversion
        self.convert_btn.config(state=tk.DISABLED)
        
        # Start conversion in a separate thread to keep UI responsive
        thread = threading.Thread(target=self.convert_files)
        thread.daemon = True
        thread.start()
    
    def convert_files(self):
        total_files = len(self.files_to_convert)
        successful = 0
        
        for i, file_path in enumerate(self.files_to_convert):
            try:
                # Update progress
                self.root.after(0, self.update_progress, i, total_files)
                self.root.after(0, self.update_status, f"Converting {i+1}/{total_files}: {os.path.basename(file_path)}")
                
                # Open HEIC file
                image = Image.open(file_path)
                
                # Determine output path
                filename = os.path.splitext(os.path.basename(file_path))[0]
                output_path = os.path.join(self.output_folder.get(), f"{filename}.{self.output_format.get().lower()}")
                
                # Convert and save
                if self.output_format.get() == "JPG":
                    # Convert to RGB for JPG as it doesn't support transparency
                    if image.mode in ("RGBA", "P"):
                        image = image.convert("RGB")
                    image.save(output_path, "JPEG", quality=95)
                else:
                    image.save(output_path, "PNG")
                
                successful += 1
                
            except Exception as e:
                self.root.after(0, self.show_error, f"Failed to convert {os.path.basename(file_path)}: {str(e)}")
        
        # Update progress to complete
        self.root.after(0, self.update_progress, total_files, total_files)
        
        # Show completion message
        self.root.after(0, self.conversion_complete, successful, total_files)
    
    def update_progress(self, current, total):
        self.progress['value'] = (current / total) * 100
        self.root.update_idletasks()
    
    def update_status(self, message):
        self.status_label.config(text=message)
    
    def show_error(self, message):
        messagebox.showerror("Conversion Error", message)
    
    def conversion_complete(self, successful, total):
        self.convert_btn.config(state=tk.NORMAL)
        self.status_label.config(text=f"Conversion complete: {successful}/{total} files converted successfully")
        messagebox.showinfo("Complete", f"Conversion complete: {successful}/{total} files converted successfully")

if __name__ == "__main__":
    root = tk.Tk()
    app = HEICConverter(root)
    root.mainloop()
