<?php

$host = 'localhost';
$username = 'root';
$password = '';
$database = 'crud_db';

// create connection
$conn = new mysqli($host, $username, $password, $database);


// check connection
if ($conn->connect_error){
    die("Connection failed: " . $conn->connect_error);
}
