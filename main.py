import qrcode
import argparse
import pathlib
from PIL import Image
from pyzbar.pyzbar import decode

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='create and read qrcode')
    parser.add_argument('--encode', type=ascii, help='input your text')
    parser.add_argument('--decode', type=pathlib.Path, help='qrcode image location')
    args = parser.parse_args()

    if args.encode:
        create_qrcode = qrcode.make(str(args.encode))
        create_qrcode.save("qrcode.png")

    if args.decode:
        read_qrcode = decode(Image.open(str(args.decode)))
        print(read_qrcode[0].data.decode())