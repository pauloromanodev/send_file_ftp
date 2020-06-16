from ftplib import FTP
from pathlib import Path

file_path = Path('C:\\SOME_FOLDER\\YOUR_FILE.csv')

with FTP('FTP_IP_ADDRESS', 'FTP_USER', 'FTP_PASSWORD') as ftp, open(file_path, 'rb') as file:
    ftp.storbinary(f'STOR {file_path.name}', file)
