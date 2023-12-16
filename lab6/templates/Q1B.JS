<!DOCTYPE html>
<html>
<head>
    <title>Q1B</title>
</head>
<body>

<h1 id="helloText">Hello</h1>

<script>
    function setCookie(cname, cvalue, exdays, path) {
        const d = new Date();
        d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
        let expires = "expires=" + d.toUTCString();
        let cookieString = cname + "=" + cvalue + ";" + expires + ";path=" + path;
        document.cookie = cookieString;
    }

    setCookie("Q1B1", "thv20002", 30, "/");
    setCookie("Q1B2", "Nguyen", 30, "/Q1B2");
    setCookie("Q1B3", "172.16.49.54", 30, "/;Secure;");
   
    function getCookie(cname) {
        const name = cname + "=";
        const decodedCookie = decodeURIComponent(document.cookie);
        const cookieArray = decodedCookie.split(';');

        for (let i = 0; i < cookieArray.length; i++) {
            let cookie = cookieArray[i];
            while (cookie.charAt(0) === ' ') {
                cookie = cookie.substring(1);
            }
            if (cookie.indexOf(name) === 0) {
                return cookie.substring(name.length, cookie.length);
            }
        }
        return "";
    }


</script>

</body>
</html>