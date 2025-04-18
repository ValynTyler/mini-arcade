const uptime_element = document.querySelector("#uptime")

const address = "ws://192.168.4.1/ws"
const ws = new WebSocket(address)

ws.onmessage = (event) => {
  uptime_element.textContent = `${(event.data / 1000).toFixed(2)} seconds`
}

ws.onclose = () => {
  console.log("Closed!")
}