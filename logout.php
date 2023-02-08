<?php 
// This code is a PHP script that logs out the user by ending the current session and redirecting them to the login page.
session_start();
$login = $_SESSION['login_user_type'];
session_destroy();
header('location:login.php');
