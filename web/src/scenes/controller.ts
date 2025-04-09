import CircleButton from "../gameobjects/circle-button"
import SquareButton from "../gameobjects/square-button"

export default class Controller extends Phaser.Scene {
  private joystick!: any
  private dpad!: Phaser.GameObjects.Container

  private menu_btn!: CircleButton
  private powr_btn!: SquareButton
  private led!: Phaser.GameObjects.Arc

  private positionUI = () => {
    const vw = this.game.config.width as number / 100
    const vh = this.game.config.height as number / 100

    this.joystick.setPosition(20 * vw, 50 * vh)
    this.menu_btn.setPosition(50 * vw, 50 * vh)
    this.powr_btn.setPosition(50 * vw, 75 * vh)
    this.dpad.setPosition(80 * vw, 50 * vh)
    this.led.setPosition(50 * vw, 25 * vh)
  }

  constructor() {
    super({
      key: 'examples'
    })
  }

  preload() {
    var url = 'https://raw.githubusercontent.com/rexrainbow/phaser3-rex-notes/master/dist/rexvirtualjoystickplugin.min.js'
    this.load.plugin('rexvirtualjoystickplugin', url, true)
  }

  create() {
    this.input.addPointer(10); // if you manage to need more pointers than most people have fingers, I'll be truly impressed.

    this.joystick = (this
      .plugins
      .get('rexvirtualjoystickplugin') as any)
      .add(this, {
        radius: 100,
        forceMin: 0,
        base: this.add.circle(0, 0, 125, 0x111111),
        thumb: this.add.circle(0, 0, 55, 0x1c1c1c).setStrokeStyle(10, 0x111111)
      })
      .on('update', () => console.log(this.joystick.forceX, this.joystick.forceY))

    this.menu_btn = new CircleButton(this, 0, 0)
      .on('press', () => console.log('pressed menu'))

    this.powr_btn = new SquareButton(this, 0, 0)
      .setFaceColor(0x00ff00)
      .setStemColor(0x00bb00)
      .on('press', () => console.log('pressed power'))

    this.dpad = this
      .add
      .container(0, 0, [
        this.add.circle(0, 0, 125, 0x111111),
        new SquareButton(this,  0, -75).on('press', () => console.log('pressed dpad up')),
        new SquareButton(this,  0,  75).on('press', () => console.log('pressed dpad down')),
        new SquareButton(this, -75,  0).on('press', () => console.log('pressed dpad left')),
        new SquareButton(this,  75,  0).on('press', () => console.log('pressed dpad right')),
      ])

    this.led = this
      .add
      .circle(0, 0, 8, 0xffffff)
      .setStrokeStyle(4, 0xbbbbbb)

    this.scale.on('resize', this.positionUI)
    this.positionUI()
  }
}