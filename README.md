# Damn Vulnerable Web Application (DVWA)

In this repository you will find solutions in terms of python code of the various challanged made available by the famous DVWA. 

To start the application I highly suggest to use the docker image

```sh
docker run --name dvwa --rm -d -it -p 80:80 vulnerables/web-dvwa
```

Then, to correctly executes the script, first create a python virtual environment 

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
- [ ] Brute Force
- [ ] Command Injection
- [ ] Client Side Request Forgery (CSRF)
- [ ] File Inclusion 
- [ ] File Upload
- [ ] Insecure CAPTCHA
- [ ] Weak Session IDs
- [ ] XSS (DOM)
- [ ] XSS (Reflected)
- [ ] XSS (Stored)
- [ ] CSP Bypass
- [ ] Javascript
