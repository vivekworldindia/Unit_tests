from hello import hello

def test_hdefault():
   assert hello() == "hello,world"
   
def test_argument():
    for name in ["vivek","ram","vijay"]:
      assert hello(name) == f"hello,{name}"