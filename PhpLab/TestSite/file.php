<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>google</title>
</head>

<body>
    <h1>
        <?php
        $y = $_POST['username'];
        $x = $_POST['email'];
        $fileName="file.txt";
        $file = fopen($fileName,"r") or die("unable to open file!");
        echo fread($file, filesize($fileName));
        fclose($file);

        echo "$file <br>
        UserName:$x,<br>
        Email:$y<br>";

        ?>
    </h1>
</body>

</html>