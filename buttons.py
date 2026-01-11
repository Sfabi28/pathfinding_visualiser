import pygame

BLACK = (0, 0, 0) 
BUTTON_COLOR = (180, 180, 180)
BUTTON_HOVER_COLOR = (200, 200, 200)
TEXT_COLOR = (0, 0, 0)

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.SysFont('Arial', 20, bold=True)
    
    def draw(self, win):
        mouse_pos = pygame.mouse.get_pos()
        color = BUTTON_HOVER_COLOR if self.rect.collidepoint(mouse_pos) else BUTTON_COLOR
        
        pygame.draw.rect(win, color, self.rect)
        pygame.draw.rect(win, BLACK, self.rect, 2)
        
        text_surf = self.font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        win.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)