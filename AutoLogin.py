import curlify
import requests
url="x"#x填Request URL对应的数据
data={
"userId":"x",
"password":"x",
"service": "x",
"queryString":"x",
"passwordEncrypt":"x"
}#x填Form Data对应的数据，这里多的部分需要删除掉，少的部分需要你自己填写，格式参照上述已写的部分
header={
"Accept":"*/*",
"Accept-Encoding":"x",
"Accept-Language":"x",
"Connection":"x",
"Content-Length":"x",
"Content-Type":"x",
"Cookie":"x",
"Host":"x",
"Origin":"",
"Referer":"x",
"User-Agent":"x",
}#x填Request Headers对应的数据，这里多的部分需要删除掉，少的部分需要你自己填写，格式参照上述已写的部分
response=requests.post(url,data,headers=header).status_code
print("状态码:{}\n".format(response))#打印状态码
if(response==200):
    print("登陆成功\n")
#如果将下面代码前面的#删除，则输出一个crul(bash)脚本文件
#ret = curlify.to_curl(response.request, compressed=True)
#with open("AutoLogin.sh",'w') as f:
#    f.write(ret)
#print(ret)
#response.encoding='utf8'
#print(response.text)
