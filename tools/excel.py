#!/usr/bin/env python3

import pandas as pd
import os

dirname = "./files"

def allwork():
    oot=disk()
    for root, _, filenames in os.walk(dirname):
        for filename in filenames:
            if filename.startswith('.'):
                continue
            else:
                realname=os.path.join(root, filename)
                ex=excel(realname)
                ex.prepare()
                ex.cal()
                oot.writeResult(filename,ex.output)
    oot.writeDisk()

class disk:
    def __init__(self):
        self.dstname= dirname+"/result.xlsx"
        self.buffer=pd.DataFrame([])

    def writeResult(self,fname,nlist):
        xv=pd.DataFrame(nlist,columns=['分类','支出'])
        #添加新列，标记来自哪个文件
        xv['from']=fname
        self.buffer=self.buffer.append(xv,ignore_index=True)
        print(self.buffer)

    def writeDisk(self):
        with pd.ExcelWriter(self.dstname) as writer:
            self.buffer.to_excel(writer,sheet_name='Sheet1')

class excel:
    def __init__(self,name):
        self.name=name
        self.paytypes=[]
        self.output=[]
    def show(self):
        #data = pd.read_excel(self.name,sheet_name= 0,index_col=0,header=0)
        #print(data.info())
        print(self.name)

    def prepare(self):
        data = pd.read_excel(self.name,sheet_name= 0,index_col=0,header=0)
        items= data["备注"].unique()
        for item in items:
            if item==None or item=="":
                print("get nil item,please check file")
            else:
                self.paytypes.append(item)
    def cal(self):
        data = pd.read_excel(self.name,sheet_name= 0,index_col=0,header=0)
        for item in self.paytypes:
            targets=data[data["备注"]==item].iloc[:,[1,2]]
            result=targets["支出"].sum()
            #print ("对于分类:",item, "总支出为",result)
            self.output.append([item,result])

def main():
    allwork()

if __name__ == '__main__':
    main()
