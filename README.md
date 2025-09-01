
```markdown
# 🗂️ Python File Organizer

A simple Python script that automatically organizes files into folders based on their extensions (PDFs, Images, Docs, Music, Videos, Others).  
This project demonstrates **automation using Python**.

---

## 🚀 Features
- Automatically sorts files into categorized folders:
  - **PDFs** → `.pdf`
  - **Images** → `.jpg`, `.jpeg`, `.png`, `.gif`
  - **Docs** → `.doc`, `.docx`, `.txt`, `.ppt`, `.pptx`, `.xls`, `.xlsx`
  - **Music** → `.mp3`, `.wav`, `.aac`
  - **Videos** → `.mp4`, `.mkv`, `.avi`
  - **Others** → Any unknown file types
- Creates folders automatically if they don’t exist.
- Works on **Windows, Mac, and Linux**.
- Easy to customize with your own categories and extensions.

---

## 📂 Project Structure
```

File-Organizer/
│-- file\_organizer.py   # Main script
│-- README.md           # Documentation
│-- /TestFiles          # (Optional) Put sample files here for testing

````

---

## ⚙️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python-file-organizer.git
   cd python-file-organizer
````

2. Run the script:

   ```bash
   python file_organizer.py
   ```

3. Place files in the target folder → script will create subfolders (`PDFs`, `Images`, `Docs`, etc.) and move files accordingly.

---

## 🛠️ How It Works

1. The script scans all files inside the selected folder.
2. It checks each file’s **extension** (e.g., `.pdf`, `.jpg`, `.docx`).
3. Based on the extension, it decides the **category** (PDFs, Images, Docs, etc.).
4. If the target category folder does not exist, it is created automatically.
5. The file is then **moved** into the correct folder using Python’s `shutil.move()`.
6. If a file doesn’t match any category, it is moved into the **Others** folder.

This ensures your folder stays clean and organized automatically.

---

## 🔧 Configuration

By default, the script organizes files in the **same folder where it is placed**.

* If you want to specify a **custom folder**, edit this line in `file_organizer.py`:

  ```python
  folder_to_organize = r"C:\Users\YourName\Downloads\filesorter"
  ```

* Or keep it **auto-detecting current folder**:

  ```python
  folder_to_organize = os.path.dirname(os.path.abspath(__file__))
  ```

---

## 🖼️ Example

**Before:**

```
Downloads/
├── project.pdf
├── photo.png
├── resume.docx
├── song.mp3
├── randomfile.xyz
```

**After running the script:**

```
Downloads/
├── PDFs/project.pdf
├── Images/photo.png
├── Docs/resume.docx
├── Music/song.mp3
├── Others/randomfile.xyz
```


Do you want me to also prepare a **`requirements.txt`** (even though this script only uses built-in Python libraries) just so your repo looks more professional?
```
