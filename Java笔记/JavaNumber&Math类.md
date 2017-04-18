## Java Number & Math 类
一般地，当需要使用数字的时候，我们通常使用内置数据类型，如：`byte`、`int`、`long`、`double` 等。
```
int a = 5000;
float b = 13.65f;
byte c = 0x4a;
```
然而，在实际开发过程中，我们经常会遇到需要使用对象，而不是内置数据类型的情形。为了解决这个问题，Java 语言为每一个内置数据类型提供了对应的包装类。
所有的包装类（`Integer`、`Long`、`Byte`、`Double`、`Float`、`Short`）都是抽象类 `Number` 的子类。

## Java Math 类
Math 的方法都被定义为 static 形式，通过 Math 类可以在主函数中直接调用
```
public class Test {  
    public static void main (String []args)  
    {  
        System.out.println("90 度的正弦值：" + Math.sin(Math.PI/2));  
        System.out.println("0度的余弦值：" + Math.cos(0));  
        System.out.println("60度的正切值：" + Math.tan(Math.PI/3));  
        System.out.println("1的反正切值： " + Math.atan(1));  
        System.out.println("π/2的角度值：" + Math.toDegrees(Math.PI/2));  
        System.out.println(Math.PI);  
    }  
}
----------------------------------------------
90 度的正弦值：1.0
0度的余弦值：1.0
60度的正切值：1.7320508075688767
1的反正切值： 0.7853981633974483
π/2的角度值：90.0
3.141592653589793
```
