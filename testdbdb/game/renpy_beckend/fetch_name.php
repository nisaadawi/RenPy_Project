<?php
$servername = "x";
$username = "x";
$password = "x?";
$dbname = "x";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    http_response_code(500);
    echo json_encode(["error" => "Connection failed"]);
    exit();
}

$sql = "SELECT name FROM players ORDER BY id DESC LIMIT 10";
$result = $conn->query($sql);

$names = [];

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $names[] = $row["name"];
    }
}

$conn->close();

header('Content-Type: application/json');
echo json_encode($names);
?>
