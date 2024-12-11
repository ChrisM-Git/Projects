<?php
    $companyname = $_POST['cname'];
    $venue = $_POST['venue'];
    $size = $_POST['size'];
    $date = $_POST['date'];
    $date = date('Y-m-d H:i:s')
$filename = $_FILES['file']['name'];
$servername = "10.104.247.162";
$username = "root";
$password = "whitetree";
$dbname = "whitetree";

$conn = new mysqli($servername, $username, $password,$dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}else {
        $sql = "INSERT INTO `events`(`companyname`, `Venue`, `Size`, `Date`, `image`) 
        VALUES ('$companyname','$venue','$size','$date','$filename')";
        $run = mysqli_query($conn,$sql);
        if($run){
            echo "Database updated successfully";
        }else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
}

$conn->close();
?>


