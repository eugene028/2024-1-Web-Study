import pandas as pd

# Excel 파일의 경로
excel_file_path = '3_BFPER.xlsx'

# 시트 지정
sheet_name = '1'

# 열 이름 지정
brand = '브랜드'
product = '상품명'

# Excel 파일 읽기
df = pd.read_excel(excel_file_path)

# 특정 열 데이터를 문자열 리스트로 추출
data_list = df[brand].astype(str).tolist()
data_list2 = df[product].astype(str).tolist()
for i in range(0,104):
    print("'" + data_list2[i][:-5]+ '-' + data_list[i] + "',")
# 결과 출력
