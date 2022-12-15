# Python-zipfile
解决部分zip文件无法解压的问题。

## 解决报错内容
  File "C:\Users\Administrator\anaconda3\lib\zipfile.py", line 1625, in extract
    return self._extract_member(member, path, pwd)
  File "C:\Users\Administrator\anaconda3\lib\zipfile.py", line 1692, in _extract_member
    os.mkdir(targetpath)
FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'D:\\yourfile\\test \\ W'