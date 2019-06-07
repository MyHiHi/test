import os,sys
from aip import AipImageSearch
APP_ID = '16415257'
API_KEY = 'd8McO2IaD1NZ9d3gVK9uoqFr'
SECRET_KEY = 'Ta6gBIPzr98z5ofe5VsSyqeQemdzO8Pm'
client=AipImageSearch(APP_ID,API_KEY,SECRET_KEY)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

filePath=os.path.join(sys.path[0],'images/man.jpg')
image = get_file_content(filePath)
client.similarSearch(image)