var hostname = "miniarcade.local"
var port = "8765"
var connection = new WebSocket(`ws://${hostname}:${port}`);

connection.onopen = function () {
    console.log("Connection established successfully")
    connection.send("RED SPY IS IN THE BASE!")
}

connection.onmessage = function (event) {
    console.log(event.data)
}
