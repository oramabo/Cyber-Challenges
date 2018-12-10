<html>
<body>
<?php
	$username_html = $_POST['username'];
	echo $username_html. "'s password is ";
	$conn = new mysqli("localhost", "root2", "password" , "new_schema");
	$sql = sprintf('SELECT * FROM master_table WHERE usernames = \'%s\'',mysqli_real_escape_string($conn,$username_html));
	$result = $conn->query($sql);
	if ($result->num_rows > 0){
		while($row = $result->fetch_assoc()){
			echo $row["Passwords"]. "<br>";
		}
	} else{
		echo "nothing because username doesn't exist.";
	}
?>
</body>
</html>