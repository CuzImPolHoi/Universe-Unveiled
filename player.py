
# LIBRARIES
import pygame

class Player:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

        self.imagepath = "graphics/characters/main_character_male/"

        self.animations = {
            "up_walk": [pygame.image.load(self.imagepath + "up_walk/0.png"), pygame.image.load(self.imagepath + "up_walk/1.png"), pygame.image.load(self.imagepath + "up_walk/2.png"), pygame.image.load(self.imagepath + "up_walk/3.png")],
            "down_walk": [pygame.image.load(self.imagepath + "down_walk/0.png"), pygame.image.load(self.imagepath + "down_walk/1.png"), pygame.image.load(self.imagepath + "down_walk/2.png"), pygame.image.load(self.imagepath + "down_walk/3.png")],
            "left_walk": [pygame.image.load(self.imagepath + "left_walk/0.png"), pygame.image.load(self.imagepath + "left_walk/1.png")],
            "right_walk": [pygame.image.load(self.imagepath + "right_walk/0.png"), pygame.image.load(self.imagepath + "right_walk/1.png")],
            "up_idle": [pygame.image.load(self.imagepath + "up_idle/0.png")],
            "down_idle": [pygame.image.load(self.imagepath + "down_idle/0.png")],
            "left_idle": [pygame.image.load(self.imagepath + "left_idle/0.png")],
            "right_idle": [pygame.image.load(self.imagepath + "right_idle/0.png")]
        }

        # variables for animations
        self.current_animation = "down_idle"
        self.current_frame = 0
        # variables for animation speed
        self.animation_speed = 10  # Adjust this value to change animation speed
        self.frame_counter = 0  # Counter to control animation speed

    def set_animation(self, animation):
        if animation != self.current_animation:
            self.current_animation = animation
            self.current_frame = 0  # Reset frame to the beginning of the animation

    def update_animation(self):
         if self.animations[self.current_animation]:
            self.frame_counter += 1
            if self.frame_counter >= self.animation_speed:
                self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_animation])
                self.frame_counter = 0  # Reset frame counter after changing frame

    def move(self, keys, screen_width, screen_height):
        if keys[pygame.K_w]:
            self.y -= self.speed
            self.set_animation("up_walk")

        if keys[pygame.K_s]:
            self.y += self.speed
            self.set_animation("down_walk")

        if keys[pygame.K_a]:
            self.x -= self.speed
            self.set_animation("left_walk")

        if keys[pygame.K_d]:
            self.x += self.speed
            self.set_animation("right_walk")

        if not any(keys):
            if self.current_animation.endswith('_walk'):
                self.set_animation(self.current_animation.replace('_walk', '_idle'))

        self.update_animation()


        # Boundary check to keep player within the screen
        if self.x < 0:
            self.x = 0
        elif self.x > screen_width - self.width:
            self.x = screen_width - self.width
        if self.y < 0:
            self.y = 0
        elif self.y > screen_height - self.height:
            self.y = screen_height - self.height

    def draw(self, screen):
        screen.blit(self.animations[self.current_animation][self.current_frame], (self.x, self.y))