import pygame
import pytest
from game import our_snake, gameLoop  # Certifique-se de que essas funções existem no game.py


@pytest.fixture
def init_pygame():
    pygame.init()
    dis_width = 800
    dis_height = 600
    dis = pygame.display.set_mode((dis_width, dis_height))
    yield dis
    pygame.quit()


def test_snake_draw(init_pygame):
    dis = init_pygame
    snake_block = 10
    snake_list = [[100, 50], [90, 50], [80, 50]]

    # Testando se a função desenha a cobra corretamente
    our_snake(snake_block, snake_list)
    pixels = pygame.PixelArray(dis)
    assert pixels[100][50] == dis.map_rgb((0, 255, 0))
    assert pixels[90][50] == dis.map_rgb((0, 255, 0))
    assert pixels[80][50] == dis.map_rgb((0, 255, 0))
    del pixels


def test_game_loop_quit_event(mocker):
    # Mock do evento QUIT
    mocker.patch('pygame.event.get', return_value=[pygame.event.Event(pygame.QUIT)])

    with pytest.raises(SystemExit):
        gameLoop()
