import os

def handle_upload(file_name, file_content):
    file_path = os.path.join('/tmp', file_name)
    with open(file_path, 'wb') as f:
        f.write(file_content)
    return file_path
