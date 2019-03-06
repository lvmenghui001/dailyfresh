import hashlib

def hashStr(strInfo):
    '''对字符串进行hash'''
    hashObj = hashlib.sha256()
    hashObj.update(strInfo.encode("utf-8"))
    return hashObj.hexdigest()

CHUNKSIZE = 2048
def hashFile(filename):
    '''对文件进行hash'''
    h = hashlib.sha256()
    with open(filename,"rb") as f:
        while True:
            chunk = f.read(CHUNKSIZE)
            if not chunk:
                break
        h.update(chunk)
    return  h.hexdigest()

print(hashStr("hello word"))