from db import *
import datetime
from Email import *
class chandao(object):
    sub = "【禅道数据规范】"
    def test_time(self,num):
        start_time = datetime.datetime.now()
        s = datetime.timedelta(days=num)
        start_times = (start_time - s).strftime('%Y-%m-%d %H:%M:%S')
        return str(start_times)
    def openedby(self,sql):
        openedbys = opendb(sql)
        openedbys = str(openedbys).replace('(', '').replace(",),", ',').replace(')', '').replace("'", "").replace(", ",',')
        openedbys = openedbys[:-1]
        openedbys = openedbys.split(',')
        return openedbys
    def openedbys(self,sql):
        openedby = opendbs(sql)
        openedby = str(openedby).replace('(', '').replace(",),", ',').replace(')', '').replace("'", "").replace(", ",
                                                                                                                ',')
        openedby = openedby[:-1]
        openedby = openedby.split(',')
        return openedby

    def test_all(self):
        openedby = ["dekai.dang@vhall.com", "jinhuan.ren@vhall.com", "juan.zou@vhall.com", "mei.fu@vhall.com",
                     "meiqi.lian@vhall.com", "mingchao.yang@vhall.com", "qi.tian@vhall.com",
                     "ronghuan.wang@vhall.com", "wanqian.li@vhall.com", "wenlong.liu@vhall.com", "xin.hou@vhall.com",
                     "ya.zhou@vhall.com", "yanan.cheng@vhall.com", "yangdong.chen@vhall.com", "yanmin.qin@vhall.com",
                     "yingjie.kang@vhall.com", "yuxin.shao@vhall.com", "zhanyuan.song@vhall.com", "zhebo.lin@vhall.com",
                     "zhishuai.si@vhall.com","bp.wangyan@vhallops.com","bp.zhangkun@vhallops.com","yangdong.chen@vhall.com "]
        #openedby = ["bp.wangyan@vhallops.com","bp.zhangkun@vhallops.com"]

        sqllists = []
        for i in range(len(openedby)):
            if openedby[i] != 'bp.wangyan@vhallops.com' and openedby[i] != 'bp.zhangkun@vhallops.com':
                openedby[i] = str(openedby[i]).replace("@vhall.com","")
            else:
                openedby[i] = str(openedby[i]).replace("@vhallops.com", "")
            sqlbug1 = "SELECT id from zt_bug where resolution = 'fixed' and resolvedDate <= '"+str(self.test_time(2))+"' and status = 'resolved' and openedBy ='"+openedby[i]+"'  and deleted = '0'   order by resolvedDate desc"
            sqlbug2 = "select id from zt_bug where assignedTo = '' and  status != 'closed' and deleted = '0' and openedBy='"+openedby[i]+"' and deleted = '0'  order by id desc"
            sqlbug3 = "select id from zt_bug where openedBy ='" + openedby[i] + "' and length(steps)<= 65 and type != 'proposal' and  `status` != 'closed' and deleted = '0'   order by id desc"
            sqlbug4 = "select id from zt_bug where pri=1 and status = 'active' and openedBy='"+openedby[i]+"' and openedDate < '"+str(self.test_time(7))+"' and deleted = '0'  "
            sqlbug5 = "select id from zt_bug where pri=2 and status = 'active' and openedBy='"+openedby[i]+"' and openedDate < '" + str(self.test_time(10)) + "' and deleted = '0' "
            sqlcsd1 = "select id from zt_testtask  where end < '"+str(self.test_time(1))+"' and (status = 'wait' or status = 'doing') and owner = '"+openedby[i]+"' and deleted = '0'"
            sqlcsd2 = "select id from zt_testtask where id not in (select DISTINCT(task) from zt_testrun " \
                           "where task>880) and id > 880 and begin < '" + str(self.test_time(2)) + "' and owner = '" + openedby[i] + "'  and deleted = '0'"
            #print(sqlcsd2)
            sqlcsd3 = "select distinct(k.id) from zt_testtask k LEFT JOIN zt_testrun r on k.id = r.task left join zt_case c on r.`case` = c.id  where k.`begin` <  '"+str(self.test_time(2))+"' and r.`status` = 'wait' and `owner` = '"+openedby[i]+"' and k.id > 850 and k.deleted = '0' and k.`status` = 'done'  and  c.`status` != 'normal'"

            sqlcase = "select id from zt_case where reviewedBy = '' and `status` != 'normal'  and openedDate < '"+str(self.test_time(5))+"' and openedBy ='"+openedby[i]+"' and openedDate>'2020-04-01'  and deleted = '0' "
            sqllist = [sqlbug1,sqlbug2,sqlbug3,sqlbug4,sqlbug5,sqlcsd1,sqlcsd2,sqlcsd3,sqlcase]
            sqllists.append(sqllist)
        mesglist = ["、你有未验证的bug滞留时间超过2天，编号：", "、你有未指派的bug，编号：",
                    "、bug重现步骤描述过于简单，编号：，", "、P1级bug超过7天未修复，请及时推进，编号：",
                    "、P2级bug超过10天未修复，请及时推进，编号：", "、你有提测单延期，请及时处理,编号：",
                    "、以下测试单没有关联用例，编号：", "、测试单用例未执行完毕，编号：", "、你有未评审的用例，编号："]

        ssqllists = []
        for i in range(len(openedby)):
            if openedby[i] != 'bp.wangyan@vhallops.com' and openedby[i] != 'bp.zhangkun@vhallops.com':
                openedby[i] = str(openedby[i]).replace("@vhall.com", "")
            else:
                openedby[i] = str(openedby[i]).replace("@vhallops.com", "")
            ssqlbug1 = "SELECT id from zt_bug where resolution = 'fixed' and resolvedDate <= '"+str(self.test_time(2))+"' and status = 'resolved' and openedBy ='"+openedby[i]+"' and deleted = '0'   order by resolvedDate desc"
            ssqlbug2 = "select id from zt_bug where assignedTo = '' and  status != 'closed' and deleted = '0' and openedBy='"+openedby[i]+"'  and deleted = '0'   order by id desc"
            ssqlbug3 = "select id from zt_bug where openedBy ='" + openedby[i] + "' and length(steps)<= 65 and type != 'proposal' and  `status` != 'closed'   and deleted = '0'   order by id desc"
            ssqlbug4 = "select id from zt_bug where pri=1 and status = 'active' and openedBy='"+openedby[i]+"' and openedDate < '"+str(self.test_time(7))+"'  and deleted = '0'  "
            ssqlbug5 = "select id from zt_bug where pri=2 and status = 'active' and openedBy='"+openedby[i]+"' and openedDate < '" + str(self.test_time(10)) + "'  and deleted = '0' "
            ssqlcsd1 = "select id from zt_testtask  where end < '"+str(self.test_time(1))+"' and (status = 'wait' or status = 'doing') and owner = '"+openedby[i]+"' and deleted = '0'"
            ssqlcsd2 = "select id from zt_testtask where id not in (select DISTINCT(task) from zt_testrun " \
                           "where task>100) and id > 100 and begin < '" + str(self.test_time(2)) + "' and owner = '" + openedby[i] + "'  and deleted = '0'"
            ssqlcsd3 = "select distinct(k.id) from zt_testtask k LEFT JOIN zt_testrun r on k.id = r.task  left join zt_case c on r.`case` = c.id  where k.`begin` <  '"+str(self.test_time(2))+"' and r.`status` = 'wait' and `owner` = '"+openedby[i]+"' and k.id > 100 and k.deleted = '0' and k.`status` = 'done'    and  c.`status` != 'normal'"

            ssqlcase = "select id from zt_case where reviewedBy = '' and `status` != 'normal'  and openedDate < '"+str(self.test_time(5))+"' and openedBy ='"+openedby[i]+"' and openedDate>'2020-04-01'   and deleted = '0'   "
            ssqllist = [ssqlbug1,ssqlbug2,ssqlbug3,ssqlbug4,ssqlbug5,ssqlcsd1,ssqlcsd2,ssqlcsd3,ssqlcase]
            ssqllists.append(ssqllist)
        print("==========================")
        #print(ssqllists)
        for i in range(len(sqllists)):
            #print("创建人：" + openedby[i])
            snum,num = 1,1
            smhtml,mhtml = "",""
            for k in range(len(sqllists[i])):
                sm = self.openedbys(ssqllists[i][k])
                m = self.openedby(sqllists[i][k])
                if str(sm) != "['']":
                    smm = str(sm).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
                    smhtml += """<p>""" + str(snum) + str(mesglist[k]) + str(smm) + """</p>"""
                    if "测试单没有关联用例" in mesglist[k]:
                        bug1count =  "select count(id) from zt_testtask where id not in (select DISTINCT(task) from zt_testrun " \
                           "where task>880) and id > 100 and begin < '" + str(self.test_time(2)) + "' and owner = '" + openedby[i] + "'  and deleted = '0'"
                        print(bug1count)
                        bug1count = self.openedbys(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, taskid, count, openedby,sf)values(7, '" + str(
                            smm) + "','" + str(bug1count) + "', '" + openedby[i] + "',1)"
                        print(bug1count)
                        print(sqlw)
                        inssql(sqlw)
                    elif "验证的bug滞留时间超过2天" in mesglist[k]:
                        bug1count = "SELECT count(id) from zt_bug where resolution = 'fixed' and resolvedDate <= '" + str(
                            self.test_time(2)) + "' and status = 'resolved' and openedBy ='" + openedby[
                                        i] + "' and deleted = '0'  order by resolvedDate desc"
                        bug1count = self.openedbys(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, bugid, count, openedby,sf)values(1, '" + str(smm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',1)"
                        inssql(sqlw)
                    elif "有未指派的bug" in mesglist[k]:
                        bug1count = "select count(id) from zt_bug where assignedTo = '' and  status != 'closed' and deleted = '0' and openedBy='" + \
                                    openedby[i] + "' and deleted = '0'  order by id desc"
                        bug1count = self.openedbys(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, bugid, count, openedby,sf)values(2, '" + str(smm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',1)"
                        inssql(sqlw)
                    elif "重现步骤描述过于简单" in mesglist[k]:
                        bug1count = "select count(id) from zt_bug where openedBy ='" + openedby[
                            i] + "' and length(steps)<= 65 and type != 'proposal' and  `status` != 'closed'  and deleted = '0'  order by id desc"
                        bug1count = self.openedbys(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, bugid, count, openedby,sf)values(3, '" + str(smm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',1)"
                        inssql(sqlw)
                    elif "P1级bug超过7天未修复" in mesglist[k]:
                        bug1count = "select count(id) from zt_bug where pri=1 and status = 'active' and openedBy='" + \
                                    openedby[i] + "' and openedDate < '" + str(self.test_time(7)) + "' and deleted = '0' "
                        bug1count = self.openedbys(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, bugid, count, openedby,sf)values(4, '" + str(smm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',1)"
                        inssql(sqlw)
                    elif "P2级bug超过10天未修复" in mesglist[k]:
                        bug1count = "select count(id) from zt_bug where pri=2 and status = 'active' and openedBy='" + \
                                    openedby[i] + "' and openedDate < '" + str(self.test_time(10)) + "' and deleted = '0' "
                        bug1count = self.openedbys(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, bugid, count, openedby,sf)values(5, '" + str(smm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',1)"
                        inssql(sqlw)
                    elif "提测单延期" in mesglist[k]:
                        bug1count = "select count(id) from zt_testtask  where end < '" + str(
                            self.test_time(1)) + "' and (status = 'wait' or status = 'doing') and owner = '" + openedby[
                                        i] + "' and deleted = '0'"
                        bug1count = self.openedbys(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, taskid, count, openedby,sf)values(6, '" + str(
                            smm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',1)"
                        inssql(sqlw)
                    elif "测试单用例未执行完毕" in mesglist[k]:
                        bug1count = "select count(distinct(k.id)) from zt_testtask k LEFT JOIN zt_testrun r on k.id = r.task   left join zt_case c on r.`case` = c.id   where k.`begin` <  '" + str(
                            self.test_time(2)) + "' and r.`status` = 'wait' and `owner` = '" + openedby[
                                        i] + "' and k.id > 100 and k.deleted = '0'     and  c.`status` != 'normal'"
                        bug1count = self.openedbys(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, taskid, count, openedby,sf)values(8, '" + str(
                            smm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',1)"
                        inssql(sqlw)
                    elif "未评审的用例" in mesglist[k]:
                        bug1count = "select count(id) from zt_case where reviewedBy = '' and `status` != 'normal'  and openedDate < '" + str(
                            self.test_time(5)) + "' and openedBy ='" + openedby[i] + "' and openedDate>'2020-04-01'"
                        bug1count = self.openedbys(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, caseid, count, openedby,sf)values(9, '" + str(
                            smm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',1)"
                        inssql(sqlw)
                    snum += 1
                if str(m) != "['']":
                    mm = str(m).replace("[", "").replace("]", "").replace("'", "").replace(",", "")
                    print("*****************************************************")
                    mhtml += """<p>""" + str(num) + str(mesglist[k]) + str(mm) + """</p>"""
                    if "测试单没有关联用例" in mesglist[k]:
                        bug1count = "select count(id) from zt_testtask where id not in (select DISTINCT(task) from zt_testrun " \
                           "where task>880) and id > 880 and begin < '" + str(self.test_time(2)) + "' and owner = '" + openedby[i] + "'  and deleted = '0'"
                        bug1count = self.openedby(bug1count)
                        bug1count = str(bug1count).replace('[','').replace(']','').replace("'","")
                        bug1count=int(bug1count)
                        sqlw = "insert into tongji(type, taskid, count, openedby,sf)values(7, '"+str(mm)+"','"+str(bug1count)+"', '"+openedby[i]+"',0)"
                        inssql(sqlw)
                    elif "验证的bug滞留时间超过2天" in mesglist[k]:
                        bug1count = "SELECT count(id) from zt_bug where resolution = 'fixed' and resolvedDate <= '"+str(self.test_time(2))+"' and status = 'resolved' and openedBy ='"+openedby[i]+"' and deleted = '0'  order by resolvedDate desc"
                        bug1count = self.openedby(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, bugid, count, openedby,sf)values(1, '" + str(mm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',0)"
                        inssql(sqlw)
                    elif "有未指派的bug" in mesglist[k]:
                        bug1count =  "select count(id) from zt_bug where assignedTo = '' and  status != 'closed' and deleted = '0' and openedBy='"+openedby[i]+"' and deleted = '0'  order by id desc"
                        bug1count = self.openedby(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, bugid, count, openedby,sf)values(2, '" + str(mm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',0)"
                        inssql(sqlw)
                    elif"重现步骤描述过于简单" in mesglist[k]:
                        bug1count = "select count(id) from zt_bug where openedBy ='" + openedby[i] + "' and length(steps)<= 65 and type != 'proposal' and  `status` != 'closed' and deleted = '0'  order by id desc"
                        bug1count = self.openedby(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, bugid, count, openedby,sf)values(3, '" + str(mm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',0)"
                        inssql(sqlw)
                    elif "P1级bug超过7天未修复" in mesglist[k]:
                        bug1count = "select count(id) from zt_bug where pri=1 and status = 'active' and openedBy='"+openedby[i]+"' and openedDate < '"+str(self.test_time(7))+"' and deleted = '0' "
                        bug1count = self.openedby(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, bugid, count, openedby,sf)values(4, '" + str(mm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',0)"
                        inssql(sqlw)
                    elif "P2级bug超过10天未修复" in mesglist[k]:
                        bug1count = "select count(id) from zt_bug where pri=2 and status = 'active' and openedBy='"+openedby[i]+"' and openedDate < '" + str(self.test_time(10)) + "' and deleted = '0' "
                        bug1count = self.openedby(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, bugid, count, openedby,sf)values(5, '" + str(mm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',0)"
                        inssql(sqlw)
                    elif "提测单延期" in mesglist[k]:
                        bug1count = "select count(id) from zt_testtask  where end < '"+str(self.test_time(1))+"' and (status = 'wait' or status = 'doing') and owner = '"+openedby[i]+"' and deleted = '0' "
                        bug1count = self.openedby(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, taskid, count, openedby,sf)values(6, '" + str(mm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',0)"
                        inssql(sqlw)
                    elif "测试单用例未执行完毕" in mesglist[k]:
                        bug1count = "select count(distinct(k.id)) from zt_testtask k LEFT JOIN zt_testrun r on k.id = r.task   left join zt_case c on r.`case` = c.id   where k.`begin` <  '"+str(self.test_time(2))+"' and r.`status` = 'wait' and `owner` = '"+openedby[i]+"' and k.id > 850 and k.deleted = '0'    and  c.`status` != 'normal'"
                        bug1count = self.openedby(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, taskid, count, openedby,sf)values(8, '" + str(mm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',0)"
                        inssql(sqlw)
                    elif "未评审的用例" in mesglist[k]:
                        bug1count = "select count(id) from zt_case where reviewedBy = '' and `status` != 'normal'  and openedDate < '"+str(self.test_time(5))+"' and openedBy ='"+openedby[i]+"' and openedDate>'2020-04-01'"
                        bug1count = self.openedby(bug1count)
                        bug1count = str(bug1count).replace('[', '').replace(']', '').replace("'", "")
                        bug1count = int(bug1count)
                        sqlw = "insert into tongji(type, caseid, count, openedby,sf)values(9, '" + str(mm) + "','" + str(
                            bug1count) + "', '" + openedby[i] + "',0)"
                        inssql(sqlw)

                        #print(mhtml)
                    num += 1
            html = mhtml + smhtml
            #print(html)
            saascslist = "zhebo.lin@vhall.com,chengtai.wang@vhall.com,xiongbing.li@vhall.com,yanan.cheng@vhall.com"
            paascslist = "zhebo.lin@vhall.com,chengtai.wang@vhall.com,xiongbing.li@vhall.com,meiqi.lian@vhall.com,yangdong.chen@vhall.com "
            lmtcdlist = "zhebo.lin@vhall.com,chengtai.wang@vhall.com,xiongbing.li@vhall.com,zhanyuan.song@vhall.com"
            saas = "jinhuan.ren@vhall.com,ronghuan.wang@vhall.com,wenlong.liu@vhall.com,xin.hou@vhall.com,yanan.cheng@vhall.com,yanmin.qin@vhall.com,yuxin.shao@vhall.com,juan.zou@vhall.com"
            paas = 'dekai.dang@vhall.com,mei.fu@vhall.com,meiqi.lian@vhall.com,mingchao.yang@vhall.com,qi.tian@vhall.com,wanqian.li@vhall.com,zhishuai.si@vhall.com,bp.wangyan@vhallops.com,bp.zhangkun@vhallops.com,yangdong.chen@vhall.com '
            lmt = 'zhanyuan.song@vhall.com,ya.zhou@vhall.com'
            testkyj = 'yingjie.kang@vhall.com'
            testcs = "yingjie.kang@vhall.com,zhebo.lin@vhall.com"
            sf = "<p>----------------------以下是第三方禅道相关信息------------------------</p>"
            if str(mhtml) != "" and str(smhtml) != "":
                html = mhtml+sf+smhtml
                print( openedby[i])
                print(html)
                # semail("yingjie.kang@vhall.com", "yingjie.kang@vhall.com", "测试", str(openedby[i]) + "你好：" + str(html))
                if str(openedby[i]) == "bp.zhangkun" or str(openedby[i]) == "bp.wangyan":
                    if str(openedby[i]) in paas:
                        semail(str(openedby[i]) + "@vhallops.com", paascslist, self.sub,
                               str(openedby[i]) + "你好" + str(html))
                    # if str(openedby[i]) in paas:
                    #     semail(str(openedby[i]) + "@vhallops.com", 'zhebo.lin@vhall.com,yingjie.kang@vhall.com', self.sub,
                    #            str(openedby[i]) + "你好" + str(html))
                else:
                    if str(openedby[i]) in lmt:
                        semail(str(openedby[i])+"@vhall.com", lmtcdlist, self.sub, str(openedby[i]) + "你好" + str(html))
                    if str(openedby[i]) in paas:
                        semail(str(openedby[i])+"@vhall.com", paascslist, self.sub, str(openedby[i]) + "你好" + str(html))
                    if str(openedby[i]) in saas:
                        semail(str(openedby[i])+"@vhall.com", saascslist, self.sub, str(openedby[i]) + "你好" + str(html))
                    if str(openedby[i]) in testkyj:
                        semail(str(openedby[i])+"@vhall.com", testcs, self.sub, str(openedby[i]) + "你好" + str(html))
            elif str(smhtml) != "" and str(mhtml) == "":
                html = sf+smhtml
                print(openedby[i])
                print(html)
                # semail("yingjie.kang@vhall.com", "yingjie.kang@vhall.com", "测试",
                #         str(openedby[i]) + "你好：" + str(html))
                if str(openedby[i]) == "bp.zhangkun" or str(openedby[i]) == "bp.wangyan":
                    if str(openedby[i]) in paas:
                        semail(str(openedby[i]) + "@vhallops.com", paascslist, self.sub,
                               str(openedby[i]) + "你好" + str(html))
                    # semail(str(openedby[i]) + "@vhallops.com", 'zhebo.lin@vhall.com,yingjie.kang@vhall.com', self.sub,
                    #        str(openedby[i]) + "你好" + str(html))
                else:
                    if str(openedby[i]) in lmt:
                        semail(str(openedby[i])+"@vhall.com", lmtcdlist, self.sub, str(openedby[i]) + "你好" + str(html))
                    if str(openedby[i]) in paas:
                        semail(str(openedby[i])+"@vhall.com", paascslist, self.sub, str(openedby[i]) + "你好" + str(html))
                    if str(openedby[i]) in saas:
                        semail(str(openedby[i])+"@vhall.com", saascslist, self.sub, str(openedby[i]) + "你好" + str(html))
                    if str(openedby[i]) in testkyj:
                        semail(str(openedby[i])+"@vhall.com", testcs, self.sub,
                               str(openedby[i]) + "你好" + str(html))
            elif str(mhtml) == "" and str(smhtml) == "":
                pass
            else:
                html = mhtml
                print(openedby[i])
                print(html)
                # semail("yingjie.kang@vhall.com", "yingjie.kang@vhall.com", "测试",
                #        str(openedby[i]) + "你好：" + str(html))
                if str(openedby[i]) == "bp.zhangkun" or str(openedby[i]) == "bp.wangyan":
                    if str(openedby[i]) in paas:
                        semail(str(openedby[i]) + "@vhallops.com", paascslist, self.sub,
                               str(openedby[i]) + "你好" + str(html))
                    # semail(str(openedby[i]) + "@vhallops.com", 'zhebo.lin@vhall.com,yingjie.kang@vhall.com', self.sub,
                    #        str(openedby[i]) + "你好" + str(html))
                else:
                    if str(openedby[i]) in lmt:
                        semail(str(openedby[i])+"@vhall.com", lmtcdlist, self.sub, str(openedby[i]) + "你好" + str(html))
                    if str(openedby[i]) in paas:
                        semail(str(openedby[i])+"@vhall.com", paascslist, self.sub, str(openedby[i]) + "你好" + str(html))
                    if str(openedby[i]) in saas:
                        semail(str(openedby[i])+"@vhall.com", saascslist, self.sub, str(openedby[i]) + "你好" + str(html))
                    if str(openedby[i]) in testkyj:
                        semail(str(openedby[i])+"@vhall.com", testcs, self.sub,
                               str(openedby[i]) + "你好" + str(html))


if __name__ == '__main__':
    res = chandao()
    res.test_all()
