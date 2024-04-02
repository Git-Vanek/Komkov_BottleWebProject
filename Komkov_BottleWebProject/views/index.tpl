% rebase('layout.tpl', title='Home Page', year=year)

<script>
    function form() {
        var a = document.forms["FORM"]["QUEST"].value;
        if (a == "" || a == null) {
            alert("Please, enter question");
            return false;
        }
        var a = document.forms["FORM"]["ADRESS"].value;
        if (a == "" || a == null) {
            alert("Please, enter email");
            return false;
        }
        var a = document.forms["FORM"]["USERNAME"].value;
        if (a == "" || a == null) {
            alert("Please, enter name");
            return false;
        }
    }
</script>

<div class="jumbotron">
    <h1>Bottle</h1>
    <p class="lead">Bottle is a free web framework for building great Web sites and Web applications using HTML, CSS and JavaScript.</p>
    <p><a href="http://bottlepy.org/docs/dev/index.html" class="btn btn-primary btn-large">Learn more &raquo;</a></p>
</div>

<div class="row">
    <div class="col-md-4">
        <h2>Getting started</h2>
        <p>
            Bottle gives you a powerful, patterns-based way to build dynamic websites that
            enables a clean separation of concerns and gives you full control over markup
            for enjoyable, agile development.
        </p>
        <p><a class="btn btn-default" href="http://bottlepy.org/docs/dev/index.html">Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Get more libraries</h2>
        <p>The Python Package Index is a repository of software for the Python programming language.</p>
        <p><a class="btn btn-default" href="https://pypi.python.org/pypi">Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Microsoft Azure</h2>
        <p>You can easily publish to Microsoft Azure using Visual Studio. Find out how you can host your application using a free trial today.</p>
        <p><a class="btn btn-default" href="http://azure.microsoft.com">Learn more &raquo;</a></p>
    </div>
</div>
<h3> Ask a Question </h3>
<form name="FORM" action="/home" method="post" onsubmit="return form()" required>
        <p><textarea Style="resize: none" rows="2" cols="50" name="QUEST" placeholder="Your question"></textarea></p> 
        <p><input type="text" size="50" name="USERNAME" title="The name must contain only Latin letters and be between 3 and 12 characters long." pattern="[a-zA-Z]{3,12}" placeholder="Your name"></p>
        <p><input type="text" size="50" name="ADRESS" title="The email format is incorrect. E-mail should consist only of Latin letters, numbers and special characters, as well as have from 1 to 12 characters at the beginning and either @gmail.com , or @mail.ru at the end."
            pattern="[a-zA-Z0-9_\-.]{1,12}@(gmail.com|mail.ru)" placeholder="Your email"></p>
        <p><input class="btn btn-default" type="submit" value="Send"></p>
</form>