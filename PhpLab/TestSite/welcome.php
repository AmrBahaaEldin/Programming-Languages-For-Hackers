<?php

//expolit in web   def attack  xss    this htmlspecialchars  fliter encode 
//<script>alert("")</script>



//Server is get and post 
///recevide data 
$x=$_POST['username'];
$y=$_POST['email'];
echo("$x ____ $y<br>");

$user=htmlspecialchars($_GET['username']);
$pass=htmlspecialchars($_GET['email']);
echo("$user<hr>$pass");



?>



