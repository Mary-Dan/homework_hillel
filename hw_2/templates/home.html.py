<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
</head>
<body>
    <h1>Welcome to the Home Page</h1>
    <p><a href="{{ url_for('name') }}">Enter Your Name</a></p>
    <p><a href="{{ url_for('about') }}">About</a></p>
</body>
</html>
