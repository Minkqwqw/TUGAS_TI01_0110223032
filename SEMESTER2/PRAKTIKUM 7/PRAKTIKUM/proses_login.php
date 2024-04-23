<?php
// tangkap input login
$email = $_POST['email'];
$password = md5($_POST['password']);


$credential = [$email, $password];

include_once('koneksi.php');

// query login
$query = "SELECT * FROM users WHERE email = ? && password = ?";
$statement = $dbh->prepare($query, $credential);
$statement->execute($credential);
$result = $statement->fetch() ;


// validasi login
if ($result) {
    session_start();
    $_SESSION["name"] = $result["name"];
    $_SESSION["email"] = $result["email"];  
    // pindahkan halaman ke dashboard.php
    header('Location: dashboard.php');
} else {
    header('Location: index.html');
}
