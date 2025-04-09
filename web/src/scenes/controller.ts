const colors = {
  red: 0xff0000,
  grn: 0x00ff00,
  ylw: 0xffff00,
  blu: 0x0000ff,
  lgr: 0x1c1c1c,
  mgr: 0x111111,
  dgr: 0x040404,
}

export default class Controller extends Phaser.Scene {
  private joystick!: any
  private menu_btn!: Phaser.GameObjects.Arc
  private powr_btn!: Phaser.GameObjects.Rectangle
  private dpad!: Phaser.GameObjects.Container
  private led!: Phaser.GameObjects.Arc
  private text!: Phaser.GameObjects.Text

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
    this.joystick = (this
      .plugins
      .get('rexvirtualjoystickplugin') as any)
      .add(this, {
        radius: 100,
        forceMin: 0,
        base: this.add.circle(0, 0, 100, colors.mgr),
        thumb: this.add.circle(0, 0, 50, colors.lgr).setStrokeStyle(10, colors.dgr),
      })
      .on('update', this.dumpJoyStickState, this)

    this.menu_btn = this
      .add
      .circle(0, 0, 25, colors.red)
      .setStrokeStyle(10, colors.mgr)
      .setInteractive()
      .on('pointerdown', () => console.log('clicked menu'))

    this.powr_btn = this
      .add
      .rectangle(0, 0, 50, 50, colors.grn)
      .setStrokeStyle(10, colors.mgr)
      .setInteractive()
      .on('pointerdown', () => console.log('clicked powr'))

    this.dpad = this
      .add
      .container(0, 0, [
        this.add.circle(0, 0, 100, colors.mgr),
        this.add.rectangle( 0, -55, 50, 50, colors.red).setStrokeStyle(10, colors.dgr).setInteractive().on('pointerdown', () => console.log('clicked dpad N')),
        this.add.rectangle( 0,  55, 50, 50, colors.grn).setStrokeStyle(10, colors.dgr).setInteractive().on('pointerdown', () => console.log('clicked dpad S')),
        this.add.rectangle( 55, 0,  50, 50, colors.ylw).setStrokeStyle(10, colors.dgr).setInteractive().on('pointerdown', () => console.log('clicked dpad E')),
        this.add.rectangle(-55, 0,  50, 50, colors.blu).setStrokeStyle(10, colors.dgr).setInteractive().on('pointerdown', () => console.log('clicked dpad W')),
      ])

    this.led = this
      .add
      .circle(0, 0, 6, 0xffffff)
      .setStrokeStyle(4, 0x888888)

    this.text = this.add.text(0, 0, '')
    this.dumpJoyStickState()

    this.scale.on('resize', this.positionUI)
    this.positionUI()
  }

  dumpJoyStickState() {
    var cursorKeys = this.joystick.createCursorKeys()
    var s = 'Key down: '
    for (var name in cursorKeys) {
      if (cursorKeys[name].isDown) {
        s += `${name} `
      }
    }

    s += `
Force: ${Math.floor(this.joystick.force * 100) / 100}
Angle: ${Math.floor(this.joystick.angle * 100) / 100}
`

    s += '\nTimestamp:\n'
    for (var name in cursorKeys) {
      var key = cursorKeys[name]
      s += `${name}: duration=${key.duration / 1000}\n`
    }
    this.text.setText(s)
  }
}