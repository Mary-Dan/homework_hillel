<!DOCTYPE html>
<html>
<head>
    <title>Session Page</title>
</head>
<body>
    <h2>Session Page</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Set Session Value</button>
    </form>
</body>
</html>
