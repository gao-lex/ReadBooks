## 声明数组变量：
```
dataType[] arrayRefVar;   // 首选的方法

dataType arrayRefVar[];  // 效果相同，但不是首选方法
```
**建议使用 `dataType[] arrayRefVar` 的声明风格声明数组变量。 `dataType arrayRefVar[]` 风格是来自 C/C++ 语言 ，在Java中采用是为了让 C/C++ 程序员能够快速理解java语言**

## 创建数组：
```
arrayRefVar = new dataType[arraySize];
```
上面的语法语句做了两件事：
* 使用 `dataType[arraySize]` 创建了一个数组。
* 把新创建的数组的引用赋值给变量 `arrayRefVar`。

```
dataType[] arrayRefVar = {value0, value1, ..., valuek};
```

## foreach 循环：能在不使用下标的情况下遍历数组
```
public class TestArray {
   public static void main(String[] args) {
      double[] myList = {1.9, 2.9, 3.4, 3.5};
 
      // 打印所有数组元素
      for (double element: myList) {
         System.out.println(element);
      }
   }
}
```

## 多维数组：
```
String str[][] = new String[3][4];
```
### 多维数组的动态初始化（以二维数组为例）
* 直接为每一维分配空间，格式如下：
```
type arrayName = new typ[arraylenght1][arraylenght2];
```
* 从最高维开始，分别为每一维分配空间，例如：
```
String s[][] = new String[2][];
s[0] = new String[2];
s[1] = new String[3];
s[0][0] = new String("Good");
s[0][1] = new String("Luck");
s[1][0] = new String("to");
s[1][1] = new String("you");
s[1][2] = new String("!");
```

## Arrays 类
* 给数组赋值：通过 fill 方法。
* 对数组排序：通过 sort 方法,按升序。
* 比较数组：通过 equals 方法比较数组中元素值是否相等。
* 查找数组元素：通过 binarySearch 方法能对排序好的数组进行二分查找法操作。
