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




👩🏻‍💻**torch.clamp()**

**errors:** clamp(): argument 'min' must be Number, not Tensor.

**solutions: **可能是pytorch版本不对（尝试降低版本）



👩🏻‍💻**nn.Softmax**

**errors:** RuntimeError: "bitwise_and_cpu" not implemented for 'Float'

**solutions:**&两边没加括号

```py
top2_index = ((tem_top2<freq) & (freq<tem_top1)).nonzero()
```


