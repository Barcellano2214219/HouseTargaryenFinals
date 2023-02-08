<?php
// Connects to a MySQL database using the PHP mysqli extension
$conn= new mysqli('localhost','root','','quiz_db')or die("Could not connect to mysql".mysqli_error($con));
