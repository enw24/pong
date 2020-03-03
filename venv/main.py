import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600)) #sets screen
pygame.display.set_caption('Pong')


gameExit=False
lead_x=790
lead_y=300
lead_y_change = 0
ai_x = 0
ai_y = 300
ai_y_change = 5

clock = pygame.time.Clock()
max_vector = 200
ball_vector = 45
ball_direction = 1
ball_h=400
ball_v=300
ballspeed = 10
first_bounce = 0
ball_fraction = 0
machine_y = 300
total_bounces = 0


while not gameExit:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                lead_y_change = -15
            if event.key == pygame.K_DOWN:
                lead_y_change = 15
            if event.key == pygame.K_SPACE:
                ball_vector = 45
                ball_direction = 1
                ball_h = 400
                ball_v = 300
        if event.type == pygame.KEYUP:
            lead_y_change = 0

    if ball_h == 0:
        if int(ball_v) in range(int(ai_y-25), int(ai_y+25)):
            ball_direction *= -1
            ball_h = 0

    if ball_h == 800:
        if int(ball_v) in range(lead_y, lead_y+50):
            ball_direction *= -1
            ball_vector = (-max_vector) + (ball_v-lead_y)*(max_vector/50)
            total_bounces = abs(ball_vector * 80 / 9 / 600)
            total_vert = ball_vector*80/9

        if ball_vector < 0:
            inital_fraction = ball_v / 600
        else:
            inital_fraction = (600 - ball_v) / 600

        if total_bounces <= inital_fraction:
            machine_y = ball_v + ball_vector * 80 / 9
        else:
            if int(total_bounces - inital_fraction + 1) == 2:  # if 2 bounces, then direction same
                direction = ball_vector / abs(ball_vector)
            else:
                direction = -1 * ball_vector / abs(ball_vector)
            if direction < 0:
                machine_y = 600 + (600 * direction * (
                    (total_bounces - inital_fraction) - int(total_bounces - inital_fraction)))
            else:
                machine_y = (600 * direction * (
                    (total_bounces - inital_fraction) - int(total_bounces - inital_fraction)))

    # calculate ball movement for a single tick
    if ball_v <= abs(ball_vector*ballspeed/90) and ball_vector < 0: # calulate ball_v when bounce off top
        ball_vector *= -1
        ball_v = (ballspeed * ball_vector / 90) - ball_v
    elif ball_v >= (600 - ball_vector*ballspeed/90) and ball_vector > 1:  # calulate ball_v when bounce off bottom
        ball_vector *= -1
        ball_v = 600 + (ball_vector*ballspeed/90) - (600 - ball_v)
    else:
        ball_v += ballspeed * ball_vector / 90
    ball_h += ballspeed * ball_direction

    # AI movement calculation
    if ai_y+ai_y_change < machine_y:
        ai_y += ai_y_change
    elif ai_y-ai_y_change > machine_y:
        ai_y -= ai_y_change

    lead_y += lead_y_change
    gameDisplay.fill(white)
    #pygame.draw.rect(gameDisplay, black, [400,300,10,100])
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 50])
    pygame.draw.rect(gameDisplay, black, [398, 0, 4, 600])
    pygame.draw.rect(gameDisplay, black, [ai_x, ai_y-25, 10, 50])
    pygame.draw.circle(gameDisplay, red, [ball_h,int(ball_v)], 10)
    # gameDisplay.fill(red, rect=[200,200,50,50])
    pygame.display.update()

    clock.tick(20)





pygame.quit()
quit()

