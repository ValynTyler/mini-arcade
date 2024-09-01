var connection = new WebSocket('ws://' + "localhost" + ':8765');

connection.onopen = function () {
    console.log("Connection established successfully")
    connection.send("RED SPY IS IN THE BASE!")
}

connection.onmessage = function (event) {
    console.log(event.data)
}
