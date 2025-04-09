import CircleButton from '../gameobjects/circle-button'
import SquareButton from '../gameobjects/square-button'

export default class Example extends Phaser.Scene {
  constructor() {
    super()
  }

  create() {
    const vw = this.game.config.width as number / 100
    const vh = this.game.config.height as number / 100

    let square_button = new SquareButton(this, 20 * vw, 50 * vh)
      .setFaceColor(0x00ff00)
      .setStemColor(0x00bb00)
      .on('press', () => console.log('square button'))

    let circle_button = new CircleButton(this, 80 * vw, 50 * vh)
      .setFaceColor(0x0000ff)
      .setStemColor(0x0000bb)
      .on('press', () => console.log('circle button'))
  }
}