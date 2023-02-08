<?php
// This PHP code is a login script. It starts a session and connects to a database. 
// The code then checks if the inputted username and password match any records in the users table in the database.
include 'db_connect.php';
session_start();

extract($_POST);
$type = '';
$qry = $conn->query("SELECT * FROM users where username='$username' and password = '$password' $type ");
if ($qry->num_rows > 0) {
	foreach ($qry->fetch_array() as $k => $val) {
		if ($k != 'password')
			$_SESSION['login_' . $k] = $val;
	}
	echo 1;
} else {
	echo 2;
}
