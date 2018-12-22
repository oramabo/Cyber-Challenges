<?php
$servername = "localhost";
$username = "root2";
$password = "password";
$dbname = "new_schema";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error){
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT * FROM master_table";
$result = $conn->query($sql);

if ($result->num_rows > 0){
    while($row = $result->fetch_assoc()){
        echo "Username: " . $row["Usernames"]. " - - - Password: " . $row["Passwords"]. "<br>";
    }
} else{
    echo "0 results";
}
$conn->close();
?>