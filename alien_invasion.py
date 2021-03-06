import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """
    Общий класс для управления игрой.
    Overall	class to manage	game assets and behavior.
    """

    def __init__(self):
        """
        Инициализирует игру.
        Initialize the game, and create	game resources.
        """
        pygame.init()
        # programIcon = pygame.image.load("images/logo2.png")  # загружает поверхность лого
        # pygame.display.set_icon(programIcon)  # добавляет непосредственно programIcon в качестве иконки
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("ALIEN INVASION")
        self.ship = Ship(self)


    def run_game(self):
        while True:
            """

            """
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """

        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """

        """
        self.screen.fill(self.settings.bg_color)  # перерисовка фона при каждом проходе
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
