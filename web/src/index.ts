const hostElement: HTMLInputElement | null = document.querySelector('#host')
const portElement: HTMLInputElement | null = document.querySelector('#port')

const button: HTMLButtonElement | null = document.querySelector('#connect')

var connection: WebSocket

button?.addEventListener('click', () => {
  const host = hostElement?.value !== '' ? hostElement?.value : 'localhost'
  const port = portElement?.value !== '' ? portElement?.value : 8765

  const address = `ws://${host}:${port}`

  if (!connection) {
    console.log(`Attempting to connect to \`${address}\`...`)
    connection = new WebSocket(address)
  }

  if (connection.readyState === connection.OPEN) {
    connection.send('RED SPY IS IN THE BASE!')
  }

  connection.onopen = () => {
    console.log('Connection established successfully')
  }

  connection.onmessage = (event) => {
    console.log('Recieved:', event.data)
  }
})