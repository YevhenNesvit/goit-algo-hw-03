import os
import shutil
import argparse

def copy_files(src_dir, dest_dir):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            file_path = os.path.join(root, file)
            copy_file(file_path, dest_dir)

        for subdir in dirs:
            subdir_path = os.path.join(root, subdir)
            copy_files(subdir_path, dest_dir)

def copy_file(file_path, dest_dir):
    try:
        file_extension = os.path.splitext(file_path)[1][1:]
        dest_subdir = os.path.join(dest_dir, file_extension)

        if not os.path.exists(dest_subdir):
            os.makedirs(dest_subdir)

        shutil.copy(file_path, os.path.join(dest_subdir, os.path.basename(file_path)))
        print(f"Copied {file_path} to {dest_subdir}")

    except Exception as e:
        print(f"Error copying {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Recursive file copying and sorting")
    parser.add_argument("src_dir", help="Source directory path")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Destination directory path (default: dist)")
    args = parser.parse_args()

    if not os.path.exists(args.src_dir):
        print(f"Source directory '{args.src_dir}' does not exist.")
        return

    try:
        copy_files(args.src_dir, args.dest_dir)
        print("File copying and sorting completed successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()