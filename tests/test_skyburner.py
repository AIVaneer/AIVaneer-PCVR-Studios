"""Pytest stubs for the skyburner module."""

from skyburner.atlas_nexus import AtlasNexusEngine
from skyburner.entities import Enemy, Entity, PlayerShip, PowerUp, Projectile
from skyburner.main_scene import MainScene


class TestAtlasNexusEngine:
    def test_default_dimensions(self):
        engine = AtlasNexusEngine()
        assert engine.width == 375
        assert engine.height == 667
        assert engine.fps == 60

    def test_custom_dimensions(self):
        engine = AtlasNexusEngine(width=1920, height=1080, fps=30)
        assert engine.width == 1920
        assert engine.height == 1080
        assert engine.fps == 30

    def test_starts_stopped(self):
        engine = AtlasNexusEngine()
        assert not engine.is_running

    def test_start_stop(self):
        engine = AtlasNexusEngine()
        engine.start()
        assert engine.is_running
        engine.stop()
        assert not engine.is_running


class TestEntities:
    def test_entity_defaults(self):
        e = Entity()
        assert e.x == 0.0
        assert e.y == 0.0
        assert e.active is True

    def test_entity_repr(self):
        e = Entity(x=1.0, y=2.0)
        assert "Entity" in repr(e)

    def test_player_ship(self):
        p = PlayerShip(x=10.0, y=20.0, lives=5)
        assert p.lives == 5
        assert p.score == 0

    def test_enemy(self):
        en = Enemy(health=3)
        assert en.health == 3

    def test_projectile(self):
        proj = Projectile(speed=8.0)
        assert proj.speed == 8.0
        assert proj.owner is None

    def test_powerup(self):
        pu = PowerUp(kind="bomb")
        assert pu.kind == "bomb"


class TestMainScene:
    def test_scene_setup_and_teardown(self):
        scene = MainScene()
        scene.setup()
        assert scene.engine.is_running
        scene.teardown()
        assert not scene.engine.is_running

    def test_scene_has_player(self):
        scene = MainScene()
        assert isinstance(scene.player, PlayerShip)
        assert scene.player in scene.entities

    def test_update_does_not_raise(self):
        scene = MainScene()
        scene.setup()
        scene.update(dt=0.016)
        scene.teardown()
