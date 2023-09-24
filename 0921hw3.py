import os
os.mkdir('CS')
file_path = os.path.join("CS", "homework.txt")
with open(file_path, "w") as file:
    file.write('4112029014_嚴婉榛')
with open(file_path, "r") as file:
    content = file.read()
    print("內容:")
    print(content)
import os 
import time
file_size=os.path.getsize(file_path)
print(f'\n文件大小:{file_size}字節')
modification_time=os.path.getmtime(file_path)
print(f'\n最後修改時間:{modification_time}')
formatted_time=time.ctime(modification_time)
print(f'\n最後修改時間(人類可讀模式):{formatted_time}')

os.remove(file_path)
print("\n檔案已刪除。")
os.rmdir("CS")
print("目錄已刪除。")

 


