<!DOCTYPE html>
<html>
<head>
    <title>Q2</title>
</head>
<body>

<h1 id="helloText">Hello</h1>

<script>
    document.getElementById('helloText').innerText = 'Hello';

    var iframe = document.createElement('iframe');
    iframe.style.display = 'none';
    iframe.src = "http://127.0.0.1:2223/loggedIn?username=AQuinnita54&moneyAmount=5";
    document.body.appendChild(iframe);
</script>

</body>
</html>