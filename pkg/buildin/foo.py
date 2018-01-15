#!/usr/local/bin/python3
num = -10
count = 8
countries = ['US','UK','JAPAN']
words = 'nice to meet you!'
emptyList = []
emptymap = {}
hasascii = '*3\r\n$3\r\nset\r\n$5\r\nhello\r\n$5\r\nworld\r\n'

class person:
    def __init__(self,name,age):
        self.name=name
        self.age = age

def show():
    print('hello world')

#动态执行python代码
#arg 1 must be a string, bytes or code object
def show_exec():
    exec('print("Hello World")')
    exec("""for i in range(5):
        print("iter time: %d" % i)
        """)
#过滤
#filter(function, iterable)
def show_filter():
    def is_odd(n):
        return n % 2 == 1
    l = filter(is_odd,[1,9,34,28,7])
    print(tuple(l))

def test():
    #绝对值
    x = abs(num)
    print(type(x),x)
    #如果iterable的所有元素为真（或者iterable为空）， 返回True
    print(all(countries),all(emptyList))
    # 如果iterable的任一元素为真，返回True。如果iterable为空，返回False
    print(any(emptymap))
    #返回Ascii-only，相对与repr
    #repr返回printable
    print(ascii(hasascii),repr(hasascii))
    #返回整形的二进制形式
    print(bin(num))
    # 检查一个对象是否可调用,实现了__call__方法的类也是可调用的
    print(callable(show))
    # 返回整形值unicode对应的字符
    print(chr(97))
    #bool() 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False
    print(bool(num),bool(""))
    #class bytearray(source[,encoding])
    #if source is 正整数，返回该长度字节数组（0值）
    #if source is string, 按照编码方式，返回字节序列
    print(bytearray(count),'\n',bytearray(words,'utf-8'))
    # 设置object的属性,获取对象的属性,判定是否有某个属性
    a=person('lee',40)
    setattr(a,'name','jacky')
    print(getattr(a,'name'),hasattr(a,'location'))

    #dict 创建一个字典
    #class dict(**kwarg)
    #class dict(mapping, **kwarg)
    #class dict(iterable, **kwarg)
    mp=dict(a='a', b='b', t='t')
    mp=dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    mp=dict([('one', 1), ('two', 2), ('three', 3)])
    #不加参数，返回当前作用域内的变量名,方法名
    #加参数，返回那个对象的属性,方法列表
    print(dir(),dir(person))

    #divmod(a,b) ,返回一个包含商和余数的元组(a // b, a % b)
    print(divmod(13,4))

    #用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
    #初始索引值为0，可以改变
    a=enumerate(countries)
    a=enumerate(countries,start=5)
    for i,v in a:
        print(i,v)

    #用来执行一个字符串表达式，并返回表达式的值
    print(eval('pow(2,10)'))

    #input: iterable object
    #output: frozenset集合，不可修改
    print(frozenset(range(10)))

    #会以字典类型返回当前位置的全部全局变量。
    print(globals())

    #用于获取取一个对象的哈希值
    print(hash(words),hash(str(countries)))

    #hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
    print(hex(num))

    #返回对象的唯一性id
    print(id(a))

    #isinstance(object, classinfo)
    #判定一个对象是否是那个类型
    #与type()区别在于该函数考虑对象的继承关系
    print(isinstance(mp,dict),isinstance(countries,(str,int,list)))
    #classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
#class sing:
#    @classmethod
#    def



if __name__ == "__main__":
    test()
    #show_exec()
    #show_filter()
