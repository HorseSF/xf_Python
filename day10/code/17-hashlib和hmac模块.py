import hashlib
import hmac

# 用来进行数据加密
# hashlib模块主要支持md5和sha加密方式
# 加密方式：单向加密 md5/sha，对称加密，非对称加密 rsa
# 单向加密：只有加密过程，不能解密

# 需要将加密的内容转换成二进制
x = hashlib.md5()
x.update("abc".encode("utf-8"))
print(x.hexdigest())

h1 = hashlib.sha1('123456'.encode())
print(h1.hexdigest())
h2 = hashlib.sha224('123456'.encode())
print(h2.hexdigest())
h3 = hashlib.sha256('123456'.encode())
print(h3.hexdigest())
h4 = hashlib.sha384('123456'.encode())
print(h4.hexdigest())

h = hmac.new("h".encode(), "你好".encode())
result = h.hexdigest()
print(result)  # 获取加密后的结果
