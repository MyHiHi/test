import requests
import json
import base64


def get_file_content(filePath):
	""" 读取图片base64 """
	with open(filePath, 'rb') as fp:
		return base64.b64encode(fp.read())



def recognise_handwriting_pic(access_token,image_path):
	image = get_file_content(image_path)
	r = requests.post(
		url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting?access_token='+access_token,
		headers={"Content-Type":"application/x-www-form-urlencoded"},
		data = {'image':image})
	#print(r.text)
	j = json.loads(r.text)
	words_result = j.get('words_result')
	for i in words_result:
		print(i.get('words'))

access_token = '24.ac66a9a7e005479093891451de551926.2592000.1562037674.282335-16410328'  # 获取一次保存下来就够了，一般1个月有效期
print(access_token)
import sys,os

recognise_handwriting_pic(access_token,image_path=os.path.join(sys.path[0],'13.jpg'))
