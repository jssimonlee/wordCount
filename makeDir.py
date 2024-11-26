import os

def create_numbered_folders(base_path, num_folders):
    # base_path: 폴더가 생성될 경로
    # num_folders: 생성할 폴더의 개수
    
    # base_path가 존재하지 않으면 생성
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    for i in range(1, num_folders + 1):
        folder_name = f"{i:02d}권"  # 순번을 3자리로 생성 (예: 001, 002, ...)
        folder_path = os.path.join(base_path, folder_name)
        
        # 폴더가 이미 존재하지 않으면 생성
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"폴더 '{folder_name}' 생성됨.")
        else:
            print(f"폴더 '{folder_name}' 이미 존재.")

# 사용 예시
base_path = "test_folders"  # 폴더를 만들 경로
num_folders = 56           # 생성할 폴더 수

create_numbered_folders(base_path, num_folders)
