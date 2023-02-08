<?php
// This PHP code retrieves information from a database table called "quiz_list.
include 'db_connect.php';
	
	$qry = $conn->query("SELECT * from quiz_list where id='".$_GET['id']."' ");
	if($qry){
		echo json_encode($qry->fetch_array());
	}
