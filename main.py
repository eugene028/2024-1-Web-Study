import pandas as pd

# Excel 파일의 경로
excel_file_path = 'user.xlsx'

# 시트 지정
sheet_name = '기초 인공지능 스터디'

# 열 이름 지정
target_column_name = '깃허브핸들명'

# Excel 파일 읽기
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

# 특정 열 데이터를 문자열 리스트로 추출
data_list = df[target_column_name].astype(str).tolist()
for i in data_list:
    print('https://github.com/' + i + '/2023-2-AI-Study')
# 결과 출력
