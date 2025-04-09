import '../gameobjects/circle'
import '../gameobjects/square-button'

export default class Example extends Phaser.Scene {
  constructor() {
    super({
      key: 'examples'
    })
  }

  create() {
    const vw = this.game.config.width as number / 100
    const vh = this.game.config.height as number / 100

    const circle_button = (this.add as any)
      .circleButton(30 * vw, 50 * vh)
      .on('press', () => console.log('hey watch it! >:('))

    const square_button = (this.add as any)
      .squareButton(70 * vw, 50 * vh)
      .on('press', () => console.log('hey watch it! >:('))
  }
}