<?php
// jika tidak ada session, lempar ke halaman login
session_start();
if(!$_SESSION ["email"]){
    header("index.html");}

include_once('top.php');
include_once('menu.php');
?>
<div class="container-fluid px-4">
    <h1 class="mt-4">Dashboard</h1>
    <h3>Selamat datang di halaman admin.</h3>
</div>

<?php
include_once('bottom.php');
?>