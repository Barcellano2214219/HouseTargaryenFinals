<!DOCTYPE html>
<html>

<head>
    <?php include('header.php') ?>
    <?php
    session_start();
    if (isset($_SESSION['login_id'])) {
        header('Location:home.php');
    }
    ?>
    <title>Admin | Simple Online Quiz System</title>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
    <form class = "container" id="login-frm">     
       <div class="form-box">
            <h1>Login</h1>
            <div class="logo"></div>
            <label for="">Username</label>
            <div class="form-group"> 
                <input type="text" name="username" placeholder="Enter username" class="form-control">
            </div>
            <label for="">Password</label>
            <div class="form-group">
                <input type="password" name="password" placeholder="Enter password" class="form-control">
            </div>
            <div class="btn-field">
                <button type="submit">Login</button>
            </div>
            <div class = "forgot-pass">
                <a href="roll.html">Forgot password?</a>
            </div>
       </div>     
        
    </form>
</body>

<script>
    $(document).ready(function() {
        $('#login-frm').submit(function(e) {
            e.preventDefault()
            $('#login-frm button').attr('disable', true)
            $('#login-frm button').html('Please wait...')

            $.ajax({
                url: './login_auth.php?type=1',
                method: 'POST',
                data: $(this).serialize(),
                error: err => {
                    console.log(err)
                    alert('An error occured');
                    $('#login-frm button').removeAttr('disable')
                    $('#login-frm button').html('Login')
                },
                success: function(resp) {
                    if (resp == 1) {
                        location.replace('home.php')
                    } else {
                        alert("Incorrect username or password.")
                        $('#login-frm button').removeAttr('disable')
                        $('#login-frm button').html('Login')
                    }
                }
            })

        })
    })
</script>

</html>