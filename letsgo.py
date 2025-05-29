import re

def replace_image_paths_in_file(input_file, output_file):
    # 텍스트 파일을 읽어옵니다
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 정규표현식으로 경로를 수정합니다
    modified_content = re.sub(r'src="images/', 'src="/static/images/', content)

    # 수정된 내용을 새 파일로 저장합니다
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(modified_content)

# 사용 예
input_filename = 'staticfiles/output_modified.txt'
output_filename = 'staticfiles/output_mm.txt'

replace_image_paths_in_file(input_filename, output_filename)
