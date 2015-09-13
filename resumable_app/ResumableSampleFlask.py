__author__ = 'wilman'
from flask import Flask,request,send_file
from ResumableBackend import Resumable
import simplejson as json
# some settings
UPLOAD_DIR = ''
UPLOAD_TMP_DIR = ''


app = Flask(__name__)
R = Resumable(upload_folder="/data/upload/",upload_tmp_folder="/data/upload/tmp/")
def get_param(req,k):
    v = req.args.get(k,'')
    if not v:
        v = req.form.get(k,'')
    return v

@app.route('/upload/', methods=['GET','POST'])
def upload():
    if request.method == "POST":
        file_id = get_param(request,"resumableIdentifier")
        chunk_id = get_param(request,"resumableChunkNumber")
        file_blob_size = get_param(request,"resumableCurrentChunkSize")
        file_name =  get_param(request,"resumableFilename")
        chunk_num = get_param(request,"resumableTotalChunks")
        token = get_param(request,"upload_token")
        f = request.files.get('file')
        if f :
            file_blob = f.read()
        else:
            file_blob = None
        done = R.handle_chunk(token, file_blob,file_id,file_name, int(file_blob_size), chunk_id,chunk_num)
        if done:
            data ={'file_name':file_name, 'local_path': R.get_full_file_name(token,file_id,file_name)}
            data = json.dumps(data)
            return data,200
        else:
            return "",200

    else:

        file_id = get_param(request,"resumableIdentifier")
        chunk_id = get_param(request,"resumableChunkNumber")
        file_blob_size = get_param(request,"resumableCurrentChunkSize")
        chunk_num = get_param(request,"resumableTotalChunks")
        token = get_param(request,"upload_token")
        status = False
        if token and file_id and chunk_id and chunk_num and file_blob_size:
            status = R.check_chunk_status(token,file_id,chunk_id,chunk_num,file_blob_size)
            if not status:
                return "",201
            else:
                return "",200
        else:
            return send_file("static/myupload.html")



if __name__ == '__main__':
    app.run(debug=True)