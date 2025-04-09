import Phaser from 'phaser'

class Demo extends Phaser.Scene {
  private joystick!: any
  private menu_btn!: Phaser.GameObjects.Arc
  private powr_btn!: Phaser.GameObjects.Rectangle
  private dpad!: Phaser.GameObjects.Container
  private led!: Phaser.GameObjects.Arc
  private text!: Phaser.GameObjects.Text

  private positionUI = () => {
    const vw = config.width / 100
    const vh = config.height / 100

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
      .add(this, { radius: 100, forceMin: 0, })
      .on('update', this.dumpJoyStickState, this)

    this.menu_btn = this
      .add
      .circle(0, 0, 25)
      .setStrokeStyle(2, 0xff0000)
      .setInteractive()
      .on('pointerdown', () => console.log('clicked menu'))

    this.powr_btn = this
      .add
      .rectangle(0, 0, 50, 50)
      .setStrokeStyle(2, 0x00ff00)
      .setInteractive()
      .on('pointerdown', () => console.log('clicked powr'))

    this.dpad = this
      .add
      .container(0, 0, [
        this.add.rectangle(0, -60, 50, 50).setStrokeStyle(2, 0xff0000).setInteractive().on('pointerdown', () => console.log('clicked dpad N')),
        this.add.rectangle(0,  60, 50, 50).setStrokeStyle(2, 0xff0000).setInteractive().on('pointerdown', () => console.log('clicked dpad S')),
        this.add.rectangle( 60, 0, 50, 50).setStrokeStyle(2, 0xff0000).setInteractive().on('pointerdown', () => console.log('clicked dpad E')),
        this.add.rectangle(-60, 0, 50, 50).setStrokeStyle(2, 0xff0000).setInteractive().on('pointerdown', () => console.log('clicked dpad W')),
      ])

    this.led = this
      .add
      .circle(0, 0, 5)
      .setStrokeStyle(2, 0xffffff)

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

var config = {
  type: Phaser.AUTO,
  parent: 'phaser-example',
  width: 800,
  height: 440,
  // scale: {
  //     mode: Phaser.Scale.FIT,
  //     autoCenter: Phaser.Scale.CENTER_BOTH,
  // },
  scene: Demo,
  backgroundColor: 0x333333
}

var game = new Phaser.Game(config)