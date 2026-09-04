StartupEvents.registry('block', event => {
	event.create("wallpaper1").displayName("Wallpaper")
		.fullBlock(true)
		.material("wood")
		.soundType("cherry_wood")
		.unbreakable()
		.mapColor("terracotta_gray")
	event.create('wallpaper_soft').displayName('Wallpaper')
		.model('kubejs:block/wallpaper')
		.fullBlock(true)
		.material("wood")
		.soundType("cherry_wood")
		.waterlogged() //Poolrooms ADDITION
		.noDrops()
		.noCollision()
		.mapColor("terracotta_gray")
	event.create('wallpaper1_slab', 'slab').displayName("Wallpaper Slab")
		.material("wood")
		.soundType("cherry_wood")
		.unbreakable()
		.waterlogged()
		.mapColor("terracotta_gray")

	//Wallpapers
	let wallpaper = (id) => {
		event.create(id).displayName("Wallpaper")
		.fullBlock(true)
		.material("wood")
		.soundType("cherry_wood")
		.unbreakable()
		.mapColor("terracotta_gray")

		event.create(`${id}_soft`).displayName("Wallpaper")
		.model(`kubejs:block/${id}`)
		.fullBlock(true)
		.material("wood")
		.soundType("cherry_wood")
		.waterlogged()
		.noDrops()
		.noCollision()
		.mapColor("terracotta_gray")

		event.create(`${id}_slab`, 'slab').displayName("Wallpaper Slab")
		.material("wood")
		.soundType("cherry_wood")
		.unbreakable()
		.waterlogged()
		.mapColor("terracotta_gray")
	}
	//wallpaper("wallpaper1") //doesnt follow format
	wallpaper("wallpaper2")
	wallpaper("wallpaper3")
	wallpaper("wallpaper4")
	wallpaper("wallpaper5")
	wallpaper("wallpaper6")
	wallpaper("wallpaper7")
	wallpaper("wallpaper8")

	event.create('wallpaper_fake').displayName('Wallpaper')
		.model('kubejs:block/wallpaper1')
		.fullBlock(true)
		.material("wood")
		.soundType("cherry_wood")
		.tagBlock('minecraft:mineable/axe')
		.mapColor("terracotta_gray")
	event.create('wallpaper_white_fake').displayName('Wallpaper')
		.model('kubejs:block/wallpaper5')
		.fullBlock(true)
		.material("wood")
		.soundType("cherry_wood")
		.tagBlock('minecraft:mineable/axe')
		.mapColor("terracotta_gray")
	event.create('wallpaper_pink_fake').displayName('Wallpaper')
		.model('kubejs:block/wallpaper7')
		.fullBlock(true)
		.material("wood")
		.soundType("cherry_wood")
		.tagBlock('minecraft:mineable/axe')
		.mapColor("terracotta_gray")
		
	let strippedwallpapers = (id,grow) => {
		event.create(id).displayName('Stripped Wallpaper')
			.fullBlock(true)
			.material("wood")
			.soundType("cherry_wood")
			.unbreakable()
			.mapColor("terracotta_gray")
			.property(BlockProperties.AGE_3)
			.randomTick(tick => {
				const block = tick.block
				const properties = block.properties
				const age = Number(properties.age)
				if (age == 3) {
					block.set(grow)
				} else {
					block.set(block.getId(), {
						age: `${age + 1}`
					})
				}
			})
	}
	strippedwallpapers('stripped_wallpaper','kubejs:wallpaper1')
	strippedwallpapers('stripped_wallpaper2','kubejs:wallpaper2')
	strippedwallpapers('stripped_wallpaper3','kubejs:wallpaper3')
	//4 intentionally left unable to be stripped
	event.create('stripped_wallpaper5').displayName('Stripped Wallpaper')
		.fullBlock(true)
		.material("wood")
		.soundType("cherry_wood")
		.unbreakable()
		.mapColor("terracotta_gray")
		.property(BlockProperties.AGE_5)
		.randomTick(tick => {
			const block = tick.block
			const properties = block.properties
			const age = Number(properties.age)
			if (age == 5) {
				block.set('kubejs:wallpaper5')
			} else {
				block.set(block.getId(), {
					age: `${age + 1}`
				})
			}
		})
	strippedwallpapers('stripped_wallpaper6','kubejs:wallpaper6')
	strippedwallpapers('stripped_wallpaper7','kubejs:wallpaper7')
	strippedwallpapers('stripped_wallpaper8','kubejs:wallpaper8')

	//Ceiling
	event.create('ceilling').displayName('Ceiling')
		.fullBlock(true)
		.material("wood")
		.soundType("cherry_wood")
		.unbreakable()

	event.create('ceilling2').displayName('Ceiling')
		.fullBlock(true)
		.material("stone")
		.soundType("stone")
		.unbreakable()

	event.create('ceilling_frame').displayName('Ceiling Frame')
		.fullBlock(false)
		.material("wood")
		.soundType("cherry_wood")
		.unbreakable()
		.box(0, 0, 0, 16, 1, 1)
		.box(0, 0, 15, 16, 1, 16)
		.box(0, 0, 1, 1, 1, 15)
		.box(15, 0, 1, 16, 1, 15)

	event.create('ceilling_edge').displayName('Ceiling')
		.fullBlock(true)
		.material("wood")
		.soundType("cherry_wood")
		.unbreakable()

	event.create('ceilling_slab', 'slab').displayName('Ceiling Slab')
		.fullBlock(true)
		.material("wood")
		.soundType("cherry_wood")
		.unbreakable()
		.waterlogged()

	event.create('ceilling_stairs', 'stairs').displayName('Ceiling Stairs')
		.fullBlock(true)
		.material("wood")
		.soundType("cherry_wood")
		.unbreakable()
		.waterlogged()

	event.create('ceilling_lamp').displayName('Ceiling Lamp')
		.unbreakable()
		.material("glass")
		.soundType("glass")
		.lightLevel(1.0)

	event.create('ceilling_lamp2').displayName('Ceiling Lamp')
		.unbreakable()
		.material("glass")
		.soundType("glass")
		.lightLevel(1.0)

	event.create('ceilling_lamp_off').displayName('Ceiling Lamp')
		.unbreakable()
		.material("glass")
		.soundType("glass")


	//Floor
	event.create('carpet').displayName('Carpet')
		.fullBlock(true)
		.material("wool")
		.soundType("wool")
		.unbreakable()
		.mapColor("wood")
	event.create('soggy_carpet')
		.fullBlock(true)
		.material("wool")
		.soundType("coral_block")
		.unbreakable()
		.mapColor("wood")

	event.create('carpet_slab', 'slab')
		.fullBlock(true)
		.material("wool")
		.soundType("wool")
		.unbreakable()
		.resistance(3600000.0)
		.waterlogged()
		.noDrops()
		.mapColor("wood")
	event.create('soggy_carpet_slab', 'slab')
		.fullBlock(true)
		.material("wool")
		.soundType("wool")
		.unbreakable()
		.resistance(3600000.0)
		.waterlogged()
		.noDrops()
		.mapColor("wood")

	event.create('carpet_stairs', 'stairs')
		.fullBlock(false)
		.material("wool")
		.soundType("wool")
		.unbreakable()
		.resistance(3600000.0)
		.waterlogged()
		.noDrops()
		.mapColor("wood")
	event.create('soggy_carpet_stairs', 'stairs')
		.fullBlock(false)
		.material("wool")
		.soundType("wool")
		.unbreakable()
		.resistance(3600000.0)
		.waterlogged()
		.noDrops()
		.mapColor("wood")
	event.create('carpet_soft').displayName('Carpet')
		.model('kubejs:block/carpet')
		.fullBlock(true)
		.material("wool")
		.soundType("wool")
		.waterlogged() //Poolrooms ADDITION
		.noDrops()
		.noCollision()
		.mapColor("wood")
	event.create('carpet_fake').displayName('Carpet')
		.model('kubejs:block/carpet')
		.fullBlock(true)
		.material("wool")
		.soundType("wool")
		.tagBlock('minecraft:mineable/axe')
		.mapColor("wood")

	event.create('red_carpet')
		.fullBlock(true)
		.material("wool")
		.soundType("wool")
		.unbreakable()
		.mapColor("color_red")
	event.create('red_carpet_slab', 'slab')
		.fullBlock(true)
		.material("wool")
		.soundType("wool")
		.unbreakable()
		.resistance(3600000.0)
		.waterlogged()
		.mapColor("color_red")
	event.create('red_carpet_stairs', 'stairs')
		.fullBlock(true)
		.material("wool")
		.soundType("wool")
		.unbreakable()
		.resistance(3600000.0)
		.waterlogged()
		.noDrops()
		.mapColor("color_red")
	event.create('red_carpet_fake').displayName('Red Carpet')
		.model('kubejs:block/red_carpet')
		.fullBlock(true)
		.material("wool")
		.soundType("wool")
		.tagBlock('minecraft:mineable/axe')
		.mapColor("color_red")

	event.create('green_carpet')
		.fullBlock(true)
		.material("wool")
		.soundType("wool")
		.unbreakable()
		.mapColor("color_green")
	event.create('green_carpet_fake').displayName('Green Carpet')
		.model('kubejs:block/green_carpet')
		.fullBlock(true)
		.material("wool")
		.soundType("wool")
		.tagBlock('minecraft:mineable/axe')
		.mapColor("color_green")

	event.create('floor_tiles').tagBlock('kubejs:concrete_tiles')
		.fullBlock(false)
		.material("stone")
		.soundType("stone")
		.unbreakable()
		.mapColor("color_light_gray")
		.box(0, 0, 0, 16, 15, 16)
		.property(BlockProperties.AGE_3)
		.randomTick(tick => {
			const block = tick.block
			const properties = block.properties
			const age = Number(properties.age)
			if (age == 3) {
				block.set('kubejs:carpet')
			} else {
				block.set(block.getId(), {
					age: `${age + 1}`
				})
			}
		})
	event.create('floor_tiles_full').displayName('Floor Tiles')
		.fullBlock(false)
		.material("stone")
		.soundType("stone")
		.unbreakable()
		.mapColor("color_light_gray")

	event.create('floor_tiles_infinite').displayName('Floor Tiles')
		.model('kubejs:block/floor_tiles')
		.fullBlock(false)
		.material("stone")
		.soundType("stone")
		.unbreakable()
		.mapColor("color_light_gray")
		.box(0, 0, 0, 16, 15, 16)

	event.create('floor_tiles_red').displayName('Floor Tiles').tagBlock('kubejs:concrete_tiles')
		.fullBlock(false)
		.material("stone")
		.soundType("stone")
		.unbreakable()
		.mapColor("color_light_gray")
		.box(0, 0, 0, 16, 15, 16)
		.property(BlockProperties.AGE_5)
		.randomTick(tick => {
			const block = tick.block
			const properties = block.properties
			const age = Number(properties.age)
			if (age == 5) {
				block.set('kubejs:red_carpet')
			} else {
				block.set(block.getId(), {
					age: `${age + 1}`
				})
			}
		})
	event.create('floor_tiles_red_full').displayName('Floor Tiles')
		.fullBlock(false)
		.material("stone")
		.soundType("stone")
		.unbreakable()
		.mapColor("color_light_gray")

	event.create('floor_tiles_green').displayName('Floor Tiles').tagBlock('kubejs:concrete_tiles')
		.fullBlock(false)
		.material("stone")
		.soundType("stone")
		.unbreakable()
		.mapColor("color_light_gray")
		.box(0, 0, 0, 16, 15, 16)
		.property(BlockProperties.AGE_5)
		.randomTick(tick => {
			const block = tick.block
			const properties = block.properties
			const age = Number(properties.age)
			if (age == 5) {
				block.set('kubejs:green_carpet')
			} else {
				block.set(block.getId(), {
					age: `${age + 1}`
				})
			}
		})
	event.create('floor_tiles_green_full').displayName('Floor Tiles')
		.fullBlock(false)
		.material("stone")
		.soundType("stone")
		.unbreakable()
		.mapColor("color_light_gray")

	event.create('error').displayName('Divided by Zero')
		.material("shroomlight")
		.soundType("shroomlight")
		.fullBlock(true)
		.hardness(10)
		.mapColor("color_pink")
	event.create('error_carpet').displayName('Divided by Zero')
		.material("shroomlight")
		.soundType("shroomlight")
		.fullBlock(true)
		.hardness(10)
		.mapColor("color_pink")
	event.create('error_wallpaper').displayName('Divided by Zero')
		.material("shroomlight")
		.soundType("shroomlight")
		.fullBlock(true)
		.hardness(10)
		.mapColor("color_pink")

	event.create('oil_carpet').displayName('Crude Oil Soaked Carpet')
		.fullBlock(true)
		.material("wool")
		.soundType("coral_block")
		.unbreakable()
		.mapColor("color_brown")

	event.create('drain').displayName('Drain')
		.fullBlock(true)
		.material("lantern")
		.soundType("lantern")
		.unbreakable()
		.mapColor("metal")
	event.create('carpeted_drain_dry').displayName('Carpet')
		.model('kubejs:block/carpet')
		.fullBlock(true)
		.material("wool")
		.soundType("wool")
		.unbreakable()
		.mapColor("wood")
		.property(BlockProperties.AGE_3)
		.randomTick(tick => {
			const block = tick.block
			const properties = block.properties
			const age = Number(properties.age)
			if (age == 3) {
				block.set('kubejs:carpeted_drain_soggy')
			} else {
				block.set(block.getId(), {
					age: `${age + 1}`
				})
			}
		})
	event.create('carpeted_drain_soggy').displayName('Soggy Carpet')
		.model('kubejs:block/soggy_carpet')
		.fullBlock(true)
		.material("wool")
		.soundType("wool")
		.unbreakable()
		.mapColor("wood")

	//Poolrooms
	event.create('pool_tiles').displayName('Pool Tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.mapColor("quartz")
	event.create('pool_tiles_soft').displayName('Pool Tiles')
		.model('kubejs:block/pool_tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("deepslate")
		.waterlogged()
		.noDrops()
		.noCollision()
		.mapColor("quartz")
	event.create('pool_tiles_slab', 'slab').displayName('Pool Tiles Slab')
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.waterlogged()
		.mapColor("quartz")
	event.create('pool_tiles_stairs', 'stairs').displayName('Pool Tiles Stairs')
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.waterlogged()
		.noDrops()
		.mapColor("quartz")
	event.create('long_pool_tiles').displayName('Pool Tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.mapColor("quartz")
	event.create('long_pool_tiles_soft').displayName('Pool Tiles')
		.model('kubejs:block/long_pool_tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("deepslate")
		.waterlogged()
		.noDrops()
		.noCollision()
		.mapColor("quartz")
	event.create('long_pool_tiles_slab', 'slab').displayName('Pool Tiles Slab')
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.waterlogged()
		.mapColor("quartz")
	event.create('long_pool_tiles_stairs', 'stairs').displayName('Pool Tiles Stairs')
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.waterlogged()
		.noDrops()
		.mapColor("quartz")
	event.create('pool_locker_single').displayName('Pool Locker')
		.soundType("metal")
		.property(BlockProperties.FACING)
		.property(BlockProperties.HALF)
		.unbreakable()
		.mapColor("metal")
		.placementState(state => {
			state.set(BlockProperties.FACING, state.horizontalDirection.opposite)
			state.set(BlockProperties.HALF, 'bottom')
		})
	event.create('pool_locker_double').displayName('Pool Locker')
		.soundType("metal")
		.property(BlockProperties.FACING)
		.property(BlockProperties.HALF)
		.unbreakable()
		.mapColor("metal")
		.placementState(state => {
			state.set(BlockProperties.FACING, state.horizontalDirection.opposite)
			state.set(BlockProperties.HALF, 'bottom')
		})
	event.create('pool_tiles_wet').displayName('Wet Pool Tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.slipperiness(0.99)
		.mapColor("quartz")
	event.create('pool_tiles_wet_slab', 'slab').displayName('Wet Pool Tiles Slab')
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.waterlogged()
		.mapColor("quartz")
	event.create('pool_tiles_wet_stairs', 'stairs').displayName('Wet Pool Tiles Stairs')
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.waterlogged()
		.noDrops()
		.mapColor("quartz")
	event.create('pool_tiles_golden').displayName('Golden Pool Tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("metal")
		.unbreakable()
		.mapColor("gold")
	event.create('pool_tiles_golden_half').displayName('Golden Pool Tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("metal")
		.unbreakable()
		.mapColor("gold")
	event.create('missing_tiles_empty').displayName('Missing Pool Tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.mapColor("stone")
		.property(BlockProperties.AGE_3)
		.randomTick(tick => {
    const block = tick.block
	const properties = block.properties
	const age = Number(properties.age)
	    if (age == 3) {
      		block.set('kubejs:missing_tiles_half')
		} else {
        	block.set(block.getId(), {
          	age: `${age+1}`
        })
	}})
	event.create('missing_tiles_half').displayName('Missing Pool Tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.mapColor("quartz")
		.property(BlockProperties.AGE_5)
		.randomTick(tick => {
    const block = tick.block
	const properties = block.properties
	const age = Number(properties.age)
	    if (age == 5) {
      		block.set('kubejs:pool_tiles')
		} else {
        	block.set(block.getId(), {
          	age: `${age+1}`
        })
	}})
	event.create('missing_tiles_half_wet').displayName('Missing Wet Pool Tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.slipperiness(0.85)
		.mapColor("quartz")
		.property(BlockProperties.AGE_5)
		.randomTick(tick => {
    const block = tick.block
	const properties = block.properties
	const age = Number(properties.age)
	    if (age == 5) {
      		block.set('kubejs:pool_tiles_wet')
		} else {
        	block.set(block.getId(), {
          	age: `${age+1}`
        })
	}})
	event.create('missing_tiles_golden_half').displayName('Missing Golden Pool Tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.mapColor("quartz")
		.property(BlockProperties.AGE_5)
		.randomTick(tick => {
    const block = tick.block
	const properties = block.properties
	const age = Number(properties.age)
	    if (age == 5) {
      		block.set('kubejs:pool_tiles_golden')
		} else {
        	block.set(block.getId(), {
          	age: `${age+1}`
        })
	}})
	event.create('missing_tiles_half_golden').displayName('Missing Pool Tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.mapColor("quartz")
		.property(BlockProperties.AGE_5)
		.randomTick(tick => {
    const block = tick.block
	const properties = block.properties
	const age = Number(properties.age)
	    if (age == 5) {
      		block.set('kubejs:pool_tiles_golden_half')
		} else {
        	block.set(block.getId(), {
          	age: `${age+1}`
        })
	}})
	event.create('pool_tiles_cracked').displayName('Cracked Pool Tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.mapColor("quartz")
	event.create('missing_tiles_half_cracked').displayName('Missing Cracked Pool Tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.mapColor("quartz")
	event.create('pool_tiles_cracked_wet').displayName('Wet Cracked Pool Tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.slipperiness(0.99)
		.mapColor("quartz")
	event.create('missing_tiles_half_cracked_wet').displayName('Missing Wet Cracked Pool Tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("deepslate")
		.unbreakable()
		.slipperiness(0.85)
		.mapColor("quartz")
	event.create('pool_tiles_fake').displayName('Pool Tiles')
		.model('kubejs:block/pool_tiles')
		.fullBlock(true)
		.material("stone")
		.soundType("deepslate")
		.tagBlock('minecraft:mineable/pickaxe')
		.mapColor("quartz")
	event.create('pool_tiles_golden_fake').displayName('Golden Pool Tiles')
		.model('kubejs:block/pool_tiles_golden')
		.fullBlock(true)
		.material("stone")
		.soundType("metal")
		.tagBlock('minecraft:mineable/pickaxe')
		.mapColor("gold")
	
	event.create('carpet_grass')
		.material("wool")
		.soundType("wool")
		.renderType("cutout")
		.fullBlock(false)
		.noCollision()
		.opaque(false)
		.noDrops()
		.hardness(0)
		.tagBlock('minecraft:mineable/hoe')
	
	//loot
	event.create('batteries')
		.material("stone")
		.soundType("lantern")
		.renderType("translucent")
		.fullBlock(false)
		.waterlogged() //Poolrooms ADDITION
		.hardness(0.0)
		.resistance(0.0)
		.box(2, 0, 2, 14, 6, 14)

	event.create('red_tape')
		.material("wool")
		.soundType("wool")
		.renderType("translucent")
		.fullBlock(false)
		.box(0, 0, 0, 16, 1, 16)
		.hardness(0.0)
		.resistance(0.0)
		.noCollision()
		.item(item =>
			item.modelJson({
				parent: 'minecraft:item/generated',
				textures: {
					layer0: `kubejs:item/red_tape_roll`,
				},
			})
		)
		.placementState(c => {
			c.set(BlockProperties.FACING, c.nearestLookingDirection.opposite)}
		)
		.blockstateJson = {
		"variants": {
			"facing=up": {
				"model": `kubejs:block/red_tape_north`,
			},
			"facing=down": {
				"model": `kubejs:block/red_tape_north`,
			},
			"facing=north": {
				"model": `kubejs:block/red_tape_north`,
			},
			"facing=east": {
				"model": `kubejs:block/red_tape_east`,
			},
			"facing=south": {
				"model": `kubejs:block/red_tape_north`,
			},
			"facing=west": {
				"model": `kubejs:block/red_tape_east`,
			},
		}
	}
	
	event.create("power_house")
		.fullBlock(false)
		.material("lantern")
		.soundType("lantern")
		.renderType("translucent")
		.opaque(false)
		.property(BlockProperties.FACING)
		.placementState(c => {
			c.set(BlockProperties.FACING, c.nearestLookingDirection.opposite)}
		)
		.blockstateJson = {
		"variants": {
			"facing=up": {
				"model": `kubejs:block/power_house`,
				"y": 0
			},
			"facing=down": {
				"model": `kubejs:block/power_house`,
				"y": 0
			},
			"facing=north": {
				"model": `kubejs:block/power_house`,
				"y": 0
			},
			"facing=east": {
				"model": `kubejs:block/power_house`,
				"y": 90
			},
			"facing=south": {
				"model": `kubejs:block/power_house`,
				"y": 180
			},
			"facing=west": {
				"model": `kubejs:block/power_house`,
				"y": 270
			},
		}
	}

	//Traffic Poles
	let traffic_poles = (id, name) => {
		event.create(id).displayName(name)
			.fullBlock(true)
			.material("lantern")
			.soundType("lantern")
			.renderType("cutout")
			.fullBlock(false)
			.opaque(false)
			.hardness(1.0)
			.requiresTool(true)
			.waterlogged() //Poolrooms ADDITION
			.tagBlock('minecraft:mineable/pickaxe')
			.item(item =>
				item.modelJson({
					parent: 'minecraft:item/generated',
					textures: {
						layer0: `kubejs:block/${id}`,
					},
				})
			)
			.box(6, 0, 6, 10, 16, 10)
			.property(BlockProperties.FACING)
			.placementState(c => {
				c.set(BlockProperties.FACING, c.nearestLookingDirection.opposite)
			}
			)
			.blockstateJson = {
			"variants": {
				"facing=up": {
					"model": `kubejs:block/${id}`,
					"y": 0
				},
				"facing=down": {
					"model": `kubejs:block/${id}`,
					"y": 0
				},
				"facing=north": {
					"model": `kubejs:block/${id}`,
					"y": 0
				},
				"facing=east": {
					"model": `kubejs:block/${id}`,
					"y": 90
				},
				"facing=south": {
					"model": `kubejs:block/${id}`,
					"y": 180
				},
				"facing=west": {
					"model": `kubejs:block/${id}`,
					"y": 270
				},
			}
		}
	}

	traffic_poles('traffic_pole', 'sign')
	traffic_poles('arrow1_sign', 'sign')
	traffic_poles('arrow2_sign', 'sign')
	traffic_poles('liminal_warning', 'sign')
	traffic_poles('liminal_warning2', 'sign')
	traffic_poles('box_sign', 'sign')
	traffic_poles('infinity_sign', 'sign')
	traffic_poles('skull_sign', 'sign')
	traffic_poles('stop_sign', 'sign')
	traffic_poles('explantion1_sign', 'sign')
	traffic_poles('explantion2_sign', 'sign')
	traffic_poles('unknown1', 'sign')
	traffic_poles('cross_sign', 'sign')
	traffic_poles('exit_sign', 'sign')
	traffic_poles('exit_sign2', 'sign')
	traffic_poles('left_arrow_sign', 'sign')
	traffic_poles('right_arrow_sign', 'sign')
	traffic_poles('nowhere_sign', 'sign')
	traffic_poles('monolith_sign', 'sign')
	traffic_poles('witahdigroi_sign', 'sign')
	traffic_poles('tripple_sign', 'sign')
	traffic_poles('turn_back_sign', 'sign')
	traffic_poles('inkblod_sign', 'sign')



	//sculk
	event.create('porous_stone')
		.material("stone")
		.soundType("tuff")
		.unbreakable()
		.mapColor("wood")
	event.create('sculk_carapace')
		.material("sculk")
		.soundType("sculk_catalyst")
		.hardness(10000)
		.resistance(6)//apparently this is intended to only be able to be broken by tnt... wish that was conveyed. Anyways it shouldnt be 0
		.noDrops()
		.tagBlock('minecraft:mineable/pickaxe')
		.mapColor("color_black")
	event.create('sculk_slab', 'slab')
		.material("sculk")
		.soundType("sculk")
		.unbreakable()
		.fullBlock(false)
		.opaque(false)
		.mapColor("color_black")
	event.create('sculk_stairs', 'stairs')
		.material("sculk")
		.soundType("sculk")
		.unbreakable()
		.fullBlock(false)
		.opaque(false)
		.mapColor("color_black")
	event.create('sculk_tendrils')
		.material("sculk")
		.soundType("sculk_vein")
		.waterlogged()
		.renderType("cutout")
		.fullBlock(false)
		.noCollision()
		.opaque(false)
		.tagBlock('minecraft:mineable/hoe')
	event.create('sculk_shroom')
		.material("sculk")
		.soundType("sculk_vein")
		.waterlogged()
		.renderType("cutout")
		.fullBlock(false)
		.noCollision()
		.opaque(false)
		.tagBlock('minecraft:mineable/hoe')

	//Tier 2
	event.create('light_engineering_empty').displayName('Light Engineering Frame')
		.material('lantern').hardness(1.5)
		.soundType("lantern")
		.tagBlock('minecraft:mineable/pickaxe')
		.mapColor("metal")
		.renderType("cutout")
		.box(0, 0, 0, 3, 3, 16)
		.box(13, 0, 0, 16, 3, 16)
		.box(0, 13, 0, 3, 16, 16)
		.box(13, 13, 0, 16, 16, 16)
		.box(0, 3, 0, 3, 13, 3)
		.box(0, 3, 13, 3, 13, 16)
		.box(13, 3, 13, 16, 13, 16)
		.box(13, 3, 0, 16, 13, 3)
		.box(3, 13, 0, 13, 16, 3)
		.box(3, 0, 0, 13, 3, 3)
		.box(3, 0, 13, 13, 3, 16)
		.box(3, 13, 13, 13, 16, 16)

	event.create('heavy_engineering_empty').displayName('Heavy Engineering Frame')
		.material('lantern').hardness(1.5)
		.soundType("lantern")
		.tagBlock('minecraft:mineable/pickaxe')
		.mapColor("metal")
		.renderType("cutout")
		.box(0, 0, 0, 3, 3, 16)
		.box(13, 0, 0, 16, 3, 16)
		.box(0, 13, 0, 3, 16, 16)
		.box(13, 13, 0, 16, 16, 16)
		.box(0, 3, 0, 3, 13, 3)
		.box(0, 3, 13, 3, 13, 16)
		.box(13, 3, 13, 16, 13, 16)
		.box(13, 3, 0, 16, 13, 3)
		.box(3, 13, 0, 13, 16, 3)
		.box(3, 0, 0, 13, 3, 3)
		.box(3, 0, 13, 13, 3, 16)
		.box(3, 13, 13, 13, 16, 16)

	event.create('half_frame_bottom').displayName('Bottom of a Machine Frame')
		.material('lantern').hardness(1.5)
		.tagBlock('minecraft:mineable/pickaxe')
		.soundType("lantern")
		.mapColor("metal")
		.box(11, 5, 11, 16, 8, 16, true)
		.box(0, 5, 11, 5, 8, 16, true)
		.box(11, 5, 0, 16, 8, 5, true)
		.box(0, 5, 0, 5, 8, 5, true)
		.box(5, 0, 11, 11, 5, 16, true)
		.box(5, 0, 0, 11, 5, 5, true)
		.box(11, 0, 0, 16, 5, 16, true)
		.box(0, 0, 0, 5, 5, 16, true)

	event.create('half_frame_top').displayName('Top of a Machine Frame')
		.material('lantern').hardness(1.5)
		.tagBlock('minecraft:mineable/pickaxe')
		.soundType("lantern")
		.mapColor("metal")
		.box(11, 0, 0, 16, 5, 5, true)
		.box(0, 0, 0, 5, 5, 5, true)
		.box(11, 0, 11, 16, 5, 16, true)
		.box(0, 0, 11, 5, 5, 16, true)
		.box(5, 5, 0, 11, 10, 5, true)
		.box(5, 5, 11, 11, 10, 16, true)
		.box(11, 5, 0, 16, 10, 16, true)
		.box(0, 5, 0, 5, 10, 16, true)

	//Tier3
	event.create('sculk_scrubber')
		.fullBlock(true)
		.material("stone")
		.soundType("lantern")
		.tagBlock('minecraft:mineable/pickaxe')
		.mapColor("metal")
	event.create('sculked_sculk_scrubber')
		.fullBlock(true)
		.material("stone")
		.soundType("lantern")
		.tagBlock('minecraft:mineable/pickaxe')
		.mapColor("metal")
	
	//Tier4
	event.create('wall_destroyer').displayName('Wall Piercer')
		.fullBlock(true)
		.material("stone")
		.soundType("lantern")
		.tagBlock('minecraft:mineable/pickaxe')
		.mapColor("metal")
		.property(BlockProperties.FACING)
		.placementState(c => {
			c.set(BlockProperties.FACING, c.nearestLookingDirection.opposite)
		}
		)
		.blockstateJson = {
		"variants": {
			"facing=up": {
				"model": `kubejs:block/wall_destroyer`,
				"x": 180
			},
			"facing=down": {
				"model": `kubejs:block/wall_destroyer`,
				"x": 0
			},
			"facing=north": {
				"model": `kubejs:block/wall_destroyer`,
				"x": 90,
				"y": 180
			},
			"facing=east": {
				"model": `kubejs:block/wall_destroyer`,
				"x": 90,
				"y": 270
			},
			"facing=south": {
				"model": `kubejs:block/wall_destroyer`,
				"x": 90,
				"y": 0
			},
			"facing=west": {
				"model": `kubejs:block/wall_destroyer`,
				"x": 90,
				"y": 90
			},
		}
	}

	event.create('reality_frame')
		.fullBlock(true)
		.material("stone")
		.soundType("netherite_block")
		.tagBlock('minecraft:mineable/pickaxe')
		.mapColor("metal")
	event.create('reality_charge')
		.fullBlock(true)
		.material("stone")
		.soundType("netherite_block")
		.lightLevel(1.0)
		.tagBlock('minecraft:mineable/pickaxe')
		.mapColor("metal")
	event.create('reality_charge_empty').displayName('Empty Reality Charge')
		.fullBlock(true)
		.material("stone")
		.soundType("netherite_block")
		.tagBlock('minecraft:mineable/pickaxe')
		.mapColor("metal")
	event.create('reality_controller')
		.fullBlock(true)
		.material("netherite_block")
		.soundType("netherite_block")
		.tagBlock('minecraft:mineable/pickaxe')
		.mapColor("metal")
		.property(BlockProperties.FACING)
		.placementState(c => {
			c.set(BlockProperties.FACING, c.nearestLookingDirection.opposite)
		}
		)
		.blockstateJson = {
		"variants": {
			"facing=up": {
				"model": `kubejs:block/reality_controller`,
				"y": 0
			},
			"facing=down": {
				"model": `kubejs:block/reality_controller`,
				"y": 0
			},
			"facing=north": {
				"model": `kubejs:block/reality_controller`,
				"y": 0
			},
			"facing=east": {
				"model": `kubejs:block/reality_controller`,
				"y": 90
			},
			"facing=south": {
				"model": `kubejs:block/reality_controller`,
				"y": 180
			},
			"facing=west": {
				"model": `kubejs:block/reality_controller`,
				"y": 270
			},
		}
	}
	event.create('reality_controller_running').displayName('Reality Controller')
		.fullBlock(true)
		.material("netherite_block")
		.soundType("netherite_block")
		.tagBlock('minecraft:mineable/pickaxe')
		.mapColor("metal")
		.property(BlockProperties.FACING)
		.placementState(c => {
			c.set(BlockProperties.FACING, c.nearestLookingDirection.opposite)
		}
		)
		.blockstateJson = {
		"variants": {
			"facing=up": {
				"model": `kubejs:block/reality_controller_running`,
				"y": 0
			},
			"facing=down": {
				"model": `kubejs:block/reality_controller_running`,
				"y": 0
			},
			"facing=north": {
				"model": `kubejs:block/reality_controller_running`,
				"y": 0
			},
			"facing=east": {
				"model": `kubejs:block/reality_controller_running`,
				"y": 90
			},
			"facing=south": {
				"model": `kubejs:block/reality_controller_running`,
				"y": 180
			},
			"facing=west": {
				"model": `kubejs:block/reality_controller_running`,
				"y": 270
			},
		}
	}

	event.create('lost_eye').displayName('Lost Eye')
		.fullBlock(true)
		.material("stone")
		.soundType("shroomlight")
		.box(4, 0, 4, 12, 8, 12)
		.item(item =>
			item.modelJson({
				parent: 'minecraft:item/generated',
				textures: {
					layer0: `endrem:item/lost_eye`,
				},
			})
		)
	event.create('exotic_eye').displayName('Exotic Eye')
		.fullBlock(false)
		.material("stone")
		.soundType("shroomlight")
		.box (4, 0, 4, 12, 8, 12)
		.renderType("cutout")
		.opaque(false)
		.item(item => 
			item.modelJson({
			  parent: 'minecraft:item/generated',
			  textures: {
				layer0: `endrem:item/exotic_eye`,
			  },
			})
		)

	event.create('hyper_experience_block').displayName('Block of Living Experience')
		.fullBlock(true)
		.material("amethyst")
		.soundType("amethyst")
		.tagBlock('minecraft:mineable/pickaxe')
		.tagBlock('minecraft:beacon_base_blocks')
		.mapColor("diamond")

})

StartupEvents.registry('item', event => {

	event.create('incomplete_component_electronic').displayName('Incomplete Electronic Component')
	event.create('incomplete_component_electronic_adv').displayName('Incomplete Advanced Electronic Component')
	event.create('crowbar').maxDamage(8)
	event.create('putty_knife')
	event.create('diamond_brush').tag('kubejs:brushers').maxDamage(320)
	event.create('wallpaper').tag('kubejs:cut_wallpaper')
	event.create('wallpaper_white').displayName('White Wallpaper').tag('kubejs:cut_wallpaper')
	event.create('wallpaper_pink').displayName('Pink Wallpaper').tag('kubejs:cut_wallpaper')
	event.create('cut_carpet').tag('kubejs:cut_carpet')
	event.create('cut_carpet_red').displayName('Cut Red Carpet').tag('kubejs:cut_carpet')
	event.create('cut_carpet_green').displayName('Cut Green Carpet').tag('kubejs:cut_carpet')
	event.create('carpet_dust')
	event.create('asbestos_dust')
	event.create('scrap').displayName('Metal Scrap')
	event.create('concrete_piece').displayName('Concrete Chunk')
	event.create('cobblestone_bucket').displayName('Bucket of Packed Cobblestone')
	event.create('heated_concrete')
	event.create('concrete_brick')
	event.create('cracked_steel')
	event.create('hot_steel')
	event.create('pool_tile')
	event.create('pool_tile_golden').displayName('Gold Pool Tile')
	event.create('battery')
	event.create('empty_fuse')
	event.create('soul_fuse')
	event.create('fluorescent_tube')
	event.create('reality_alloy')
	event.create('moderate_soul_gem').rarity('rare')
	event.create('sculk_clump').rarity('rare')
	event.create('overclocked_clock').rarity('rare')
	event.create('ai').displayName('Artificial Intelligence').rarity('rare')
	event.create('quantum_string').rarity('epic')
	event.create('error_item').displayName('Error')
	event.create('sentimental_thaumium').rarity('epic')
	event.create('sentimental_ash_alloy').rarity('epic')
	event.create('party_popper')
	//acension
	event.create('pale_cod').food(food => { food.hunger(2).saturation(0.2).effect('wither', 100, 0, 0.8) }).tag('forge:raw_fishes/cod')
	event.create('pale_salmon').food(food => { food.hunger(2).saturation(0.3).effect('wither', 200, 0, 0.2) }).tag('forge:raw_fishes/salmon')
	event.create('cooked_pale_cod').food(food => { food.hunger(4).saturation(0.6) })
	event.create('cooked_pale_salmon').food(food => { food.hunger(5).saturation(0.8) })
	event.create('pale_squid').food(food => { food.hunger(3).saturation(0.3).effect('nausea', 200, 0, 1) }).tag('forge:squid')

	event.create('reality_storage_empty').displayName('Empty Reality Storage Cell')
	event.create('reality_storage_cell1').displayName('Reality Storage Cell')

	event.create('data_chip_blank').displayName('Blank Data Chip').tag('kubejs:inscribable_data_chip')
	event.create('data_chip1').displayName('Data Chip').tag('kubejs:inscribable_data_chip').tag('kubejs:basic_data_chip')
	event.create('data_chip2').displayName('Data Chip').tag('kubejs:inscribable_data_chip').tag('kubejs:basic_data_chip')
	event.create('data_chip3').displayName('Data Chip').tag('kubejs:inscribable_data_chip').tag('kubejs:basic_data_chip')
	event.create('data_chip4').displayName('Data Chip').tag('kubejs:inscribable_data_chip').tag('kubejs:basic_data_chip')
	event.create('data_chip5').displayName('Data Chip').tag('kubejs:inscribable_data_chip').tag('kubejs:basic_data_chip')
	event.create('data_chip6').displayName('Data Chip').tag('kubejs:inscribable_data_chip').tag('kubejs:basic_data_chip')
	event.create('data_chip7').displayName('Data Chip').tag('kubejs:inscribable_data_chip').tag('kubejs:basic_data_chip')
	event.create('data_chip8').displayName('Data Chip').tag('kubejs:inscribable_data_chip').tag('kubejs:basic_data_chip')
	event.create('data_chip9').displayName('Data Chip').tag('kubejs:inscribable_data_chip').tag('kubejs:basic_data_chip')
	event.create('data_chip10').displayName('Data Chip').tag('kubejs:inscribable_data_chip').tag('kubejs:basic_data_chip')
	event.create('data_chip11').displayName('Data Chip').tag('kubejs:inscribable_data_chip').tag('kubejs:basic_data_chip')
	event.create('data_chip12').displayName('Data Chip').tag('kubejs:inscribable_data_chip').tag('kubejs:basic_data_chip')
	event.create('data_chip13').displayName('Data Chip').tag('kubejs:inscribable_data_chip').tag('kubejs:basic_data_chip')
	event.create('data_chip14').displayName('Data Chip').tag('kubejs:inscribable_data_chip').tag('kubejs:basic_data_chip')
	event.create('data_chip15').displayName('Data Chip').tag('kubejs:inscribable_data_chip').tag('kubejs:basic_data_chip')
	event.create('data_chip_infinity').displayName('Modified Data Chip').rarity('rare')
	event.create('data_chip_error').displayName('Corrupted Data Chip').tag('kubejs:corrupted_data_chip')
	event.create('data_chip_infinity_error').displayName('Corrupted Modified Data Chip').rarity('rare').tag('kubejs:corrupted_data_chip')

})

StartupEvents.registry('fluid', event => {
	event.create('liquid_time')
		.displayName('The Flow of Time')
		.stillTexture('kubejs:block/liquid_time_flow')
		.flowingTexture('kubejs:block/liquid_time_flow')
		.bucketColor(0xFFFFFF)
		.noBlock()

	event.create('ball_pit')
		.stillTexture('kubejs:block/ball_pit_still')
		.flowingTexture('kubejs:block/ball_pit_flow')
    	.density(4000)
    	.viscosity(6000)
})