import Phaser from 'phaser'

import Controller from './scenes/controller'

var config = {
  type: Phaser.AUTO,
  parent: 'phaser-example',
  width: 800,
  height: 440,
  // scale: {
  //     mode: Phaser.Scale.FIT,
  //     autoCenter: Phaser.Scale.CENTER_BOTH,
  // },
  scene: Controller,
  backgroundColor: 0x1c1c1c
}

var game = new Phaser.Game(config)