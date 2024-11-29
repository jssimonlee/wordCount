import os
from bs4 import BeautifulSoup
import re
import warnings

# 모든 경고를 무시
warnings.filterwarnings("ignore")

# 현재폴더 아래에 있는 epub 안에 있는 htm 문서 안에서 특정 단어가 몇번 반복되는지 검사

def count_word_in_html_file(file_path, target_word):
    """ 주어진 HTML 파일에서 특정 단어의 출현 횟수를 계산하는 함수 """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # BeautifulSoup를 사용하여 HTML 태그를 제거한 텍스트만 추출
            soup = BeautifulSoup(content, 'html.parser')
            text = soup.get_text()
            # 특정 단어의 등장 횟수 계산 (대소문자 구분 없음)
            if '-' not in target_word:
                word_count = text.lower().count(target_word.lower())
            else:
                word = target_word.split('-')
                word_count = text.lower().count(word[0].lower().strip()) - text.lower().count(word[1].lower().strip())
            if word_count > 0:
                if file_path.count('권'):
                    volume = file_path.split("권")[0][-6:] + '권'
                else:
                    volume = "_".join(file_path.split("\\")[-2:-1])
                if file_path.count('_r1'):
                    chapter = file_path.split("_r1")[0].split("c")[1]
                elif file_path.count('Ch'):
                    chapter = file_path.split("Ch")[-1].split('.')[0]
                elif file_path.count('ch'):
                    chapter = file_path.split("ch")[-1].split('.')[0]
                else:
                    chapter = file_path.split("\\")[-1].split('.')[0]
                print(f"{volume} Ch {chapter} : {word_count}번 등장")
                sentences = find_sentences_with_word_in_html(file_path, target_word)
                for sen in sentences:
                    # print(sen.replace('“','').replace('”','').replace('\n','').strip() + '.')
                    if sen[0] == '”':
                        sen = sen[1:]
                    print(sen.replace('\n','').strip() + '.')
                print()
            return word_count
    except Exception as e:
        print(f"파일 읽기 오류: {file_path} - {e}")
        return 0

def count_word_in_folder(folder_path, target_word):
    """ 지정한 폴더에서 모든 HTML 파일을 확인하여 특정 단어의 총 출현 횟수를 계산하는 함수 """
    total_count = 0
    # 폴더 내의 모든 파일을 확인
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.htm') or file.endswith('.xhtml') or file.endswith('.html'):
                file_path = os.path.join(root, file)
                word_count = count_word_in_html_file(file_path, target_word)
                total_count += word_count
    return total_count

# 특정 단어가 포함된 문장을 추출하는 함수
def find_sentences_with_word_in_html(file_path, target_word):
    # 결과를 저장할 리스트
    sentences_with_word = []
    
    # HTML 파일 열기
    with open(file_path, 'r', encoding='utf-8') as file:
        # HTML 내용 읽기
        content = file.read()
        
        # BeautifulSoup을 사용하여 HTML 태그 제거
        soup = BeautifulSoup(content, 'html')
        text = soup.get_text()  # HTML 태그를 제거하고 텍스트만 추출
        
        # 문장을 정규 표현식으로 구분 (여기서는 마침표, 물음표, 느낌표 등을 기준으로 문장을 구분)
        sentences = re.split(r'[.!?]', text)
        
        # 각 문장을 순회하면서 특정 단어가 포함되어 있는지 확인
        for sentence in sentences:
            # - 가 찾는 단어에 들어가면 -뒤에 나오는 단어는 제외
            if '-' not in target_word:
                if target_word.lower() in sentence.lower():  # 대소문자 구분 없이 검색
                    sentences_with_word.append(sentence.strip())  # 문장 앞뒤 공백 제거
            else:
                word = target_word.split('-')
                if (word[0].lower().strip() in sentence.lower()) and (word[1].lower().strip() not in sentence.lower()):  # 대소문자 구분 없이 검색
                    sentences_with_word.append(sentence.strip())  # 문장 앞뒤 공백 제거
                    
    return sentences_with_word

# 예시 사용법
# folder_path = "C:/example/folder"  # HTML 파일이 들어 있는 폴더 경로
# 현재 파일의 경로를 얻고, 디렉토리만 추출
current_file_path = os.path.abspath(__file__)
folder_path = os.path.dirname(current_file_path)
print(folder_path)
while(1):
    print('\n\n\n')
    print('='*50)
    word = input("\n찾고 싶은 단어를 입력하세요 : ")  # 찾고 싶은 단어
    print()
    total_word_count = count_word_in_folder(folder_path, word)
    print(f"\n총 단어 '{word}' 등장 횟수: {total_word_count}")
