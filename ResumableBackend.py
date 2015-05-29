__author__ = 'wilman'
from utils.webtools import md5hex

from os.path import isfile,getsize,join, isdir
from os import remove as remove_file, mkdir
from io import BytesIO as IOBuffer
class Resumable(object):
    upload_tmp_folder = None
    upload_folder = None

    def __init__(self, upload_tmp_folder="uploads_tmp", upload_folder="uploads"):
        self.upload_tmp_folder = upload_tmp_folder
        self.upload_folder = upload_folder
        if not isdir(upload_folder):
            mkdir(upload_folder)
        if not isdir(upload_tmp_folder):
            mkdir(upload_tmp_folder)



    def handle_chunk(self,token, file_blob, file_id,filename, file_blob_size, chunk_inx, chunk_num):
        # print file_blob,len(file_blob),chunk_inx,chunk_num,file_id,filename
        if len(file_blob) != file_blob_size:
            print "error!!"
            return False

        fln = md5hex(token+file_id) + "-" + chunk_num + "-" + chunk_inx+ ".tmp"
        try:
            fs = open(join(self.upload_tmp_folder,fln),"wb")
            for c in file_blob.chunks():
                fs.write(c)
            fs.close()

            if self.check_all_chunks_ready(token,file_id,chunk_num):
                data = self.merge_chunk_files(token,file_id,chunk_num)
                if data:
                    f = open(join(self.upload_folder,md5hex(token+file_id)+"-"+filename),"wb")
                    f.write(data.read())
                    f.close()
                    self.del_chunk_tmp_files(token,file_id,chunk_num)
                    return True
                else:
                    return False

        except Exception as e:
            print e
            return False

    # check the status of the chunk in the server
    # return False, the chunk is not on the server, please reupload
    #        True, the chunk is ready on the server, no need to reupload
    def check_chunk_status(self,token,file_id,chunk_inx,chunk_num,chunk_size):
        flhash = md5hex(token+file_id)
        fln = "%s-%s-%s.tmp" %(flhash,str(chunk_num),str(chunk_inx))
        full_fln = join(self.upload_tmp_folder,fln)
        if isfile(full_fln):
            # check the size of the file
            if int(chunk_size) == getsize(full_fln):
                return True
            else:
                return False
        else:
            return False


    def check_all_chunks_ready(self,token,file_id, chunk_num):
        flhash = md5hex(token+file_id)
        chunk_num = int(chunk_num)
        file_cnt = 0
        for chunk_inx in range(1,chunk_num+1):
            fln = "%s-%s-%s.tmp" %(flhash,str(chunk_num),str(chunk_inx))
            if isfile(join(self.upload_tmp_folder,fln)):
                file_cnt = file_cnt +1
            else:
                pass

        if file_cnt == chunk_num:
            print "file is ready!!"
            return True
        else:
            return False

    def merge_chunk_files(self,token,file_id,chunk_num):
        flhash = md5hex(token+file_id)
        chunk_num = int(chunk_num)
        ofs = IOBuffer()
        try:
            for chunk_inx in range(1,chunk_num+1):
                fln = "%s-%s-%s.tmp" %(flhash,str(chunk_num),str(chunk_inx))
                ful_fln = join(self.upload_tmp_folder,fln)
                f = open(ful_fln,"rb")
                d = f.read()
                ofs.write(d)
            ofs.seek(0)
            return ofs
        except Exception as e:
            print "error: ",e
            return None

    def del_chunk_tmp_files(self,token,file_id,chunk_num):
        flhash = md5hex(token+file_id)
        chunk_num = int(chunk_num)
        for chunk_inx in range(1,chunk_num+1):
            fln = "%s-%s-%s.tmp" %(flhash,str(chunk_num),str(chunk_inx))
            ful_fln = join(self.upload_tmp_folder,fln)
            remove_file(ful_fln)




