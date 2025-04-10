export default class SquareButton extends Phaser.GameObjects.Container {
  area_visible = false

  btn_size: number = 50
  base_size: number = 70
  height: number = 15

  face_color: number = 0xff0000
  stem_color: number = 0xbb0000
  base_color: number = 0x000000

  pressed: boolean = false

  private target_height: number = this.height
  private actual_height: number = this.height

  private area!: Phaser.GameObjects.Shape
  private face!: Phaser.GameObjects.Rectangle
  private stem!: Phaser.GameObjects.Rectangle
  private base!: Phaser.GameObjects.Rectangle

  constructor(scene: Phaser.Scene, x: number, y: number, area?: Phaser.GameObjects.Shape) {
    super(scene);

    this.scene = scene;
    this.x = x;
    this.y = y;

    this.area = area ? area : this.scene.add
      .circle(0, 0, this.btn_size)
      .setStrokeStyle(2, 0xffffff)
      .setInteractive()
      .on("pointerup", this.onButtonRelease)
      .on("pointerdown", this.onButtonPress)
      .on("pointerout", () => {
        if (this.pressed) { this.onButtonRelease() }
      })
      .on("pointerover", (pointer: any) => {
        if (pointer.wasTouch) {
          this.onButtonPress()
        }
      })

    this.base = this.scene.add
      .rectangle(0, 0, this.base_size, this.base_size, this.base_color)

    this.face = this.scene.add
      .rectangle(0, 0, undefined, undefined, this.face_color)

    this.stem = this.scene.add
      .rectangle(0, 0, undefined, undefined, this.stem_color)
      .setOrigin(0.5, 1)

    this.add(this.base)
    this.add(this.stem)
    this.add(this.face)
    this.add(this.area)

    this.scene.add.existing(this)
  }

  private onButtonRelease = () => {
    this.pressed = false
    this.emit('release')
    this.target_height = this.height
    this.redrawUI()
  }

  private onButtonPress = () => {
    this.pressed = true
    this.emit('press')
    this.target_height = 0
    this.redrawUI()
  }

  private redrawUI = () => {
    const stem_position = { x: 0, y: this.btn_size / 2 }
    const face_position = { x: 0, y: -this.actual_height }

    const stem_size = { width: this.btn_size, height: this.actual_height }
    const face_size = { width: this.btn_size, height: this.btn_size }

    if (this.area_visible) {
      this.area.setStrokeStyle(2, 0xffffff)
    } else {
      this.area.setStrokeStyle()
    }

    this.stem.setPosition(stem_position.x, stem_position.y).setSize(stem_size.width, stem_size.height).setFillStyle(this.stem_color)
    this.face.setPosition(face_position.x, face_position.y).setSize(face_size.width, face_size.height).setFillStyle(this.face_color)
    this.base.setFillStyle(this.base_color)
  }

  public setBaseColor(color: number) {
    this.base_color = color
    return this
  }

  public setFaceColor(color: number) {
    this.face_color = color
    return this
  }

  public setStemColor(color: number) {
    this.stem_color = color
    return this
  }

  preUpdate() { this.update() }

  update() {
    this.actual_height = Phaser.Math.Linear(this.target_height, this.actual_height, 0.5)
    this.redrawUI()
  }
}

Phaser.GameObjects.GameObjectFactory.register('squareButton', function (this: Phaser.GameObjects.GameObjectFactory, x: number, y: number) {
  const button = new SquareButton(this.scene, x, y)

  this.displayList.add(button)
  this.updateList.add(button)

  return button
})