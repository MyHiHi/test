# def getK(t):
#     res=[]
#     res.append([1])
#     r1=[1,1]
#     res.append(r1)
#     for i in range(2,t):
#         r=[]
#         for j in range(0,len(r1)-1):
#             r.append(r1[j]+r1[j+1])
#         r1=[1]+r+[1]
#         res.append(r1)
#     return res
# for k in getK(6):
#     print(k)


import requests
# p=requests.get(url='http://localhost:8080/#/app/home/index').content
# print(p)
from wxpy import Bot
from threading import Timer
import time
from wxpy import *
url='http://open.iciba.com/dsapi/'
def getInfo(url):
    info=requests.get(url).json()
    return info['content'],info['note']
bot=Bot(cache_path=True)
bot.enable_puid();
def sendMsg(name):  
    duration=60000
    try:
        bot.file_helper.send('我是助手')
        # print(bot.groups())
        
        # for i in bot.friends():
        #     print(i.puid)
        friends=bot.friends();
        chats=bot.chats();
        groups=bot.groups();
        # for i in groups:
        #     i.update_group(True);
        #     print(i.members.stats_text())
        # print(friends.stats_text())
        friend=friends.search(name)[0];
        self_messages=bot.messages.search(sender=friend);
        print('自己发送的消息: ',self_messages);
        p=getInfo(url);
        content,note=p
        i='''
        来自 男朋友的 问候：\n
        '''+content+'\n'+note;
        i=' 昭昭 ';
        # friend.send(i);
        
        Timer(duration,sendMsg(name)).start();

    except Exception as e:
        
        bot=Bot(cache_path=True).friends().search(u'撒丫子就跑')[0];
        
        bot.send('消息发送失败('+str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+')');
        print('>>>: ',e)
    finally:
        print('发送完毕');






def getAutoReceive(msg):
    import requests
    apiUrl = 'http://www.tuling123.com/openapi/api';
    data={
        "key":'d382e1d7de994876a11500ac8c872761',
        'info':msg,
    }
    try:
        return requests.post(apiUrl,data=data).json().get('text')
    except Exception as e:
        return None

@bot.register()
def messager(msg):
    print(msg.sender.name,msg.text)
    msg.sender.mark_as_read();
    if msg.type==TEXT:
        return getAutoReceive(msg.text)
    elif msg.type==PICTURE:
        source_path='./images'
        import os
        save_path=os.path.join(source_path,msg.file_name);
        msg.get_file(save_path);
        print(save_path);
        save_path=os.path.join(source_path,'1.jpg');
        msg.reply_image(save_path);
    else:
        msg.forward(msg.sender)

embed();
# bot.file_helper.send('test .....')





# if __name__=='__main__':
    # name='Mr.枫尉大人'
    # name='奋斗男人'
    # sendMsg(name)
   
                    
