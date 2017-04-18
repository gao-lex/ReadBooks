## while循环：
```
while( 布尔表达式 ) {
  //循环内容
}
```

## do...while循环：
```
do {
       //代码语句
}while(布尔表达式);
```

## for循环：
```
for(初始化; 布尔表达式; 更新) {
    //代码语句
}
```

## Java 增强 for 循环
```
for(声明语句 : 表达式)
{
   //代码句子
}
```

eg:
```
public class Test {
   public static void main(String args[]){
      int [] numbers = {10, 20, 30, 40, 50};
 
      for(int x : numbers ){
         System.out.print( x );
         System.out.print(",");
      }
      System.out.print("\n");
      String [] names ={"James", "Larry", "Tom", "Lacy"};
      for( String name : names ) {
         System.out.print( name );
         System.out.print(",");
      }
   }
}
---------------------------------------------------------
10,20,30,40,50,
James,Larry,Tom,Lacy,
```

## break关键字
```
public class Test {
   public static void main(String args[]) {
      int [] numbers = {10, 20, 30, 40, 50};
 
      for(int x : numbers ) {
         // x 等于 30 时跳出循环
         if( x == 30 ) {
            break;
         }
         System.out.print( x );
         System.out.print("\n");
      }
   }
}
---------------------------------------------
10
20
```

## continue 关键字
```
public class Test {
   public static void main(String args[]) {
      int [] numbers = {10, 20, 30, 40, 50};
 
      for(int x : numbers ) {
         if( x == 30 ) {
        continue;
         }
         System.out.print( x );
         System.out.print("\n");
      }
   }
}

----------------------------------------------
10
20
40
50
```