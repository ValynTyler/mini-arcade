export default class CircleButton extends Phaser.GameObjects.Container {
  area_visible: boolean = false

  btn_diameter: number = 50
  base_diameter: number = 70
  height: number = 15

  face_color: number = 0xff0000
  stem_color: number = 0xbb0000
  base_color: number = 0x000000

  pressed: boolean = false

  private target_height: number = this.height
  private actual_height: number = this.height

  private area!: Phaser.GameObjects.Shape
  private face!: Phaser.GameObjects.Arc
  private base!: Phaser.GameObjects.Arc
  private stem_circle!: Phaser.GameObjects.Arc
  private stem_square!: Phaser.GameObjects.Rectangle

  constructor(scene: Phaser.Scene, x: number, y: number, area?: Phaser.GameObjects.Shape) {
    super(scene);

    this.scene = scene;
    this.x = x;
    this.y = y;

    this.area = area ? area : this.scene.add
      .circle(0, 0, this.btn_diameter)
      .setStrokeStyle(2, 0x00ff00)
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
      .circle(0, 0, this.base_diameter / 2, this.base_color)

    this.face = this.scene.add
      .circle(0, 0, undefined, this.face_color)

    this.stem_circle = this.scene.add
      .circle(0, 0, undefined, this.stem_color)

    this.stem_square = this.scene.add
      .rectangle(0, 0, undefined, undefined, this.stem_color)
      .setOrigin(0.5, 1)

    this.add(this.base)
    this.add(this.stem_circle)
    this.add(this.stem_square)
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
    const stem_position = { x: 0, y: 0 }
    const face_position = { x: 0, y: -this.actual_height }

    const stem_size = { x: this.btn_diameter, y: this.actual_height }
    const stem_radius = this.btn_diameter / 2
    const face_radius = this.btn_diameter / 2

    if (this.area_visible) {
      this.area.setStrokeStyle(2, 0x00ff00)
    } else {
      this.area.setStrokeStyle()
    }

    this.face.setPosition(face_position.x, face_position.y).setRadius(face_radius).setFillStyle(this.face_color)
    this.stem_circle.setPosition(stem_position.x, stem_position.y).setRadius(stem_radius).setFillStyle(this.stem_color)
    this.stem_square.setPosition(stem_position.x, stem_position.y).setSize(stem_size.x, stem_size.y).setFillStyle(this.stem_color)
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

Phaser.GameObjects.GameObjectFactory.register('circleButton', function (this: Phaser.GameObjects.GameObjectFactory, x: number, y: number) {
  const button = new CircleButton(this.scene, x, y)

  this.displayList.add(button)
  this.updateList.add(button)

  return button
})