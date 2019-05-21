from aip import AipOcr

config = {
    'appId': '16307647',
    'apiKey': 'Epf6gBaoEvCRZ9pCiqIGMqIg',
    'secretKey': '8PoHHrbPZLVHzRRgvRFbnq4l5HIOziXx'
}

client = AipOcr(**config)


def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()


def img_to_str(image_path):
    image = get_file_content(image_path)
    result = client.basicGeneral(image)
    print(result)
    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])


img_to_str("F:\\a1.png")


