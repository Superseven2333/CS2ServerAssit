from flask import Flask, send_file
import pymongo

app = Flask(__name__)


@app.route('/V1.16')
def download_file():
    # 你想要提供下载的文件路径
    file_path = './V1.16.zip'

    return send_file(file_path, as_attachment=True)

@app.route('/version')
def version():
    return 'V1.16'


if __name__ == '__main__':
    app.run(port=8000)
