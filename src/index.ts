const hostElement: HTMLInputElement = document.querySelector('#host') as HTMLInputElement
const portElement: HTMLInputElement = document.querySelector('#port') as HTMLInputElement

const connect_button: HTMLButtonElement = document.querySelector('#connect') as HTMLButtonElement
const send_button: HTMLButtonElement = document.querySelector('#send') as HTMLButtonElement

const error: HTMLSpanElement = document.querySelector("#error") as HTMLSpanElement

const form: HTMLFormElement = document.querySelector('form') as HTMLFormElement

var connection: WebSocket

form.addEventListener('submit', () => {
  const host = hostElement?.value !== '' ? hostElement?.value : 'localhost'
  const port = portElement?.value !== '' ? portElement?.value : 8765

  const address = `ws://${host}:${port}`

  if (!connection || connection.readyState === connection.CLOSED) {
    console.log(`Attempting to connect to \`${address}\`...`)
    connection = new WebSocket(address)
    connect_button.disabled = true
    connect_button.textContent = 'Connecting...'
  } else {
    connection.close()
  }

  connection.onopen = () => {
    console.log('Connection established successfully')
    if (hostElement) hostElement.disabled = true
    if (portElement) portElement.disabled = true
    send_button?.classList.remove('hidden')
    connect_button.disabled = false
    connect_button.textContent = 'Disconnect'
    error.classList.add('hidden')
  }

  connection.onclose = (event) => {
    console.log('Closing connection...')
    if (hostElement) hostElement.disabled = false
    if (portElement) portElement.disabled = false
    send_button?.classList.add('hidden')
    connect_button.disabled = false
    if (event.wasClean) {
      connect_button.textContent = 'Connect'
    } else {
      connect_button.textContent = 'Retry'
      error.classList.remove('hidden')
      error.classList.remove('error')
      error.offsetWidth
      error.classList.add('error')
    }
  }

  connection.onmessage = (event) => {
    console.log('Recieved:', event.data)
  }
})

send_button.addEventListener('click', () => {
  if (connection.readyState === connection.OPEN) {
    connection.send('RED SPY IS IN THE BASE!')
  }
})