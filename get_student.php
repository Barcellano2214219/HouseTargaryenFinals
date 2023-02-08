<?php
// This code retrieves information from two database tables "students" and "users" and performs a left join between the two tables based on a common field "user_id".
include 'db_connect.php';
	
	$qry = $conn->query("SELECT s.*,u.name,u.id as uid,u.username,u.password from students s left join users u  on s.user_id = u.id where s.id='".$_GET['id']."' ");
	if($qry){
		echo json_encode($qry->fetch_array());
	}
