<?php
$host = 'localhost'; // адрес сервера 
$database = 'guestbook'; // имя базы данных
$user = 'root'; // имя пользователя
$password = ''; // пароль
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
	</head>

	<body>
	<style>
	.container{
		margin-left: 0px !important;
    	margin-right: 0px !important;
		max-width: 1920px !important;
	}
	.row {
		width: 100% !important;
	}
	</style>

		<nav class="navbar navbar-light bg-light">
			<a class="navbar-brand" href="#">Vita Stav</a>
		</nav><br>

		<?php

		if(isset($_POST['name']) && isset($_POST['message']) && isset($_POST['data'])){
		
			// подключаемся к серверу
			$link = mysqli_connect($host, $user, $password, $database) 
				or die("Ошибка " . mysqli_error($link)); 
			
			// экранирования символов для mysql
			$name = htmlentities(mysqli_real_escape_string($link, $_POST['name']));
			$message = htmlentities(mysqli_real_escape_string($link, $_POST['message']));
			$data = htmlentities(mysqli_real_escape_string($link, $_POST['data']));
			
			// создание строки запроса
			$query ="INSERT INTO guest VALUES(NULL, '$name','$message','$data')";
			
			// выполняем запрос
			$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
			// закрываем подключение
			mysqli_close($link);
		}
		?>
		<div class="container">
		<div class="row">
			<div class="col-4">
			
				<form method="POST">
					<div class="form-group row">
						<label for="name" class="col-sm-2 col-form-label">Имя</label>
						<div class="col-sm-10">
						<input type="text" name="name" class="form-control" id="inputEmail3">
						</div>
					</div>
					<div class="form-group row">
						<label for="inputPassword3" class="col-sm-2 col-form-label">Сообщение</label>
						<div class="col-sm-10">
						<input type="text" name="message" class="form-control" id="inputPassword3">
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
			<div class="col-8">
			<?php
				
					require_once 'connection.php'; // подключаем скрипт
					
					$link = mysqli_connect($host, $user, $password, $database) 
						or die("Ошибка " . mysqli_error($link)); 
						
					$query ="SELECT * FROM guest";
					
					$result = mysqli_query($link, $query) or die("Ошибка " . mysqli_error($link)); 
					if($result)
					{
						$rows = mysqli_num_rows($result); // количество полученных строк
						?>
						<table class="table table-hover"><tr><th scope="col">Id</th><th scope="col">Имя</th><th scope="col">Сообщение</th><th scope="col">Дата добавления</th></tr>
						<?php
						for ($i = 0 ; $i < $rows ; ++$i)
						{
							$row = mysqli_fetch_row($result);
							echo "<tr>";
								for ($j = 0 ; $j < 4 ; ++$j) echo "<td>$row[$j]</td>";
							echo "</tr>";
						}
						?>
						</table>
						<?php
						// очищаем результат
						mysqli_free_result($result);
					}
					
					mysqli_close($link);
					?>

			</div>
		</div>
		</div>

		<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
		<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
		<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
	
	</body>
</html>