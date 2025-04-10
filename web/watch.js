#!/usr/bin/env node

import url from 'url'
import path from 'path'

import * as esbuild from 'esbuild'

const __filename = url.fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let ctx = await esbuild.context({
  entryPoints: [ path.join(__dirname, 'src/index.ts') ],
  bundle: true,
  minify: true,
  outfile: path.join(__dirname, 'public', 'bundle.min.js'),
})

await ctx.watch()