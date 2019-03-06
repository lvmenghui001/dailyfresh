import hashlib

# hashobj = hashlib.sha256()
hashobj = hashlib.md5()  #创建md5的hash方法对象
str = "helloword"
hashobj.update(str.encode("utf-8"))  # 把字符串转成bytes并用update进行hash
print(hashobj.hexdigest)
