<?php
$servername = "10.104.247.162";
$username = "root";
$password = "whitetree";
$dbname = "whitetree";

// Create connection
$conn = new mysqli($servername, $username, $password,$dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>