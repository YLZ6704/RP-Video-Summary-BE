import werkzeug
from flask_restful import Resource, reqparse
from datetime import datetime
from handler.handler import processAudio
from handler.punctuator import handlePunctuation
from handler.sumy_summarizer import generate_reduction_summary, generate_lsa_summary, generate_lex_rank_summary, generate_luhn_summary
from handler.TextRank_summarizer import generate_summary
from handler.videoToAudio import videoToAudio
import sys


class VideoResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
    parser.add_argument('methods')

    #POST请求
    def post(self):
        args = VideoResource.parser.parse_args()
        video = args['file']
        methods = args['methods']
        if video:
            #生成时间戳
            now = datetime.now()
            myTimeStamp = now.strftime("%d%m%Y%H%M%S")
            fileName = './assets/' + myTimeStamp + '.mp4'
            #Video重命名 + 保存
            video.save(fileName)
            #Video转音频wav
            audioName = videoToAudio(fileName)
            #音频转文字（无标点，默认成一句话）
            text = processAudio(audioName)
            #文字加标点（有待加强）
            text = handlePunctuation(text)
            #五种方法
            result = []
            if "sumy_reduction_summary" in methods:
                summary = generate_reduction_summary(text, 3)
                result.append({
                    "method": "sumy_reduction_summary",
                    "summary": summary
                })
            if "sumy_lsa_summary" in methods:
                summary = generate_lsa_summary(text, 3)
                result.append({
                    "method": "sumy_lsa_summary",
                    "summary": summary
                })
            if "sumy_lex_rank_summary" in methods:
                summary = generate_lex_rank_summary(text, 3)
                result.append({
                    "method": "sumy_lex_rank_summary",
                    "summary": summary
                })
            if "sumy_luhn_summary" in methods:
                summary = generate_luhn_summary(text, 3)
                result.append({
                    "method": "sumy_luhn_summary",
                    "summary": summary
                })
            if "TextRank_summarizer" in methods:
                summary = generate_summary(text, 3)
                result.append({
                    "method": "sumy_luhn_summary",
                    "summary": summary
                })
            #返回结果
            return {'summary': result, 'text': text, 'res': "Done"}, 201
        return {'res': 'No video'}, 501
