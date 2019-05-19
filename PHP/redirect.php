<?php

	if (isset($_GET["u"]) && $_GET["u"] != "") {
		$u = base64_decode($_GET["u"]);

		$log = $_SERVER["REMOTE_ADDR"] . " > " . $u;
		file_put_contents("v.log", $log.PHP_EOL , FILE_APPEND | LOCK_EX);

		header("Location: " . $u);
		exit();
	}

?>

?u=
