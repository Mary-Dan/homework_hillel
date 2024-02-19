<!DOCTYPE html>
<html>
<head>
    <title>Input Page</title>
</head>
<body>
    <h2>Input Page</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
