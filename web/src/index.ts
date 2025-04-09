import Phaser from 'phaser'

import Example from './scenes/example'

var config = {
  type: Phaser.AUTO,
  parent: 'phaser-example',
  width: 800,
  height: 440,
  // scale: {
  //     mode: Phaser.Scale.FIT,
  //     autoCenter: Phaser.Scale.CENTER_BOTH,
  // },
  scene: Example,
  backgroundColor: 0xbbbbbb,
}

var game = new Phaser.Game(config)