import Phaser from 'phaser'

import Example from './scenes/example'

var config = {
  type: Phaser.AUTO,
  parent: 'canvas-container',
  width: 800,
  height: 440,
  backgroundColor: 0xbbbbbb,
  scale: {
    mode: Phaser.Scale.FIT,
    autoCenter: Phaser.Scale.CENTER_BOTH,
  },
  scene: Example,
}

var game = new Phaser.Game(config)