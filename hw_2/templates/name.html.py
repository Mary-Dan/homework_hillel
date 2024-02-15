<!DOCTYPE html>
<html>
<head>
    <title>Enter Your Name</title>
</head>
<body>
    <h1>Enter Your Name</h1>
    <form method="post" action="{{ url_for('name') }}">
        <input type="text" name="username" placeholder="Your Name" required>
        <button type="submit">Submit</button>
    </form>
    <p><a href="{{ url_for('home') }}">Back to Home</a></p>
</body>
</html>
