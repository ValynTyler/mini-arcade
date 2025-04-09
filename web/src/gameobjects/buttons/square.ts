export default class SquareButton extends Phaser.GameObjects.Container {
  constructor(scene: Phaser.Scene, x: number, y: number) {
    super(scene);

    this.scene = scene;
    this.x = x;
    this.y = y;

    this.base = this.scene.add
      .rectangle(0, 0, this.base_size, this.base_size, this.base_color)

    this.face = this.scene.add
      .rectangle(0, 0, undefined, undefined, this.face_color)
      .setInteractive()
      .on("pointerdown", this.onButtonPress)
      .on("pointerup", this.onButtonRelease)
      .on("pointerout", this.onButtonRelease)

    this.stem = this.scene.add
      .rectangle(0, 0, 0, 0, this.stem_color)
      .setOrigin(0.5, 1)
      .setInteractive()
      .on("pointerdown", this.onButtonPress)
      .on("pointerup", this.onButtonRelease)
      .on("pointerout", this.onButtonRelease)

    this.add(this.base)
    this.add(this.stem)
    this.add(this.face)

    this.scene.add.existing(this)
  }

  btn_size: number = 50
  base_size: number = 70
  height: number = 15

  face_color: number = 0xff0000
  stem_color: number = 0xbb0000
  base_color: number = 0x000000

  private target_height: number = this.height
  private actual_height: number = this.height

  private face!: Phaser.GameObjects.Rectangle
  private stem!: Phaser.GameObjects.Rectangle
  private base!: Phaser.GameObjects.Rectangle

  private onButtonRelease = () => {
    this.emit('release')
    this.target_height = this.height
    this.redrawUI()
  }

  private onButtonPress = () => {
    this.emit('press')
    this.target_height = 0
    this.redrawUI()
  }

  private redrawUI = () => {
    const stem_position = { x: 0, y: this.btn_size / 2 }
    const face_position = { x: 0, y: -this.actual_height }

    const stem_size = { width: this.btn_size, height: this.actual_height }
    const face_size = { width: this.btn_size, height: this.btn_size }

    this.stem.setPosition(stem_position.x, stem_position.y).setSize(stem_size.width, stem_size.height)
    this.face.setPosition(face_position.x, face_position.y).setSize(face_size.width, face_size.height)
  }

  preUpdate() { this.update() }

  update() {
    this.actual_height = Phaser.Math.Linear(this.target_height, this.actual_height, 0.5)
    this.redrawUI()
  }
}