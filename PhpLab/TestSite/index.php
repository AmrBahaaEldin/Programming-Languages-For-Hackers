<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TestSite</title>
</head>

<body>
    <!--br is new line -->
    <!-- action where you go  file or database ||
     method get or post ||
     Name: input is label 
     -->

    <form action="welcome.php" method="post">
        Name: <input name="username" type="text"><br>
        E-mail: <input name="email" type="text"><br>
        <input name="submit" type="submit">
    </form>
    <?php
    //run server => localhost:8000/index.php
    $color = "red";
    echo "my first php script!<br> help me <br>";
    echo "my car is $color <br>";

    //funcation
    function myMessage($name)
    {
        echo "hello  $name";
    }
    myMessage("amr");




    ?>
</body>

</html>