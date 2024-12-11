<?php
$companyname = $_POST['cname'];
$venue = $_POST['venue'];
$size = $_POST['size'];
$date = $_POST['date'];
$date = date('Y-m-d');
$filename = (string)$_FILES["uploadfile"]["name"];


$servername = "10.104.247.162";
$username = "root";
$password = "********";
$dbname = "whitetree";

$conn = new mysqli($servername, $username, $password,$dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}else {
    $sql = "INSERT INTO `events`(`companyname`, `Venue`, `Size`, `Date`, `Image`) 
        VALUES ('$companyname','$venue','$size','$date','$filename')";
    $run = mysqli_query($conn,$sql);

    global $conn;
    echo "<b>Thank you for your submission, we will get back to you if a DJ is available</b>". "<br>";
    echo "<b>Company Name:</b>" . $companyname . "<br>";
    echo "<b>Venue Type:</b>" . $venue . "<br>";
    echo "<b>Max Attendee size:</b>" . $size . "<br>";
    echo "<b>Date:</b>" . $date . "<br>";


    echo "<b>File uploaded: </b>" . $_FILES["uploadfile"]["name"] . "<br>";
    echo "<b>Type: </b>" . $_FILES["uploadfile"]["type"] . "<br>";
    echo "<b>File Size: </b>" . $_FILES["uploadfile"]["size"]/1024 . "<br>";
    echo "<b>Store in: </b>" . $_FILES["uploadfile"]["tmp_name"] . "<br>";

    $img = (string)$_FILES["uploadfile"]["name"];
    $tmp_img = (string)$_FILES["uploadfile"]["tmp_name"];
    $img_folder = "uploads/";

    if (file_exists($_FILES["uploadfile"]["name"])){
        echo "<h3>The file already exists</h3>";
    } else {
        echo "<h3>File Successfully Uploaded</h3>";
    }

    if($run){
        echo "Database updated successfully";
    }else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

$conn->close();

?>





