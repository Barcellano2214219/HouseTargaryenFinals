<?php 
// This code is a PHP script that deletes a record from a database table named "quiz_student_list".
include 'db_connect.php';
extract($_GET);
$delete = $conn->query("DELETE FROM quiz_student_list where  id=".$qid);
if($delete)
	echo true;
