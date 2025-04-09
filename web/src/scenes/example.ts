export default class Example extends Phaser.Scene {
  constructor() {
    super({
      key: 'examples'
    })
  }

  btn_size: number = 50
  base_size: number = 70
  height: number = 15

  face_color: number = 0xff0000
  stem_color: number = 0xbb0000
  base_color: number = 0x000000

  private target_height: number = this.height
  private actual_height: number = this.height

  private target_face_color: number = this.face_color
  private target_stem_color: number = this.stem_color
  private actual_face_color: number = this.face_color
  private actual_stem_color: number = this.stem_color

  private face!: Phaser.GameObjects.Rectangle
  private stem!: Phaser.GameObjects.Rectangle
  private base!: Phaser.GameObjects.Rectangle

  private onButtonRelease = () => {
    this.target_height = this.height
    this.target_face_color = this.face_color
    this.redrawUI()
  }

  private onButtonPress = () => {
    this.target_height = 0
    this.target_face_color = this.stem_color
    this.redrawUI()
  }

  private redrawUI = () => {
    const stem_position = { x: 0, y: this.btn_size / 2 }
    const face_position = { x: 0, y: -this.actual_height }

    const stem_size = { width: this.btn_size, height: this.actual_height }
    const face_size = { width: this.btn_size, height: this.btn_size }

    this.stem.setPosition(stem_position.x, stem_position.y).setSize(stem_size.width, stem_size.height).setFillStyle(this.actual_stem_color)
    this.face.setPosition(face_position.x, face_position.y).setSize(face_size.width, face_size.height).setFillStyle(this.actual_face_color)
  }

  create() {
    const vw = this.game.config.width as number / 100
    const vh = this.game.config.height as number / 100

    const asdf = 0
    const qwer = 0

    this.base = this
      .add
      .rectangle(0, 0, this.base_size, this.base_size, this.base_color)
      // .setStrokeStyle(25, this.base_color)

    this.face = this
      .add
      .rectangle(0, 0, undefined, undefined, this.face_color)
      // .setStrokeStyle(1, 0x00ff00)
      .setInteractive()
      .on("pointerdown", this.onButtonPress)
      .on("pointerup", this.onButtonRelease)
      .on("pointerout", this.onButtonRelease)

    this.stem = this
      .add
      .rectangle(0, 0, 0, 0, this.stem_color)
      // .setStrokeStyle(1, 0x0000ff)
      .setOrigin(0.5, 1)
      .setInteractive()
      .on("pointerdown", this.onButtonPress)
      .on("pointerup", this.onButtonRelease)
      .on("pointerout", this.onButtonRelease)

    this.add.container(50 * vw, 50 * vh, [
      this.base,
      this.face,
      this.stem,
    ])

    this.redrawUI()
  }

  update () {
    this.actual_height = Phaser.Math.Linear(this.target_height, this.actual_height, 0.5)

    this.redrawUI()
  }
}