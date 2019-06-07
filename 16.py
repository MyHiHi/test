import base64
def base64Encode(img_path):
    import base64
    with open(img_path,'rb') as fp:
        return base64.b64encode(fp.read())

def get_file_content(filePath):
	""" 读取图片base64 """
	with open(filePath, 'rb') as fp:
		return base64.b64encode(fp.read())

def getWord(img_path,access_token):
    word_url='https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting?access_token='+access_token
    import requests
    img=base64Encode(img_path)
    p=requests.post(word_url,data={'image':img},headers={'Content-Type':'application/x-www-form-urlencoded'})
    for i in p.json()['words_result']:
        print(i['words'])


if __name__=='__main__':
    import sys,os
    access_token='24.652b75ba01374a4400aea63fc6ea381f.2592000.1562038033.282335-16410328'
    img_path=os.path.join(sys.path[0],'13.jpg')
    getWord(img_path,access_token)