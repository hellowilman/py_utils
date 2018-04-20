from pyPdf import PdfFileWriter, PdfFileReader
def merge_scan1(fln_odd,fln_even, fln_out):
    # fln_odd is 1,3,4,7,...,2k-1
    # fln_oven is 2k,2k-2,2k-4,...,2
    input1 = PdfFileReader(file(fln_odd, "rb"))
    input1 = PdfFileReader(file(fln_odd, "rb"))
    # check input 
    N = input1.getNumPages()
    if input2.getNumPages() != N:
        print "error!"
        return 
    # do processing 
    output = PdfFileWriter()
    
    for pid in range(0,N):
        output.addPage(input1.getPage(pid))
        output.addPage(input2.getPage(N-1-pid))
    output.write(file(fln_out,"wb"))
def merge_scan2(fln_odd,fln_even, fln_out):
    # fln_odd is 1,3,4,7, ..., 2k-1
    # fln_oven is 2,4,6,8, ..., 2k
    input1 = PdfFileReader(file(fln_odd, "rb"))
    input1 = PdfFileReader(file(fln_odd, "rb"))
    # check input 
    N = input1.getNumPages()
    if input2.getNumPages() != N:
        print "error!"
        return 
    # do processing 
    output = PdfFileWriter()
    
    for pid in range(0,N):
        output.addPage(input1.getPage(pid))
        output.addPage(input2.getPage(pid))
    output.write(file(fln_out,"wb"))
