import seldom

"""
说明：
path： 指定测试目录。
browser： Web测试，指定浏览器，默认chrome。
base_url： Http测试，指定接口地址。
app_info： 启动app配置,
app_server： appium server 地址。
title： 指定测试项目标题。
tester： 指定测试人员。
description： 指定测试环境描述。
debug： debug模式，设置为True不生成测试用例。
rerun： 测试失败重跑
"""


if __name__ == '__main__':
    # web case 配置
    seldom.main(path="./test_dir/api_case/test_ExamAddDel.py",
                title="seldom自带 Web demo",
                tester="虫师",
                base_url="http://120.46.215.163:8102/",
                timeout = 3,
                debug=True
                )

