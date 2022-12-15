import re
import zipfile
from tqdm import tqdm
解压路径='D:/yourfile/'
dest_path=str('D:\\Backup\\Downloads\\test.zip')
# 如果是zip文件
if dest_path.endswith('.zip'):
    压缩文件名v带路径=dest_path
    zip_member = zipfile.ZipFile(压缩文件名v带路径,'r') # 压缩文件位置
    for fileyy in tqdm(zip_member.infolist(), desc='Extracting '):
        try:
            # 解决问题
            fileyy.filename=re.sub(r'\s*/\s*', "/", fileyy.filename)
            # print(fileyy)
            zip_member.extract(fileyy, 解压路径)
        except zipfile.error as e:
            print(e)
    zip_member.close()