<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<link rel="stylesheet" href="nav_bar.css">
	<!-- It generates a navigation bar at the top with the title "Online Quiz System" and a logout button with the user's name. 
	It also generates a side menu with different options for different user types: "Home", "Student List", "Quiz List", and "Quiz Records".  -->
	<nav class="navbar">
		<div class="container-fluid">
			<div class="navbar-header">
				<p class="navbar-text pull-right text-white">
				<h3>Online Quiz System</h3>
				</p>
			</div>
			<div class="nav-right">
				<a href="logout.php" class="text-dark"> <?php echo $name ?> <i class="fa fa-power-off"></i></a>
			</div>
		</div>
	</nav>

	<div id="sidebar" class="bg-light">
		<div id="sidebar-field">
			<a href="home.php" class="sidebar-item text-dark">
				<div class="sidebar-icon"><i class="fa fa-home"> </i></div> Home
			</a>
		</div>
		<?php if ($_SESSION['login_user_type'] != 3) : ?>
			<div id="sidebar-field">
				<a href="student.php" class="sidebar-item text-dark">
					<div class="sidebar-icon"><i class="fa fa-users"> </i></div> Student List
				</a>
			</div>
			<div id="sidebar-field">
				<a href="quiz.php" class="sidebar-item text-dark">
					<div class="sidebar-icon"><i class="fa fa-list"> </i></div> Quiz List
				</a>
			</div>
			<div id="sidebar-field">
				<a href="history.php" class="sidebar-item text-dark">
					<div class="sidebar-icon"><i class="fa fa-history"> </i></div> Quiz Records
				</a>
			</div>
		<?php else : ?>
			<div id="sidebar-field">
				<a href="student_quiz_list.php" class="sidebar-item text-dark">
					<div class="sidebar-icon"><i class="fa fa-list"> </i></div> Quiz List
				</a>
			</div>
		<?php endif; ?>

	</div>
	<script>
		$(document).ready(function() {
			var loc = window.location.href;
			loc.split('{/}')
			$('#sidebar a').each(function() {
				// console.log(loc.substr(loc.lastIndexOf("/") + 1),$(this).attr('href'))
				if ($(this).attr('href') == loc.substr(loc.lastIndexOf("/") + 1)) {
					$(this).addClass('active')
				}
			})
		})
	</script>

</html>