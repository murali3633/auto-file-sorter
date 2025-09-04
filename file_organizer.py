import os
import shutil

# Define file categories 
FILE_CATEGORIES = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Docs": [".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Others": []
}
 
def organize_files(source_folder):
    # Make sure the folder exists
    if not os.path.exists(source_folder):
        print("Source folder not found!")
        return

    # Loop through all files in the folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Find category for the file
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if ext in extensions:
                category_folder = os.path.join(source_folder, category)
                os.makedirs(category_folder, exist_ok=True)  # Create folder if not exists
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved: {filename} → {category}/")
                moved = True
                break

        # If no category found → Others
        if not moved:
            category_folder = os.path.join(source_folder, "Others")
            os.makedirs(category_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(category_folder, filename))
            print(f"Moved: {filename} → Others/")

if __name__ == "__main__":
    # Change this path to the folder you want to organize
    folder_to_organize = r"C:\Users\91739\Downloads\filesorter"

    organize_files(folder_to_organize)


 
