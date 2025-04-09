import Phaser from 'phaser'

import Controller from './scenes/controller'

var config = {
  type: Phaser.AUTO,
  parent: 'canvas-container',
  width: 800,
  height: 440,
  backgroundColor: 0x1c1c1c,
  scale: {
    mode: Phaser.Scale.FIT,
    autoCenter: Phaser.Scale.CENTER_BOTH,
  },
  scene: Controller,
}

var game = new Phaser.Game(config)