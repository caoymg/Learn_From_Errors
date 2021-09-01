# Model (based on PyTorch)


👩🏻‍💻**nn.Module**

**errors:** AttributeError: cannot assign module before Module.__init__() call

**solutions:**

```py
 class YmgModel(nn.Module):
        def __init__(self):
            super(YmgModel, self).__init__()
            self.xx = nn.xxx()
```

**comments:** This usually happens when super class's init has not been called. In this case one should start their Neural network class with **super.__init__() call**.



👩🏻‍💻**nn.Softmax**

**errors:** softmax之后的结果都是1.

**solutions: **看下softmax的dim是不是设错了

```py
nn.Softmax(dim=1)
```

**comments:** 😅

