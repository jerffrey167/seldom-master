import seldom
from seldom import depend

class TestDepend(seldom.TestCase):

    def test_001login(self):
        self.open("http://120.46.215.163:8102/#/login")
        self.type(xpath="//input[@type='text']", text="s2")
        self.type(xpath='//input[@type="password"]', text="123456")
        self.click(xpath='//button[@type="button"]')

    def test_002openpage(self):
        self.click(xpath="//*[starts-with(@style,'padding-left: 20px')]/span[text()='在线考试']")
        self.click(xpath='//*[@id="screenfull"]/*[@class="svg-icon"]')
        self.click(xpath="//*[starts-with(@style,'padding-left: 40px')]/span[text()='在线考试']")

    def test_003redayexam1(self):
        self.assertNotElement(xpath="//*[text()='您有正在进行的考试，离线太久考试将被作废哦，点击此处可继续考试！']")

    def test_003redayexam2(self):
        self.assertElement(xpath="//*[text()='您有正在进行的考试，离线太久考试将被作废哦，点击此处可继续考试！']")

    @depend("test_003redayexam1")
    def test_004examing(self):
        self.type(xpath='//input[@placeholder="搜索考试名称"]', text="演示考试")
        self.click(xpath="//span[text()='去考试']")

    @depend("test_003redayexam2")
    def test_005examing(self):
        self.click(xpath="//*[text()='您有正在进行的考试，离线太久考试将被作废哦，点击此处可继续考试！']")
        self.click(xpath="//span[text()=' 交卷 ']//..")
        self.click(xpath="//*[@aria-label='提示']//button[2]")

    # @depend("test_003examing")
    # def test_005texaming2(self):
    #     self.click(xpath="//span[text()='去考试']")
    #     self.click(xpath="//*[text()=' 开始考试 ']")
    #     self.sleep(3)
    #     self.click(xpath="//*[contains(text(),'A.')]//..")
    #     self.click(xpath="//span[text()=' 下一题 ']//..")
    #     #1
    #     self.sleep(3)
    #     self.click(xpath="//*[contains(text(),'A.')]//..")
    #     self.click(xpath="//span[text()=' 下一题 ']//..")
    #     #2
    #     self.sleep(3)
    #     self.click(xpath="//*[contains(text(),'A.')]//..")
    #     self.click(xpath="//span[text()=' 下一题 ']//..")
    #     #3
    #     self.sleep(3)
    #     self.click(xpath="//*[contains(text(),'A.')]//..")
    #     self.click(xpath="//span[text()=' 下一题 ']//..")
    #     #4
    #     self.sleep(3)
    #     self.click(xpath="//*[contains(text(),'A.')]//..")
    #     self.click(xpath="//span[text()=' 下一题 ']//..")
    #     #5
    #     self.sleep(3)
    #     self.click(xpath="//*[contains(text(),'A.')]//..")
    #     self.click(xpath="//span[text()=' 下一题 ']//..")
    #     #6
    #     self.sleep(3)
    #     self.click(xpath="//*[contains(text(),'A.')]//..")
    #     self.click(xpath="//*[contains(text(),'B.')]//..")
    #     self.click(xpath="//*[contains(text(),'C.')]//..")
    #     self.click(xpath="//span[text()=' 下一题 ']//..")
    #     #7
    #     self.sleep(3)
    #     self.click(xpath="//*[contains(text(),'A.')]//..")
    #     self.click(xpath="//*[contains(text(),'B.')]//..")
    #     self.click(xpath="//*[contains(text(),'C.')]//..")
    #     self.click(xpath="//span[text()=' 下一题 ']//..")
    #     #8
    #     self.sleep(3)
    #     self.click(xpath="//*[contains(text(),'A.')]//..")
    #     self.click(xpath="//span[text()=' 下一题 ']//..")
    #     #9
    #     self.sleep(3)
    #     self.click(xpath="//*[contains(text(),'A.')]//..")
    #     self.sleep(3)
    #     self.click(xpath="//span[text()=' 交卷 ']//..")
    #     self.click(xpath="//*[@aria-label='提示']//button[2]")

    def test_099logout(self):
        self.sleep(5)
        self.click(xpath="//div[text()=' 学员2 ']")
        self.click(xpath="//span[text()='退出登录']//..")

if __name__ == '__main__':
    seldom.main(browser="gc", debug=False)