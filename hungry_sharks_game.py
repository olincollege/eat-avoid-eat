"""
Runs the Hungry Sharks game
"""
from hungry_sharks_view import PyGameView
from hungry_sharks_field import HungrySharksField
from character_controller import PlayerVelocityController, AIVelocityController


def main():
    """
    Runs the game of Hungry Sharks
    """
    field = HungrySharksField(1200, 600, 10)
    view = PyGameView(field)
    player_controller = PlayerVelocityController(field, fps=view.fps)
    ai_controller = AIVelocityController(field, fps=view.fps)

    # main game loop
    while not field.game_end:
        # view
        view.draw()

        # control
        player_controller.move()
        ai_controller.move()

        # update model to valid state
        field.update()

    # win and lose screen
    end_screen_switcher = {
        "win" : view.win_screen,
        "lose" : view.lose_screen
    }

    end_screen_switcher[field.game_end]()


if __name__ == "__main__":
    main()
