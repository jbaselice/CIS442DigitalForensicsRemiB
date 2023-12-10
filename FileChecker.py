import os
import magic


mime_types = { #Using Python Magic, the mime types are checking file types here.
     '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.gif': 'image/gif',
    '.txt': 'text/plain',
    '.html': 'text/html',
    '.pdf': 'application/pdf',
    '.doc': 'application/msword',
    '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    '.ppt': 'application/vnd.ms-powerpoint',
    '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    '.xls': 'application/vnd.ms-excel',
    '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    '.csv': 'text/csv',
    '.mp3': 'audio/mpeg',
    '.wav': 'audio/wav',
    '.mp4': 'video/mp4',
    '.mov': 'video/quicktime',
    '.avi': 'video/x-msvideo',
    # Add more mappings as needed
}

def get_file_signature(file_path):
    try:
        return magic.from_file(file_path, mime=True)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return None

def check_files_in_directory(directory):
    masqueraded_files = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_signature = get_file_signature(file_path)
            if file_signature:
                file_extension = os.path.splitext(filename)[1].lower()
                expected_mime_type = mime_types.get(file_extension)
                if expected_mime_type and file_signature != expected_mime_type:
                    masqueraded_files.append(file_path)
    return masqueraded_files

directory = input("Enter the directory path to check: ")
masqueraded_files = check_files_in_directory(directory)

if masqueraded_files:
    print("Found masqueraded files:")
    for file in masqueraded_files:
        print(file)
else:
    print("No masqueraded files found in the directory.")
