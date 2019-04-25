def test(func):
    func()
    print("call test")
 
def test1(f):
    f()
    print("call test1")
     
def main():
    @test
    def fun():
        print("call fun")
        @test1
        def fun1():
            print("call fun1")
main()

# 输出
# call fun
# call fun1
# call test1
# call test