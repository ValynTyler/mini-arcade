const hostElement: HTMLInputElement | null = document.querySelector('#host')
const portElement: HTMLInputElement | null = document.querySelector('#port')

const connect_button: HTMLButtonElement | null = document.querySelector('#connect')
const send_button: HTMLButtonElement | null = document.querySelector('#send')

var connection: WebSocket

connect_button?.addEventListener('click', () => {
  const host = hostElement?.value !== '' ? hostElement?.value : 'localhost'
  const port = portElement?.value !== '' ? portElement?.value : 8765

  const address = `ws://${host}:${port}`

  if (!connection || connection.readyState === connection.CLOSED) {
    console.log(`Attempting to connect to \`${address}\`...`)
    connection = new WebSocket(address)
  } else {
    connection.close()
  }

  connection.onopen = () => {
    console.log('Connection established successfully')
    if (hostElement) hostElement.disabled = true
    if (portElement) portElement.disabled = true
    connect_button.textContent = 'Disconnect'
    send_button?.classList.remove('hidden')
  }

  connection.onclose = () => {
    console.log('Closing connection...')
    if (hostElement) hostElement.disabled = false
    if (portElement) portElement.disabled = false
    connect_button.textContent = 'Connect'
    send_button?.classList.add('hidden')
  }

  connection.onmessage = (event) => {
    console.log('Recieved:', event.data)
  }
})

send_button?.addEventListener('click', () => {
  if (connection.readyState === connection.OPEN) {
    connection.send('RED SPY IS IN THE BASE!')
  }
})