Opening the file in Binary Ninja, I found the strings that the program output when you run it (🤖💬 < Have you got a message for me? > 🗨️ 🤖:)

I also found the main function using this Label : src::main::hf9bc229851763ab9

Then main function do the following (briefly):
1. Print the message
2. Read user input
3. Call src::remove_newline::h49daf0023bf5b77c (clean the user input)
4. Call src::check_flag::h49daf0023bf5b77c(rax_2, rdx_1)
5. Then print a message (panic or no)

So, in order to not get a panic message as a response, ill have to print the flag direclty.

After looking at the check_flag function and understanding what it do,
the function basically receive the ptr to the input bytes of the user input after being cleaned in "remove_newline" and the input length.

Then for each 'char' of the input length, it compare the char with another one that is basically part of the flag.
The check is made using that weird function i found : core::ops::function::FnOnce::call_once, but that function is not really the same everytime.

exemple for the first char check :
```
00408b80    int64_t core::ops::function::FnOnce::call_once::h32497efb348ffe3c(char arg1, int64_t arg2 @ rax)

00408b85        if (arg1 u< 0x48)
00408b9e            core::panicking::panic::h8ddd58dc57c2dc00()
00408b9e            noreturn
00408b9e        
00408b87        if (arg1 == 0x48)
00408b8a            return arg2
00408b8a        
00408bb7        core::panicking::panic::h8ddd58dc57c2dc00()
00408bb7        noreturn
```
the `h32497efb348ffe3c` after the function name is the hash that correspond to the right check. 

so basically, `if input[0] == 0x48`, that means its the first letter of the flag and so on...
but for input[1] it gonna compare using a different value.

Here all the hex code for the flag :
```
0x48, 0x48, 0x42, 0x7b, 0x64, 0x30, 0x6e, 0x74, 0x5f, 0x70, 0x34, 0x6e, 0x31, 0x63, 0x5f, 0x63, 0x34, 0x74, 0x63, 0x68, 0x5f, 0x74, 0x68, 0x65, 0x5f, 0x33, 0x72, 0x72, 0x6f, 0x72, 0x7d
```
simple python script to decode in plain text :
```python
letters = [0x48, 0x54, 0x42, 0x7b, 0x64, 0x30, 0x6e, 0x74, 0x5f, 0x70, 0x34, 0x6e, 0x31, 0x63, 0x5f, 0x63, 0x34, 0x74, 0x63, 0x68, 0x5f, 0x74, 0x68, 0x65, 0x5f, 0x33, 0x72, 0x72, 0x6f, 0x72, 0x7d]
flag = ""

for i in letters:
    flag += chr(i)

print(flag)
```