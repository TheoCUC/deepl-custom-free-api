'''
Author: isaac
Date: 2022-10-06 17:16:44
LastEditors: isaac
LastEditTime: 2022-10-06 21:55:31
Description: 
'''
# import asyncio
from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class DeepLWebAPI():
    def __init__(self):
        # service = Service(executable_path='/Users/isaac/Downloads/edgedriver_mac64_m1/msedgedriver')
        self.js = '''
            return document.getElementById('target-dummydiv').innerHTML
            '''
        # self.driver = webdriver.Edge(service=service)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Remote(
        # command_executor="http://127.0.0.1:4444/wd/hub",
        # desired_capabilities=DesiredCapabilities.CHROME)

    def translator(self,
                   text: str,
                   lang_tgt: str = 'ZH',
                   lang_src: str = 'EN',
                   detect: bool = False) -> tuple:
        self.driver.get(
            f'https://www.deepl.com/en/translator#{lang_src.upper()}/{lang_tgt.upper()}/{text}'
        )
        WebDriverWait(self.driver, 100,
                      0.5).until(lambda x: x.execute_script(self.js) != '\r\n')
        return self.driver.execute_script(self.js)

    # def __del__(self):
    # self.driver.quit()


def main():
    text = 'Example of a hierarchical structure annotation'
    try:
        print('Start running...')
        # asyncio.get_event_loop().run_until_complete(translator(text))
        DeepL = DeepLWebAPI()
        ret = DeepL.translator(text)
        print(ret)
    except KeyboardInterrupt as k:
        print('\nKey pressed to interrupt...')

    # print('Start running...')


if __name__ == "__main__":
    main()
