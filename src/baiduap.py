from aip import AipOcr
import configparser


class BaiDuAPI:
    """图片文字识别"""

    # 初识化方法
    def __init__(self, filePath):  # self 就是BaiDuAPI()
        # 读取工单信息
        target = configparser.ConfigParser()
        target.read(filePath)
        app_id = target.get('我的工单', 'App_ID')
        app_key = target.get('我的工单', 'App_KEY')
        secret_key = target.get('我的工单', 'SECRET_KEY')
        self.client = AipOcr(app_id, app_key, secret_key)

    def picture2Text(self, filePath):
        # 读取图片
        image = self.getPicture(filePath)
        texts = self.client.basicGeneral(image)
        # print(texts['words_result'])
        allTexts = ''
        for word in texts['words_result']:
            allTexts = allTexts + word.get('words', '')
        return allTexts

    @staticmethod
    def getPicture(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()


if __name__ == '__main__':
    baiduapi = BaiDuAPI('password.ini')
    print(baiduapi.picture2Text('Picture.png'))