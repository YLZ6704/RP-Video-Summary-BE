# UTS 32933 Research Project - Autumn 2021
## Video Summary Converter - Back End

Students:
- Wencheng Xiong - 13680436
- Xiaorong Pan - 12765982
- Yali Zhu - 13336704

### Major Tech Stack

- Python Flask 1.1.2
- Flask-RESTful 0.3.8
- Punctuator 
- NLTK
- Numpy
- Sumy

### Run in local dev environment
At root directory
Mac
```sh
    source venv/Script/activate
    pip install -r requirements.txt
    mkdir -p ~/.punctuator
    cd ~/.punctuator
    gdown https://drive.google.com/uc?id=0B7BsN5f2F1fZd1Q0aXlrUDhDbnM
    python app.py
```
Windows
```sh
    cd venv/Script/
    activate.bat
    pip install -r requirements.txt
    mkdir -p ~/.punctuator
    cd ~/.punctuator
    gdown https://drive.google.com/uc?id=0B7BsN5f2F1fZd1Q0aXlrUDhDbnM
    python app.py
```
## Run in production
Link repo to Heroku
Enable storage service

Remove .bk extension from Procfile.bk and wsgi.py.bk

Remove following codes from app.py
```py
    if __name__ == '__main__':
    app.run(port=5000, debug=True)
```
