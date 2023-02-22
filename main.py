def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    2 2 2 2 . 2 2 2 2 . 2 2 2 2 . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        spacePlane,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_countdown_end():
    game.game_over(True)
info.on_countdown_end(on_countdown_end)

def on_on_overlap(sprite2, otherSprite2):
    otherSprite2.destroy()
    scene.camera_shake(4, 500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy(effects.fire, 500)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

bogey: Sprite = None
projectile: Sprite = None
spacePlane: Sprite = None
info.start_countdown(60)
spacePlane = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . 3 3 3 3 3 3 3 3 . . . . 
            . . . 3 d 3 3 3 3 3 3 c 3 . . . 
            . . 3 c d 3 3 3 3 3 3 c c 3 . . 
            . 3 c c d d d d d d 3 c c d 3 d 
            . 3 c 3 a a a a a a a b c d 3 3 
            . 3 3 a b b a b b b a a b d 3 3 
            . 3 a b b b a b b b b a 3 3 3 3 
            . a a 3 3 3 a 3 3 3 3 3 a 3 3 3 
            . a a a a a a f a a a f a 3 d d 
            . a a a a a a f a a f a a a 3 d 
            . a a a a a a f f f a a a a a a 
            . a f f f f a a a a f f f a a a 
            . . f f f f f a a f f f f f a . 
            . . . f f f . . . . f f f f . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(spacePlane, 200, 200)
spacePlane.set_stay_in_screen(True)
info.set_life(5)
scene.background_image()

def on_update_interval():
    global bogey
    bogey = sprites.create(img("""
            . . . . . . . . . c c 8 . . . . 
                    . . . . . . 8 c c c f 8 c c . . 
                    . . . c c 8 8 f c a f f f c c . 
                    . . c c c f f f c a a f f c c c 
                    8 c c c f f f f c c a a c 8 c c 
                    c c c b f f f 8 a c c a a a c c 
                    c a a b b 8 a b c c c c c c c c 
                    a f c a a b b a c c c c c f f c 
                    a 8 f c a a c c a c a c f f f c 
                    c a 8 a a c c c c a a f f f 8 a 
                    . a c a a c f f a a b 8 f f c a 
                    . . c c b a f f f a b b c c 6 c 
                    . . . c b b a f f 6 6 a b 6 c . 
                    . . . c c b b b 6 6 a c c c c . 
                    . . . . c c a b b c c c . . . . 
                    . . . . . c c c c c c . . . . .
        """),
        SpriteKind.enemy)
    bogey.set_flag(SpriteFlag.AUTO_DESTROY, False)
    bogey.set_position(160, randint(5, 115))
    bogey.set_velocity(-100, 0)
game.on_update_interval(1000, on_update_interval)
