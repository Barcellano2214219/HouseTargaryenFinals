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

<!-- <body>
    <form id="login-frm">
        <div class="form-group">
            <h2>Login</h2>
            <label>UserName</label>
            <input type="text" name="username" placeholder="Username" class="form-control">
        </div>
        <div class="form-group">
            <label>UserName</label>
            <input type="password" name="password" placeholder="Password" class="form-control">
        </div>
        <div class="form-group">
            <button type="submit">Login</button>
        </div>
    </form>
</body> -->

<body>
    <div class = "container">
        <div class = "form-box">
            <div class="logo"></div>
            <h1 id="title">Login</h1>
            
            <form action="" method="post">
                <div class = "input-group">
                    <div class = "input-field" id="nameField">
                        <input type="username" id = "username" placeholder="Username">
                    </div>

                    <div class = "input-field">
                        <input type="password" id ="password" placeholder="Password">
                    </div>
                </div>
                
                <div class="checkbox-text">
                    <div class="checkbox-content">
                        <input type="checkbox" id="logCheck">

                    </div>
                    <p for="logcheck" class="text">Remember me</p>
                </div>

                <p>Forgot password? <a href="#">Click here</a></p>
                
                <div class="btn-field">
                    <button type="button" onclick="validation()" id="loginBtn">Login</button>
                    <button type="button" id = "cancelBtn" class="disable">Cancel</button>
                </div>
            
            
            
            
            </form>
        </div>

        
    </div>



    
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