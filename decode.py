from PIL import Image

def decode():
   
    img = input("Enter image name (with extension): ")
    image = Image.open(img, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while True:
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]

        binstr = ''

        for i in pixels[:8]:
            binstr += '0' if i % 2 == 0 else '1'

        data += chr(int(binstr, 2))

        if pixels[-1] % 2 != 0:
            return data

if __name__ == '__main__':
    print("Decoded text: " + decode())
