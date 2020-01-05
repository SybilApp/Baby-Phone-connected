<!DOCTYPE html>
<html>

<iframe src="http://192.168.137.81:8081" right="500px" width="640px" height="480px" align="right" >

</iframe>

<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("#buttonOn").click(function(){
    $.get("musiqueon.php", function(data, status){

    });
  });
});
</script>
</head>
<body>

<button id="buttonOn">MUSIQUE ON</button>

</body>
</html>
