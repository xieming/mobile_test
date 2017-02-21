#coding=utf-8
import threading
import os
import re
import time
import xlsxwriter
from xlsxwriter import workbook
from xlsxwriter.workbook import Workbook
import time

class CpuGet(threading.Thread):

    _list = []
    flag = True
    sleepTime = 1
    num = 0
    _start0 = 0
    _end0 = 0
    _start1 = 0
    _end1 = 0

    def __init__(self,num=20,sleepTime=1):
        threading.Thread.__init__(self)
        self.num = num
        self.maxline = num
        self.pid,self.pName = CTools().getCurrentPID()
        self.sleepTime = sleepTime

    def run(self):
        # self._start0 = CTools().getTotalCpuTime()
        # self._start1 = CTools().getPIDCpuTime(self.pid)
        while self.flag:
            time.sleep(self.sleepTime)
            #self._end0 = CTools().getTotalCpuTime()
            self._end1 = CTools().getPIDCpuTime(self.pName)
            #cpuUsage = float((self._end1-self._start1))/(self._end0-self._start0)*100
            self._list.append(float('%s'%self._end1))
            print '%s'%self._list
            # self._start0 = self._end0
            # self._start1 = self._end1
            self.num -=1
            if self.num<1:
                self.flag = False
                print 'stop trace!'
                CTools().writeChart(self._list,self.pName,self.maxline-2)

class CTools():

    def getCurrentTime(self):
        return time.strftime('%Y%m%d-%H%M%S',time.localtime())

    def getCurrentPID(self):
        _result = os.popen("adb shell top -n 1 | grep  'engage'").read().strip().split()
        _resultPid = _result[0]
        _resultPName = _result[9]
        print "pid is %s" %(_resultPid )
        print "Name is %s" %(_resultPName)
        return [_resultPid,_resultPName]

    # def getTotalCpuTime(self):
    #     _result = os.popen('adb shell cat /proc/stat').read().strip()
    #     _result = _result.split('\n')[0]
    #     _result = re.findall(u'(\d+)', _result)
    #     _result = reduce(lambda x,y:int(x) + int(y), _result)
    #     return _result
    #
    # def getPIDCpuTime(self,pid):
    #     _result = os.popen('adb shell cat /proc/%s/stat'%pid).read().strip()
    #     _result = re.findall(u'(\d+)', _result)
    #     _result = reduce(lambda x,y:x+y, [int(_result[11]),int(_result[12]),int(_result[13]),int(_result[14])]);
    #     return _result

    def getPIDCpuTime(self,PName):
         _result = os.popen('adb shell dumpsys cpuinfo | grep %s' %PName).read().strip()
         _result = _result[0]
         return _result

    def writeChart(self,_list,_PidName='unknow',_maxline=20):
        workBook = xlsxwriter.Workbook(self.getCurrentTime()+'.xls')
        workSheet = workBook.add_worksheet("CpuInfo")
        workSheet.set_column(1, 1, 15)
        bold = workBook.add_format({"bold":1})
        workSheet.write("A1",u"cpu使用率",bold)
        _row = 1
        for info in _list:
            workSheet.write(_row,0,info)
            _row+=1

        chart = workBook.add_chart({"type":"line"})
        chart.add_series({'categories':"=CpuInfo!$A$2$:A$%d"%(_maxline+1),'values':["CpuInfo",1,0,(_maxline+2),0],'line':{'color': 'red'}})
        chart.set_title({"name":u"CPU"+'\n'+u'进程：'+_PidName})
        chart.set_x_axis({"name":u"次数"})
        chart.set_y_axis({"name":u"当前进程使用率"})
        workSheet.insert_chart(0, 3, chart)   
        workBook.close()

if __name__ == '__main__':
    CpuGet().start()