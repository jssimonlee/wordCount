import os

# 확장자를 변경할 폴더 경로
folder_path = r"C:\python\MTH"

# 변경하고 싶은 확장자 (현재 확장자 -> 새로운 확장자)
old_extension = ".epub"
new_extension = ".zip"

# 폴더 안의 모든 파일을 순회하며 확장자 변경
for filename in os.listdir(folder_path):
    # 파일 경로
    file_path = os.path.join(folder_path, filename)
    
    # 파일이 실제 파일일 경우만 처리
    if os.path.isfile(file_path):
        # 파일이 현재 확장자와 일치하면
        if filename.endswith(old_extension):
            # 새로운 파일명 생성
            new_filename = filename.replace(old_extension, new_extension)
            new_file_path = os.path.join(folder_path, new_filename)
            
            # 파일명 변경
            os.rename(file_path, new_file_path)
            print(f"파일명 변경: {file_path} -> {new_file_path}")

print("모든 파일 확장자가 변경되었습니다.")
