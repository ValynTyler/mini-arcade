import SquareButton from "../gameobjects/buttons/square"

export default class Example extends Phaser.Scene {
  constructor() {
    super({
      key: 'examples'
    })
  }

  create() {
    const vw = this.game.config.width as number / 100
    const vh = this.game.config.height as number / 100

    const square_button = (this.add as any)
      .squareButton(50 * vw, 50 * vh)
      .on('press', () => console.log('hey watch it! >:('))
  }
}

Phaser.GameObjects.GameObjectFactory.register('squareButton', function (this: Phaser.GameObjects.GameObjectFactory, x: number, y: number) {
  const button = new SquareButton(this.scene, x, y)

  this.displayList.add(button)
  this.updateList.add(button)

  return button
})