import werkzeug
from flask_restful import Resource, reqparse
from datetime import datetime
from handler.handler import processVideo
from handler.punctuator import handlePunctuation
from handler.sumy_summarizer import generate_reduction_summary, generate_lsa_summary, generate_lex_rank_summary, generate_luhn_summary
from handler.TextRank_summarizer import generate_summary


class VideoResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')
    parser.add_argument('method', type=str)

    def post(self):
        args = VideoResource.parser.parse_args()
        video = args['file']
        method = args['method']
        if video:
            now = datetime.now()
            myTimeStamp = now.strftime("%d%m%Y%H%M%S")
            fileName = './assets/' + myTimeStamp + '.wav'
            video.save(fileName)
            text = processVideo(fileName)
            text = handlePunctuation(text)
            if method == "sumy_reduction_summary":
                summary = generate_reduction_summary(text, 5)
            elif method == "sumy_lsa_summary":
                summary = generate_lsa_summary(text, 5)
            elif method == "sumy_lex_rank_summary":
                summary = generate_lex_rank_summary(text, 5)
            elif method == "sumy_luhn_summary":
                summary = generate_luhn_summary(text, 5)
            elif method == "TextRank_summarizer":
                summary = generate_summary(text, 5)
            return {'summary': summary, 'text': text, 'res': "Done"}, 201
        return {'res': 'No video'}, 501
