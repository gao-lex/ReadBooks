## 创建格式化字符串
我们知道输出格式化数字可以使用 printf() 和 format() 方法。
String 类使用静态方法 format() 返回一个String 对象而不是 PrintStream 对象。
String 类的静态方法 format() 能用来创建可复用的格式化字符串，而不仅仅是用于一次打印输出。
```
System.out.printf("浮点型变量的的值为 " +
                  "%f, 整型变量的值为 " +
                  " %d, 字符串变量的值为 " +
                  "is %s", floatVar, intVar, stringVar);
```

```
String fs;
fs = String.format("浮点型变量的的值为 " +
                   "%f, 整型变量的值为 " +
                   " %d, 字符串变量的值为 " +
                   " %s", floatVar, intVar, stringVar);
```