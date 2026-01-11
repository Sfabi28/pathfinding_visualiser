import pygame

BLACK = (0, 0, 0)
TEXT_COLOR = (0, 0, 0)

BUTTON_COLOR = (180, 180, 180)
BUTTON_HOVER_COLOR = (200, 200, 200)

WATER = (64, 164, 223)
WATER_HOVER = (100, 200, 255)

MUD = (139, 69, 19)
MUD_HOVER = (170, 100, 50)

class Button:
    def __init__(self, x, y, width, height, text, base_color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.SysFont('Arial', 20, bold=True)
        self.base_color = base_color
        self.hover_color = hover_color
    
    def draw(self, win):
        mouse_pos = pygame.mouse.get_pos()
        
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.base_color
        
        pygame.draw.rect(win, color, self.rect)
        pygame.draw.rect(win, BLACK, self.rect, 2)
        
        text_surf = self.font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        win.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)