# Damn Vulnerable Web Application (DVWA)

In this repository you will find solutions in terms of python code of the various challanged made available by the famous DVWA. 

To start the application, you can either use the `vulnerables/web-dvwa` image, which is pre-built but lacks some configuration for two modules (`File Inclusion`, and `Insecure CAPTCHA`)

```sh
docker run --name dvwa --rm -d -it -p80:80 vulnerables/web-dvwa
```

Or you can build an extension of the docker image I have developed on
top of the previous one. To build the extension just put your
re-CAPTCHA keys within a `.env` file in the main folder of the
project. The file should look as follows

```
CAPTCHA_PUBLIC=<YOUR_KEY>
CAPTCHA_PRIVATE=<YOUR_KEY>
```

then perform the build and activate the docker

```
docker build -t dvwa .
docker run --name dvwa --rm -d -it -p80:80 dvwa
```

------------

Finally, to correctly executes the script, first create a python virtual environment 

```sh
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
```

and then modify the `PYTHONPATH` variable, otherwise the imports will
not work properly. This has to be executed within the main folder of
the repository

```sh
export PYTHONPATH=./src
```

You can then execute the main script as follows

```sh
python3 src/main.py
```

# Challenges Completed

Currently the following challenges have been completed

- [X] SQL Injection
- [X] SQL Injection Blind
- [X] Brute Force
- [X] Command Injection
- [X] Client Side Request Forgery (CSRF)
- [X] File Inclusion
- [X] File Upload
- [ ] Insecure CAPTCHA
- [X] Weak Session IDs
- [ ] XSS (DOM)
- [X] XSS (Reflected)
- [X] XSS (Stored)
- [X] CSP Bypass
- [ ] Javascript
