import hashlib, os

if __name__ == '__main__':
    dirs = os.listdir('./captcha-example5')
    for item in dirs:
        dot = item.find('.png')
        if dot != -1:
            captcha = item[0:dot]
            image = open('./captcha-example5/' + item)
            print 'md5[\'%s\'] = \'%s\'' % (hashlib.md5(image.read()).hexdigest(), captcha)
            image.close()
