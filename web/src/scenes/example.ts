export default class Example extends Phaser.Scene {
  constructor() {
    super({
      key: 'examples'
    })
  }

  private size: number = 100
  private height: number = 20

  private primary_color: number = 0xff0000
  private secondary_color: number = 0xbb0000
  private background_color: number = 0x000000

  private face!: Phaser.GameObjects.Rectangle
  private stem!: Phaser.GameObjects.Rectangle

  private onPointerUp = () => {
    this.height = 20
    this.redrawUI()
  }

  private onPointerDown = () => {
    console.log('clicked!')
    this.height = 0
    this.redrawUI()
  }

  private redrawUI = () => {
    this.stem.setPosition(0, this.size/2).setSize(this.size, this.height)
    this.face.setPosition(0, -this.height).setSize(this.size, this.size)
  }

  create() {
    const vw = this.game.config.width as number / 100
    const vh = this.game.config.height as number / 100

    const asdf = 0
    const qwer = 0

    const hitbox = this
      .add
      .rectangle(0, 0, this.size, this.size)
      .setStrokeStyle(1, 0xff00ff)

    this.face = this
      .add
      .rectangle()
      .setStrokeStyle(1, 0x00ff00)
      .setInteractive()
      .on("pointerdown", this.onPointerDown)
      .on("pointerup", this.onPointerUp)

    this.stem = this
      .add
      .rectangle()
      .setStrokeStyle(1, 0x0000ff)
      .setOrigin(0.5, 1)
      .setInteractive()
      .on("pointerdown", this.onPointerDown)
      .on("pointerup", this.onPointerUp)

    this.add.container(50 * vw, 50 * vh, [
      hitbox,
      this.face,
      this.stem,
    ])

    this.redrawUI()
  }
}