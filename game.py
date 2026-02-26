import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Simple Catch Game"

PLAYER_SPEED = 7
FALL_SPEED = 5


class CatchGame(git add .
git commit -m "add game file"
git pusharcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player_list = None
        self.falling_objects = None
        self.player = None
        self.score = 0

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.falling_objects = arcade.SpriteList()

        self.player = arcade.SpriteSolidColor(80, 20, arcade.color.BLUE)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = 50

        self.player_list.append(self.player)

        self.score = 0

    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.falling_objects.draw()

        arcade.draw_text(
            f"Score: {self.score}",
            10,
            SCREEN_HEIGHT - 30,
            arcade.color.WHITE,
            18
        )

    def on_update(self, delta_time):

        # Движение игрока
        self.player.center_x += self.player.change_x

        if self.player.left < 0:
            self.player.left = 0
        if self.player.right > SCREEN_WIDTH:
            self.player.right = SCREEN_WIDTH

        # Создание падающих объектов
        if random.random() < 0.02:
            obj = arcade.SpriteSolidColor(30, 30, arcade.color.RED)
            obj.center_x = random.randint(20, SCREEN_WIDTH - 20)
            obj.center_y = SCREEN_HEIGHT
            self.falling_objects.append(obj)

        # Движение вниз
        for obj in self.falling_objects:
            obj.center_y -= FALL_SPEED

        # Столкновения
        hit_list = arcade.check_for_collision_with_list(self.player, self.falling_objects)

        for obj in hit_list:
            obj.remove_from_sprite_lists()
            self.score += 1

        # Удаление упавших
        for obj in self.falling_objects:
            if obj.center_y < 0:
                obj.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.player.change_x = 0


def main():
    game = CatchGame()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
