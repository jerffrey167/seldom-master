import json

import seldom
from seldom.db_operation import MySQLDB


class TestRequest(seldom.TestCase):

    def mysqldb(self,sql):
        db = MySQLDB(host="120.46.215.163",
                     port=3306,
                     user="yf_exam",
                     password="yf_exam",
                     database="yf_exam")
        ret = db.query_one(sql)
        db.close()
        return ret

    def test_001login(self):
        global  header
        header = {"Content-Type": "application/json"}
        data = {"username":"admin","password":"admin"}
        self.post("/exam/api/sys/user/login", json=data, headers=header)
        token = self.response["data"]["token"]
        header["token"] = token

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
        self.post("/exam/api/qu/qu/save",json=data,headers=header)

    # def test_003QuSerach(self):
    #     data={"current":1,"size":10,"params":{"content":"题目新增测试","quType":"","repoIds":[]},"t":1680789101846}
    #     self.post("/exam/api/qu/qu/paging",json=data,headers=header)
    #     global  quid , createtime
    #     quid = self.response["data"]["records"][0]["id"]

    def test_004qusql(self):
        global quid
        t1 = self.mysqldb("select id from el_qu where content ='题目新增测试'  LIMIT 0,1")
        t2 = json.dumps(t1)
        quid = json.loads(t2)["id"]
        print(quid)





    def test_005QuDel(self):
        data=quid
        self.post("/exam/api/qu/qu/delete",json=data,headers=header)




if __name__ == '__main__':
    seldom.main()

