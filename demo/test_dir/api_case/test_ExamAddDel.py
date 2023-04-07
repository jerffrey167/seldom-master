import seldom


class TestRequest(seldom.TestCase):

    header = {"Content-Type": "application/json"}
    def test_001login(self):
        data = {"username":"admin","password":"admin"}
        r = self.post("/exam/api/sys/user/login", json=data, headers=self.header)
        token = r.json()["data"]["token"]
        self.header["token"] = token

    def test_002QuAdd(self):
        data={
                "repoIds":[
                    "1265561101609795585"
                        ],
                "tagList":[],
                "answerList":[
                    {
                        "isRight":"true",
                        "content":"答案A",
                        "analysis":"答案A 答案解析"
                    },
                    {
                        "isRight":"false",
                        "content":"答案B",
                        "analysis":"答案B答案解析"
                    },
                    {
                        "isRight":"false",
                        "content":"答案C",
                        "analysis":"答案C答案解析"
                    },
                    {
                        "isRight":"false",
                        "content":"答案D",
                        "analysis":"答案D答案解析"
                    }
                            ],
                "quType":1,
                "level":1,
                "content":"题目新增测试",
                "analysis":"整题解析"
                }
        self.post("/exam/api/qu/qu/save",json=data,headers=self.header)

    def test_003QuSerach(self):
        data={"current":1,"size":10,"params":{"content":"题目新增测试","quType":"","repoIds":[]},"t":1680789101846}
        self.post("/exam/api/qu/qu/paging",json=data,headers=self.header)
        global  quid , createtime
        quid = self.response["data"]["records"][0]["id"]

    def test_004QuDel(self):
        data={"ids":[quid]}
        self.post("/exam/api/qu/qu/delete",json=data,headers=self.header)




if __name__ == '__main__':
    seldom.main()
