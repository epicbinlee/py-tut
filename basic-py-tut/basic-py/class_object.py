import keyword

print(keyword.kwlist)


class Person:
    # 成员变量1
    age: int
    name: str
    hair = 'black'

    # 类名+()=执行了init 成员变量2
    def __init__(self, name='Charlie', age=8):
        self.name = name
        self.age = age

    # toString
    def __repr__(self) -> str:
        return "hair = " + self.hair

    # set方法
    def set_hair(self, value):
        if not isinstance(value, str):
            raise ValueError("value must be str...")
        self.hair = value

    def __getattr__(self, name):
        self.name = name

    def __del__(self):
        print("对象删除")

    # 静态方法
    @staticmethod
    def say(content):
        print(content)


p = Person()
p.say("shu")
Person.say("test")
print(p.name)
p.set_hair("xxx")
print(p.hair)
print(p.__repr__())
print(dir(p))
print(p.__dict__['name'])
