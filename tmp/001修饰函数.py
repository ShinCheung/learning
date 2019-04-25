# Python函数修饰符，“@”，与其说是修饰函数倒不如说是引用、调用它修饰的函数
def test(f):
    print("before")
    f()
    print("after")

@test
def func():
    print("func was called")

# 输出
# before
# func was called
# after