<!DOCTYPE html>
<html>
<head>
    <title>Hello</title>
</head>
<body>
    <h1>Hello, {{ username }}!</h1>
    <p><a href="{{ url_for('name') }}">Enter Another Name</a></p>
    <p><a href="{{ url_for('home') }}">Back to Home</a></p>
</body>
</html>
