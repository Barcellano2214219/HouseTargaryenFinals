<?php 
// This code is a PHP script that deletes a record from a database table named "questions".
include 'db_connect.php';
extract($_GET);
$delete = $conn->query("DELETE FROM questions where  id=".$id);
if($delete)
	echo true;
