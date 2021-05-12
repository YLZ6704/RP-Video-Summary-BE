import moviepy.editor as mp
from datetime import datetime

def videoToAudio(file):
    #使用moviepy库
    #视频转音频
    clip = mp.VideoFileClip(file)
    #时间戳
    now = datetime.now()
    myTimeStamp = now.strftime("%d%m%Y%H%M%S")
    audioName = './assets/' + myTimeStamp + '.wav'
    #保存音频
    clip.audio.write_audiofile(audioName)
    #返回音频的路径
    return audioName