#!/usr/bin/env node

import * as esbuild from 'esbuild'

let ctx = await esbuild.context({
  entryPoints: ['src/index.ts'],
  bundle: true,
  outdir: 'public',
})

await ctx.watch()