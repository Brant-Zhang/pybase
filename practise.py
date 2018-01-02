#!/usr/bin/python3
#coding=utf-8
__version__ = "0.1"
__author__ = "brant"

desc = '''
Well I wonder could it be
When I was dreaming about you baby
You were dreaming of me
Call me crazy
Call me blind
To still be suffering is stupid after all of this time
Did I lose my love to someone better
And does she love you like I do
I do, you know I really really do
'''

fruits = ['apple','balala','orange','mango']

## strings
def pystr():
    print (repr("hello world")) #`x` 反引号
    print (str(1.1+2.2))
    subs = desc.split('\n') #默认以空格分割
    quote = '--'
    song=quote.join(subs).replace('you','she').upper()
    print (subs)
    print (song)
    return

## list
def pylist():
    print(fruits[1:2]*2)
    emptyl=[]
    emptyl.append(fruits[-1])
    print(emptyl,emptyl.count("apple"))
    print('grape' in fruits)

## tuple
def pytuple():
    fr = tuple(fruits)
    print(fr[2:])

## map
def pymap():
    data={}
    data['nanjing'] = 1003
    data['shanghai'] = 'far'
    data['zhejiang']=['hangzhou','ningbo','jinhua']
    m2={"msg":"ok","code":10086}
    data['status']=m2
    print(data['nanjing'],data.get('usa'),data.pop("hello"))

if __name__ == '__main__':
    #pystr()
    #pylist()
    #pytuple()
    pymap()
