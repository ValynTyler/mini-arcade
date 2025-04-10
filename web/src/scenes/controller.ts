import CircleButton from "../gameobjects/circle-button"
import SquareButton from "../gameobjects/square-button"

export default class Controller extends Phaser.Scene {
  joystick = { x: 0, y: 0 }
  dpad = { up: false, down: false, left: false, right: false }
  menu = false
  power = false

  enableDebug: boolean = true
  private pressTime: number = 0
  private debugText!: Phaser.GameObjects.Text

  private joystick_input!: any
  private dpad_input!: Phaser.GameObjects.Container

  private menu_button!: CircleButton
  private power_button!: SquareButton
  private led_indicator!: Phaser.GameObjects.Arc

  private positionUI = () => {
    const vw = this.game.config.width as number / 100
    const vh = this.game.config.height as number / 100

    this.joystick_input.setPosition(20 * vw, 50 * vh)
    this.menu_button.setPosition(50 * vw, 50 * vh)
    this.power_button.setPosition(50 * vw, 75 * vh)
    this.dpad_input.setPosition(80 * vw, 50 * vh)
    this.led_indicator.setPosition(50 * vw, 25 * vh)
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

    this.joystick_input = (this
      .plugins
      .get('rexvirtualjoystickplugin') as any)
      .add(this, {
        radius: 100,
        forceMin: 0,
        base: this.add.circle(0, 0, 125, 0x111111),
        thumb: this.add.circle(0, 0, 55, 0x1c1c1c).setStrokeStyle(10, 0x111111)
      })
      .on('update', () => {
        console.log(this.joystick_input.forceX, this.joystick_input.forceY)
        this.joystick.x = this.joystick_input.forceX
        this.joystick.y = this.joystick_input.forceY
      })

    this.menu_button = new CircleButton(this, 0, 0)
      .on('release', () => {
        this.menu = false
        let releaseTime = Date.now()
        let timeHeld = releaseTime - this.pressTime
        if (timeHeld > 3000) {
          this.enableDebug = !this.enableDebug
        }
      })
      .on('press', () => {
        console.log('pressed menu')
        this.menu = true
        this.pressTime = Date.now()
      })

    this.power_button = new SquareButton(this, 0, 0)
      .setFaceColor(0x00ff00)
      .setStemColor(0x00bb00)
      .on('release', () => this.power = false)
      .on('press', () => {
        console.log('pressed power')
        this.power = true
      })

    this.dpad_input = this
      .add
      .container(0, 0, [
        this.add.circle(0, 0, 125, 0x111111),
        new SquareButton(this, 0, -75).on('press', () => { console.log('pressed dpad up'); this.dpad.up = true }).on('release', () => this.dpad.up = false),
        new SquareButton(this, 0, 75).on('press', () => { console.log('pressed dpad down'); this.dpad.down = true }).on('release', () => this.dpad.down = false),
        new SquareButton(this, -75, 0).on('press', () => { console.log('pressed dpad left'); this.dpad.left = true }).on('release', () => this.dpad.left = false),
        new SquareButton(this, 75, 0).on('press', () => { console.log('pressed dpad right'); this.dpad.right = true }).on('release', () => this.dpad.right = false),
      ])

    this.led_indicator = this
      .add
      .circle(0, 0, 8, 0xffffff)
      .setStrokeStyle(4, 0xbbbbbb)

    this.debugText = this.add
      .text(0, 0, '')

    this.scale.on('resize', this.positionUI)
    this.positionUI()
  }

  update() {
    let s = ''

    if (this.enableDebug) {
      this.menu_button.area_visible = true;
      this.power_button.area_visible = true;
      this.dpad_input.each((child: any) => {
        child.area_visible = true;
      })

      s = `[debug mode]\n`
        + `\n`
        + `joystick x: ${this.joystick.x}\n`
        + `joystick y: ${this.joystick.y}\n`
        + `\n`
        + `dpad:\n`
        + `  up:    ${this.dpad.up}\n`
        + `  down:  ${this.dpad.down}\n`
        + `  left:  ${this.dpad.left}\n`
        + `  right: ${this.dpad.right}\n`
        + `\n`
        + `menu: ${this.menu}\n`
        + `power: ${this.power}\n`
    } else {
      this.menu_button.area_visible = false;
      this.power_button.area_visible = false;
      this.dpad_input.each((child: any) => {
        child.area_visible = false;
      })
    }

    this.debugText.setText(s)
  }
}