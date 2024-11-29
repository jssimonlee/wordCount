import re
from bs4 import BeautifulSoup
import os

# 현재 폴더 아래의 모든 htm, xhtml 파일의 Tag를 삭제
for root, dirs, files in os.walk('./'):
    for file in files:
        if file.endswith('.htm') or file.endswith('.xhtml'):
            file_path = os.path.join(root, file)
            text = ''
            with open(file_path, 'r', encoding='utf-8') as file:
                # HTML 내용 읽기
                content = file.read()
                # BeautifulSoup을 사용하여 HTML 태그 제거
                soup = BeautifulSoup(content, 'html')
                text = soup.get_text()  # HTML 태그를 제거하고 텍스트만 추출
            with open(file_path, 'w' , encoding='utf-8') as file:
                file.write(text)
