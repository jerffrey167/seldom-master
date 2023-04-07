import seldom
from seldom import SMTP


if __name__ == '__main__':
    # web case 配置
    seldom.main(path="./test_dir/api_case/test_ExamAddDel.py",
                title="seldom自带 API demo",
                tester="虫师",
                base_url="http://120.46.215.163:8102",
                debug=True,
                )
