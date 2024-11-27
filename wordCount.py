import os
from bs4 import BeautifulSoup

def count_word_in_html_file(file_path, word):
    """ 주어진 HTML 파일에서 특정 단어의 출현 횟수를 계산하는 함수 """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # BeautifulSoup를 사용하여 HTML 태그를 제거한 텍스트만 추출
            soup = BeautifulSoup(content, 'html.parser')
            text = soup.get_text()
            # 특정 단어의 등장 횟수 계산 (대소문자 구분 없음)
            return text.lower().count(word.lower())
    except Exception as e:
        print(f"파일 읽기 오류: {file_path} - {e}")
        return 0

def count_word_in_folder(folder_path, word):
    """ 지정한 폴더에서 모든 HTML 파일을 확인하여 특정 단어의 총 출현 횟수를 계산하는 함수 """
    total_count = 0
    global checkCount
    checkCount = 0
    # 폴더 내의 모든 파일을 확인
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.htm'):
                file_path = os.path.join(root, file)
                word_count = count_word_in_html_file(file_path, word)
                total_count += word_count
                checkCount += 1
                if word_count > 0:
                    print(file_path + str(checkCount) + f"파일: {file}, 단어 '{word}' 등장 횟수: {word_count}")
    return total_count

# 예시 사용법
# folder_path = "C:/example/folder"  # HTML 파일이 들어 있는 폴더 경로
folder_path = r"C:\python\wordCount-main"
checkCount = 0
while(1):
    word = input()  # 찾고 싶은 단어
    total_word_count = count_word_in_folder(folder_path, word)
    print(f"\n총 단어 '{word}' 등장 횟수: {total_word_count}")
