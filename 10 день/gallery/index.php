<?php
$host = 'localhost'; // адрес сервера 
$database = 'gallery'; // имя базы данных
$user = 'root'; // имя пользователя
$password = ''; // пароль
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
	</head>

	<style>
	.carousel-item>img {
		margin: 0px 0px 0px 25%; 
		}
		body{
			background-image: url(https://sun1.tele2-kz-astana.userapi.com/vTvwQgnkTWFecBhEKpIG3mpspXu9GPZ53NlHKw/45S3gLtP2Nk.jpg);
		}
	</style>

	<body>

		<nav class="navbar navbar-light bg-light">
			<a class="navbar-brand" href="#">Vita Stav</a>
		</nav><br>

		<?php

		if(isset($_POST['photo'])){
		
			// подключаемся к серверу
			$link = mysqli_connect($host, $user, $password, $database) 
				or die("Ошибка " . mysqli_error($link)); 
			
			// экранирования символов для mysql

			$photo = htmlentities(mysqli_real_escape_string($link, $_POST['photo']));
			
			// создание строки запроса
			$query ="INSERT INTO photo VALUES(NULL, '$photo')";
			
			// выполняем запрос
			$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
			// закрываем подключение
			mysqli_close($link);
		}
		?>
		<div class="container">
		<div class="row">
			<div class="col-12">
			
				<form method="POST">
					<div class="form-group row">
						<label for="photo" class="col-sm-2 col-form-label">Название фото</label>
						<div class="col-sm-10">
						<input type="text" name="photo" class="form-control" id="inputEmail3">
						</div>
					</div>
					<p style="display: none;">
					<input type="text" name="data" value="<?php echo date('Y-m-d H:i:s') ?>" /></p>
					<div class="form-group row">
						<div class="col-sm-10">
						<button type="submit" class="btn btn-primary" style="margin:10px 50% 5px;">Отправить</button>
						</div>
					</div>
				</form>	

			</div>
			<div class="col-12">
			<div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  				<div class="carousel-inner">
				  <div class="carousel-item active">
				  <img src='https://sun9-70.userapi.com/c845417/v845417219/12e35c/hvbM9rzTAT4.jpg' class='d-block w-50'>
				  </div>
				<?php
					
					$link = mysqli_connect($host, $user, $password, $database) 
						or die("Ошибка " . mysqli_error($link)); 
						
					$query ="SELECT * FROM photo";
					
					$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
					if($result)
					{
						$rows = mysqli_num_rows($result); // количество полученных строк
						for ($i = 0 ; $i < $rows ; ++$i)
						{
							$row = mysqli_fetch_row($result);
							echo '<div class="carousel-item">';
								for ($j = 1 ; $j < 2 ; ++$j) echo "<img src='$row[$j]' class='d-block w-50'>";
							echo '</div>';
						}
						?>
						<?php
						// очищаем результат
						mysqli_free_result($result);
					}
					
					mysqli_close($link);
					?>
				 </div>
					<a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
						<span class="carousel-control-prev-icon" aria-hidden="true"></span>
						<span class="sr-only">Previous</span>
					</a>
					<a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
						<span class="carousel-control-next-icon" aria-hidden="true"></span>
						<span class="sr-only">Next</span>
					</a>
				</div>
				</div>
				</div>
				</div>

		<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
		<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
		<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
	</body>
</html>