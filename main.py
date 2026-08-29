import os
import glob
import subprocess

# Main project folder
PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))


def open_file(folder, extension):
    """Find and open the first matching file inside a folder."""
    folder_path = os.path.join(PROJECT_FOLDER, folder)

    files = glob.glob(os.path.join(folder_path, f"*.{extension}"))

    if not files:
        print(f"\nNo .{extension} file found inside {folder}")
        return

    file_path = files[0]

    print(f"\nOpening: {os.path.basename(file_path)}")
    os.startfile(file_path)


print("=" * 60)
print(" REAL ESTATE LEAD GENERATION & CONVERSION ANALYTICS")
print("=" * 60)

while True:

    print("\nChoose an option:")
    print("1. Run Python Analysis")
    print("2. Open Excel Dashboard")
    print("3. Open Power BI Dashboard")
    print("4. Open SQL Queries")
    print("5. Open Charts Folder")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        print("\nRunning Python Analysis...")

        python_files = glob.glob(
            os.path.join(PROJECT_FOLDER, "_python", "*.py")
        )

        if python_files:
            subprocess.run(["python", python_files[0]])
        else:
            print("Python analysis file not found.")

    elif choice == "2":

        open_file("_Excel", "xlsx")

    elif choice == "3":

        open_file("_Powerbi", "pbix")

    elif choice == "4":

        open_file("_SQL", "sql")

    elif choice == "5":

        charts_folder = os.path.join(PROJECT_FOLDER, "charts")

        if os.path.exists(charts_folder):
            os.startfile(charts_folder)
        else:
            print("Charts folder not found.")

    elif choice == "6":

        print("\nProject closed.")
        break

    else:

        print("\nInvalid choice. Please enter 1 to 6.")