import urllib

def test_url(url):
    
    '''get_url accepts a URL string and return the server response code, response headers, and contents of the file'''
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.A.B.C Safari/525.13',
        'Referer': 'http://stoptazmo.com'}
    
    request = urllib.request.Request(url, headers=req_headers) # create a request object for the URL
    opener = urllib.request.build_opener() # create an opener object
    response = opener.open(request) # open a connection and receive the http response headers + contents
    
    code = response.code
    headers = response.headers # headers object
    
    print("Code: %s" % code)
    #print("Headers: %s" % headers)
    
    if code == 200:
        print("looks good to me")

        contents = response.read() # contents of the URL (HTML, javascript, css, img, etc.)
    
        try:
            teststring = str(contents[1:40],encoding='utf8')
            if (teststring.find("This file does not")) > 0:
                print("danger   ")
                RunTimeerror('file wasnt found')
                
            print("we made it")
        except:
            print ('testing')
            
    
    
    return code , headers  , contents

def test_url_download(url,strSavepath):
    '''get_url accepts a URL string and return the server response code, response headers, and contents of the file'''
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.A.B.C Safari/525.13',
        'Referer': 'http://stoptazmo.com'}
    
    request = urllib.request.Request(url , headers=req_headers) # create a request object for the URL
    opener = urllib.request.build_opener() # create an opener object
    response = opener.open(request) # open a connection and receive the http response headers + contents
    
    code = response.code
    headers = response.headers # headers object
    
    #print("Code: %s" % code)
    #print("Headers: %s" % headers)

    #if a file, not redirect
    if code == 200:
        #print("looks good to read")
        contents = response.read() # contents of the URL (HTML, javascript, css, img, etc.)
    
        try:
            teststring = str(contents[1:40],encoding='utf8') #redirect = file unavailable
            if (teststring.find("This file does not")) > 0: #this file doesnt exist
                print('Error:file wasnt found')
                return 0
                
            #not a file, but not our error
            print('Error:unknown error')
            return 0
            
        except:
            #unable to convert utf8 because we have a file
            strFileName = (url[-(len(url) - (url.find('file_name=')+10)):])
            print('begin output file: %s' % strFileName)
            
            oSaveFile = open(strSavepath + '\\' + strFileName, "wb")
            oSaveFile.write(contents)
            oSaveFile.close()
            return 1
            
        

    #contents = response.read() # contents of the URL (HTML, javascript, css, img, etc.)
    #strFileName = (url[-(len(url) - (url.find('file_name=')+10)):])
    #
    #oSaveFile = open(strSavepath + '\\' + strFileName, "wb")
    #oSaveFile.write(contents)
    #oSaveFile.close()
    

#testURL = test_url('http://stoptazmo.com/downloads/get_file.php?file_category=shamo&mirror=1&file_name=shamo_001.zip')
#print ("outputs: %s" % (testURL,))


for iIssue in range(1 , 101):
    # add time checker
    # add dynamic foldering
    #handle loops errors
    
    #Store loop number as string with 3 digits.
    str_iIssue = str(iIssue).rjust(3,'0') 
    
    test_url_download('http://stoptazmo.com/downloads/get_file.php?file_category=beck&mirror=1&file_name=beck_%s.zip' % str_iIssue,'F:\\Comics\\Manga\\Beck')

    #'http://stoptazmo.com/downloads/get_file.php?file_category=beck&mirror=1&file_name=beck_001.zip'
    #'http://stoptazmo.com/downloads/get_file.php?file_category=hunter_x_hunter&mirror=1&file_name=Hunter_X_Hunter_001.zip'
    #'http://stoptazmo.com/downloads/get_file.php?file_category=gantz&mirror=1&file_name=gantz_001.zip'
    #'http://stoptazmo.com/downloads/get_file.php?file_category=zetman&mirror=1&file_name=zetman_%s.zip'
    #'http://stoptazmo.com/downloads/get_file.php?file_category=shamo&mirror=1&file_name=shamo_001.zip'