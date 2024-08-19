<?php
// Establish a database connection (replace with your credentials)
$servername = "localhost";
$username = "your_username";
$password = "your_password";
$database = "laptop_price_comparison";

$conn = new mysqli($servername, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get form data
$item = $_POST['item'];
$colour = $_POST['colour'];
$availability = $_POST['availability'];
$available_from = $_POST['available_from'];
$amazon_price = $_POST['amazon_price'];
$flipkart_price = $_POST['flipkart_price'];
$market_price = $_POST['market_price'];

// Insert data into the database
$sql = "INSERT INTO laptops (item, colour, availability, available_from) VALUES ('$item', '$colour', '$availability', '$available_from')";
if ($conn->query($sql) === TRUE) {
    $laptop_id = $conn->insert_id;

    if (!empty($amazon_price)) {
        $sql = "INSERT INTO amazon_prices (laptop_id, price) VALUES ('$laptop_id', '$amazon_price')";
        $conn->query($sql);
    }

    if (!empty($flipkart_price)) {
        $sql = "INSERT INTO flipkart_prices (laptop_id, price) VALUES ('$laptop_id', '$flipkart_price')";
        $conn->query($sql);
    }

    if (!empty($market_price)) {
        $sql = "INSERT INTO market_prices (laptop_id, price) VALUES ('$laptop_id', '$market_price')";
        $conn->query($sql);
    }

    echo "Data inserted successfully.";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
