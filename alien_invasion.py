import sys
import pygame


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
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("ALIEN INVASION")

    def run_game(self):
        while True:
            """
            Отслеживаем, что нажимаем на клавиатуре и мыши.
            Watch for keyboard and mouse events.
            """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
