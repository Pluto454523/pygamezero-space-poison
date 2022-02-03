import pgzrun,time
from random import randint,choice

def draw():
    global bullet_state
    global enemy_fire_state1,enemy_fire_state2,enemy_fire_state3
    global enemy_state1,enemy_state2,enemy_state3,enemy_state4,enemy_state5
    global lifes,state,score
    
    if state == 'READY':
        scene.draw()
        
    elif state == 'START':
        scene.draw()
    
    elif state == 'WIN':
        scene.draw()
      
    elif state == 'GAME_OVER':
        scene.draw()
        
    elif state == 'STORY' :
        scene.draw()
        screen.draw.text('PRESS LEFT \nTO BACK PAGE',fontsize = 25, gcolor = 'orange' , center = (100, HEIGHT-20))
        screen.draw.text(str(sceneCount+1) + '/4',fontsize = 25, gcolor = 'orange' , center = (WIDTH/2, HEIGHT-20))
        screen.draw.text('PRESS RIGHT \nTO NEXT PAGE',fontsize = 25, gcolor = 'orange' , center = (WIDTH-100, HEIGHT-20))
       
    elif state == 'CREDIT' :
        scene.draw()
         
    elif state == 'PLAY':
        bg1.draw()
        bg2.draw() 
        showHealth() #แสดงหลอดเลือด
        screen.draw.text('SCORE : ' + str(score),(50,50),fontsize = 20 , color = 'white')        
        space.draw() 
        
        #enemy fire
        if score == 10:
            enemy_fire_state1 = "fire"
        if score == 30:
            enemy_fire_state2 = "fire"
        if score == 40:
            enemy_fire_state3 = "fire"
            
        if bullet_state == "fire":
            bullet.draw()
        
        if enemy_fire_state1 == "fire":
            bullet1.draw()
        
        if enemy_fire_state2 == "fire":
            bullet2.draw()
        
        if enemy_fire_state3 == "fire":
            bullet3.draw()
              
        enemy1.draw()
        enemy2.draw()
        enemy3.draw()
        enemy4.draw()
        enemy5.draw()
        
        if enemy_state1 == "dead":
            bomb1.draw()
            bomb1.x = enemy1.x
            bomb1.y = enemy1.y
            enemy_state1 = "alive"
        if enemy_state2 == "dead":

            bomb2.draw()
            bomb2.x = enemy2.x
            bomb2.y = enemy2.y
            enemy_state2 = "alive"
        if enemy_state3 == "dead":
            bomb3.draw()
            bomb3.x = enemy3.x
            bomb3.y = enemy3.y
            enemy_state3 = "alive"
        if enemy_state4 == "dead":
            bomb4.draw()
            bomb4.x = enemy4.x
            bomb4.y = enemy4.y
            enemy_state4 = "alive"
        if enemy_state5 == "dead":
            bomb5.draw()
            bomb5.x = enemy5.x
            bomb5.y = enemy5.y
            enemy_state5 = "alive"
        
    elif state == 'EXIT':
        scene.draw()
        screen.draw.text('PRESS ENTER',fontsize = 50, gcolor = 'purple' , center = (WIDTH/2, HEIGHT/2+70))
        screen.draw.text('TO BACK TO MAIN MENU',fontsize = 30, gcolor = 'purple' , center = (WIDTH/2, HEIGHT/2+100))
        
def update():
    global pos,bullet_state,score,state,lifes
    global enemy_fire_state1,enemy_fire_state2,enemy_fire_state3
    global enemy_state1,enemy_state2,enemy_state3,enemy_state4,enemy_state5
    
    if state == 'PLAY':
        
        #สำหรับควบคุมยานของเรา
        controlShip()
        
        #animation enemy
        enemy1.y += 2
        enemy2.y += 2
        enemy3.y += 2
        enemy4.y += 2
        enemy5.y += 2
        
        #animation bomb
        bomb1.y += 2
        bomb2.y += 2
        bomb3.y += 2
        bomb4.y += 2
        bomb5.y += 2
        
        # เช็ค bullet ว่ายิงหมดเฟรมหรือยัง
        # ถ้าหมดแล้วไห้ปรับ bullet_state ไห้สามายิงกระสุนออกได้
        # แล้วก็ปรับ y กระสุนไห้ออกจากเฟรมไปอยู่ที่ y = 600
        if bullet.y <= 0:
            bullet.y = 600
            bullet_state = "ready"
               
        #ยิงกระสุนชนกับยานศัตรูแล้วยานศัตรูตายแล้วเพิ่มคะแนน
        if bullet_state == "fire":
            bullet.y -= 10
            if enemy1.colliderect(bullet):
                bullet_state = "ready"
                enemy_state1 = "dead"
                sounds.bomb.play()
                score += 1
                bomb1.x = enemy1.x
                bomb1.y = enemy1.y
                enemy1.x = randint(100,WIDTH - 100)
                enemy1.y = -100
            elif enemy2.colliderect(bullet):
                bullet_state = "ready"
                enemy_state2 = "dead"
                sounds.bomb.play()
                score += 1
                bomb2.x = enemy2.x
                bomb2.y = enemy2.y
                enemy2.x = randint(100,WIDTH - 100)
                enemy2.y = -100
            elif enemy3.colliderect(bullet):
                bullet_state = "ready"
                enemy_state3 = "dead"
                sounds.bomb.play()
                score += 1
                bomb3.x = enemy3.x
                bomb3.y = enemy3.y
                enemy3.x = randint(100,WIDTH - 100)
                enemy3.y = -100
            elif enemy4.colliderect(bullet):
                bullet_state = "ready"
                enemy_state4 = "dead"
                sounds.bomb.play()
                score += 1
                bomb4.x = enemy4.x
                bomb4.y = enemy4.y
                enemy4.x = randint(100,WIDTH - 100)
                enemy4.y = -100
            elif enemy5.colliderect(bullet):
                bullet_state = "ready"
                enemy_state5 = "dead"
                sounds.bomb.play()
                score += 1
                bomb5.x = enemy5.x
                bomb5.y = enemy5.y
                enemy5.x = randint(100,WIDTH - 100)
                enemy5.y = -100
            
        #กระสุนโดนกับยานเราแล้วเลือดลด
        if bullet1.colliderect(space):
            sounds.hit.play()
            bullet1.x = enemy1.x
            bullet1.y = enemy1.y + 50
            lifes -= 20           
        elif bullet2.colliderect(space):
            sounds.hit.play()
            bullet2.x = enemy2.x
            bullet2.y = enemy2.y + 50
            lifes -= 20
        elif bullet3.colliderect(space):
            sounds.hit.play()
            bullet3.x = enemy3.x
            bullet3.y = enemy3.y + 50
            lifes -= 20

        #ยานชนกับยานศัตรูแล้วเลือดลด       
        if space.colliderect(enemy1):
            lifes -= 20
            sounds.hit.play()
            enemy1.x = randint(100,WIDTH - 100)
            enemy1.y = -100
            bomb1.x = enemy1.x
            bomb1.y = enemy1.y
        elif space.colliderect(enemy2):
            lifes -= 20
            sounds.hit.play()
            enemy2.x = randint(100,WIDTH - 100)
            enemy2.y = -100
            bomb2.x = enemy2.x
            bomb2.y = enemy2.y
        elif space.colliderect(enemy3):
            lifes -= 20
            sounds.hit.play()
            enemy3.x = randint(100,WIDTH - 100)
            enemy3.y = -100
            bomb3.x = enemy3.x
            bomb3.y = enemy3.y
        elif space.colliderect(enemy4):
            lifes -= 20
            sounds.hit.play()
            enemy4.x = randint(100,WIDTH - 100)
            enemy4.y = -100
            bomb4.x = enemy4.x
            bomb4.y = enemy4.y
        elif space.colliderect(enemy5):
            lifes -= 20
            sounds.hit.play()
            enemy5.x = randint(100,WIDTH - 100)
            enemy5.y = -100
            bomb5.x = enemy5.x
            bomb5.y = enemy5.y
        
        # เมื่อ enemy_fire_state = fire กระสุนจะขยับไปเลื่อยๆ
        if enemy_fire_state1 == "fire":
            bullet1.y += 4
        if enemy_fire_state2 == "fire":
            bullet2.y += 4
        if enemy_fire_state3 == "fire":
            bullet3.y += 4

        # ปรับกระสุน enemy ไห้ออกจากตัวยาน
        if bullet1.y > HEIGHT:
            bullet1.x = enemy1.x
            bullet1.y = enemy1.y 
        if bullet2.y > HEIGHT:
            bullet2.x = enemy2.x
            bullet2.y = enemy2.y 
        if bullet3.y > HEIGHT:
            bullet3.x = enemy3.x
            bullet3.y = enemy3.y
          
        # ปรับยาน enemy ไห้กลับไปข้างบนเมื่อหลุดขอบไป
        if enemy1.y > HEIGHT:
            enemy1.x = randint(100,HEIGHT - 100)
            enemy1.y = -100
            bomb1.x = enemy1.x
            bomb1.y = enemy1.y
        if enemy2.y > HEIGHT:
            enemy2.x = randint(100,HEIGHT - 100)
            enemy2.y = -100
            bomb2.x = enemy2.x
            bomb2.y = enemy2.y
        if enemy3.y > HEIGHT:
            enemy3.x = randint(100,HEIGHT - 100)
            enemy3.y = -100
            bomb3.x = enemy3.x
            bomb3.y = enemy3.y
        if enemy4.y > HEIGHT:
            enemy4.x = randint(100,HEIGHT - 100)
            enemy4.y = -100
            bomb4.x = enemy4.x
            bomb4.y = enemy4.y
        if enemy5.y > HEIGHT:
            enemy5.x = randint(100,HEIGHT - 100)
            enemy5.y = -100
            bomb5.x = enemy5.x
            bomb5.y = enemy5.y
            
        #ปรับความเร็ว play background ตามคะแนน
        if score >= 10:
            scoll_speed = 1.5
        elif score >= 25:
            scoll_speed = 2
        elif score >= 40:
            scoll_speed = 3
        else:
            scoll_speed = 1
        
        #คะแนนมากกว่า 50 ปรับ state เป็น win แล้วรีเซ็ตเลือดและคะแนน
        if score >= 50:
            state = 'WIN'
            lifes = 100
            score = 0
        
        #animation play background 
        scoll_speed = 1
        bg1.y += scoll_speed
        bg2.y += scoll_speed
        if bg1.y > 2099:
            bg1.y = -700
        if bg2.y > 2099:
            bg2.y = -700

        #เลือดน้อยกว่า 0 ปรับ state เป็น game_over แล้วรีเซ็ตเลือดและคะแนน
        if lifes == 0:
            state = 'GAME_OVER'
            lifes = 100
            score = 0
            
def on_mouse_down(button,pos):
    if state == 'PLAY':
        if bullet_state == "ready": 
            if (button == mouse.LEFT):
                fire_bullet()

def on_key_down(key,mod,unicode):
    
    global state,sceneCount,score,lifes

    if (key == keys.RETURN) :
        if (state == 'READY' or state == 'CREDIT') :
            sounds.sao2.play()
            music.stop()
            music.play_once('bgmusic')
            state = 'PLAY'
            sceneCount = 0
            score = 0
            lifes = 100
        elif (state == 'EXIT'):
            music.stop()
            sounds.gameover.stop()
            sceneCount = 1
            state = 'READY'
        
    elif (key == keys.C):
        if (state == 'READY') :
            music.stop()
            sounds.sao2.play()
            state = 'CREDIT'
        
    elif (key == keys.R):
        if (state == 'READY') :
            music.stop()
            sounds.sao2.play()
            state = 'STORY'
       
    elif (key == keys.ESCAPE) :
        if (state == 'PLAY') :
            music.stop()
            sceneCount = 1
            state = 'READY'  
            
        elif (state == 'CREDIT') :
            music.stop()
            sceneCount = 1
            state = 'READY'
            
        elif (state == 'STORY') :
            music.stop()
            sceneCount = 1
            state = 'READY'
            
        elif (state != 'EXIT'):
            music.stop()
            sounds.gameover.play()
            state = 'EXIT'
            
    elif (key == keys.RIGHT):
        if (state == 'STORY'):
            if sceneCount < 3:
                music.stop()
                sounds.sao2.play()
                sceneCount += 1
            
    elif (key == keys.LEFT):
        if (state == 'STORY'):
            if sceneCount > 0:
                music.stop()
                sounds.sao2.play()
                sceneCount -= 1
      
def controlShip():
    space.image = space_images[randomSpaceShip]
    if space.y >= 35:
        if (keyboard.W):
            space.y -= 6
            space.image = nitro_images[randomSpaceShip]
    if space.x >= 35:
        if (keyboard.A):
            space.x -= 6
            space.image = nitro_images[randomSpaceShip]
    if space.y <= 650:
        if (keyboard.S):
            space.y += 6
            space.image = nitro_images[randomSpaceShip]
    if space.x <= 650:
        if (keyboard.D):
            space.x += 6
            space.image = nitro_images[randomSpaceShip]
    
def fire_bullet():
    global bullet_state
    sounds.shootlaser.play()
    bullet_state = "fire"
    bullet.x = space.x
    bullet.y = space.y

def showHealth():
    global lifes
    screen.draw.filled_rect(Rect((0, 680),(310 ,30)), (0,0,0) )
    screen.draw.filled_rect(Rect((5, 685),(300 ,10)), (255,255,255) )
    screen.draw.filled_rect(Rect((5, 685),(3*lifes ,10)), (255,31,23) )

def play_scene():
    global sceneCount,state

    if state == 'READY':
        if sceneCount == 1:
            music.play_once('menu')
            scene.image = 'menu'
            sceneCount = 0
    
    if state == 'START':
        if sceneCount < 33:
            scene_name = 'scene_(' + str(sceneCount+1) + ')'
            sence_images.append(scene_name)
            scene.image = sence_images[sceneCount]
            sceneCount += 1
        else:
            time.sleep(2)
            sence_images.clear()
            sceneCount = 1
            state = 'READY'
    
    if state == 'WIN':
        if sceneCount < 74:
            scene_name = 'win_(' + str(sceneCount+1) + ')'
            sence_images.append(scene_name)
            scene.image = sence_images[sceneCount]
            sceneCount += 1
        else:
            time.sleep(2)
            sence_images.clear()
            sceneCount = 1
            state = 'READY'
     
    if state == 'EXIT':
        scene.image = 'goodbye'
        sence_images.clear()
        
    if state == 'CREDIT':
        scene.image = 'present_by'
        sence_images.clear()
    
    if state == 'GAME_OVER':
        if sceneCount < 48:
            scene_name = 'game_over_(' + str(sceneCount+1) + ')'
            sence_images.append(scene_name)
            scene.image = sence_images[sceneCount]
            sceneCount += 1
        else:
            time.sleep(2)
            sence_images.clear()
            sceneCount = 1
            state = 'READY'

    if state == 'STORY':
        if sceneCount < 4:
            scene_name = 'story_(' + str(sceneCount+1) + ')'
            scene.image = scene_name
      
#main pogram
WIDTH = 700
HEIGHT = 700
state = 'START'
score = 0
lifes = 100

# play space background
bg1 = Actor("space_bg1", (350,700))
bg2 = Actor("space_bg2", (350,-700))

#scene
sence_images = []
scene = Actor('scene_(1)')
sceneCount = 0
clock.schedule_interval(play_scene,0.3)
music.play_once('scene')

bullet_state = "ready"
enemy_fire_state1 = "ready"
enemy_fire_state2 = "ready"
enemy_fire_state3 = "ready"

enemy_state1 = "alive"
enemy_state2 = "alive"
enemy_state3 = "alive"
enemy_state4 = "alive"
enemy_state5 = "alive"

enemy1 = Actor('dark1', (120,-100))
enemy2 = Actor('dark1', (230,-100))
enemy3 = Actor('dark1', (340,-100))
enemy4 = Actor('dark1', (455,-100))
enemy5 = Actor('dark1', (585,-100))

#ship
space_images = ['space1','space2','space3','space4','space5']
nitro_images = ['space1_nitro','space2_nitro','space3_nitro','space4_nitro','space5_nitro']
randomSpaceShip = randint(0,4) #Random Space Ship
space = Actor(space_images[randomSpaceShip],(WIDTH/2,HEIGHT-100))

#bullet
bullet = Actor('our_ammo')
bullet.x = space.x
bullet.y = space.y

bullet1 = Actor('enemy_ammo')
bullet1.x = enemy1.x
bullet1.y = enemy1.y + 50

bullet2 = Actor('enemy_ammo')
bullet2.x = enemy2.x
bullet2.y = enemy2.y + 50

bullet3 = Actor('enemy_ammo')
bullet3.x = enemy3.x
bullet3.y = enemy3.y + 50

# bomb
bomb1 = Actor('bomb')
bomb1.x = enemy1.x
bomb1.y = enemy1.y

bomb2 = Actor('bomb')
bomb2.x = enemy2.x
bomb2.y = enemy2.y

bomb3 = Actor('bomb')
bomb3.x = enemy3.x
bomb3.y = enemy3.y

bomb4 = Actor('bomb')
bomb4.x = enemy4.x
bomb4.y = enemy4.y

bomb5 = Actor('bomb')
bomb5.x = enemy5.x
bomb5.y = enemy5.y

pgzrun.go()
