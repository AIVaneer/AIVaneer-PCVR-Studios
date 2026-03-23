"""
Tests for skyburner/atlas_nexus.py:
  Entity, Component, ScoreManager, WaveManager, CollisionSystem
"""
import sys
import os
import pytest

# Ensure skyburner/ is importable
SKY_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "skyburner",
)
if SKY_PATH not in sys.path:
    sys.path.insert(0, SKY_PATH)


# ---------------------------------------------------------------------------
# Vector2
# ---------------------------------------------------------------------------

class TestVector2:
    def test_default_values(self):
        from atlas_nexus import Vector2
        v = Vector2()
        assert v.x == 0.0
        assert v.y == 0.0

    def test_addition(self):
        from atlas_nexus import Vector2
        a = Vector2(1, 2)
        b = Vector2(3, 4)
        c = a + b
        assert c.x == 4.0
        assert c.y == 6.0

    def test_subtraction(self):
        from atlas_nexus import Vector2
        a = Vector2(5, 7)
        b = Vector2(2, 3)
        c = a - b
        assert c.x == 3.0
        assert c.y == 4.0

    def test_scalar_multiply(self):
        from atlas_nexus import Vector2
        v = Vector2(3, 4)
        v2 = v * 2
        assert v2.x == 6.0
        assert v2.y == 8.0

    def test_length(self):
        from atlas_nexus import Vector2
        import math
        v = Vector2(3, 4)
        assert abs(v.length() - 5.0) < 1e-9

    def test_normalized(self):
        from atlas_nexus import Vector2
        v = Vector2(0, 5)
        n = v.normalized()
        assert abs(n.x) < 1e-9
        assert abs(n.y - 1.0) < 1e-9

    def test_normalize_zero_vector(self):
        from atlas_nexus import Vector2
        v = Vector2(0, 0)
        n = v.normalized()
        assert n.x == 0.0
        assert n.y == 0.0

    def test_distance_to(self):
        from atlas_nexus import Vector2
        a = Vector2(0, 0)
        b = Vector2(3, 4)
        assert abs(a.distance_to(b) - 5.0) < 1e-9

    def test_to_tuple(self):
        from atlas_nexus import Vector2
        v = Vector2(1, 2)
        assert v.to_tuple() == (1.0, 2.0)


# ---------------------------------------------------------------------------
# AABB
# ---------------------------------------------------------------------------

class TestAABB:
    def test_intersects_overlapping(self):
        from atlas_nexus import AABB
        a = AABB(0, 0, 10, 10)
        b = AABB(5, 5, 10, 10)
        assert a.intersects(b) is True

    def test_no_intersection(self):
        from atlas_nexus import AABB
        a = AABB(0, 0, 4, 4)
        b = AABB(20, 20, 4, 4)
        assert a.intersects(b) is False

    def test_edge_touching_no_overlap(self):
        from atlas_nexus import AABB
        # hw = 5, so centers 10 apart exactly should NOT overlap (strict <)
        a = AABB(0, 0, 10, 10)
        b = AABB(10, 0, 10, 10)
        assert a.intersects(b) is False


# ---------------------------------------------------------------------------
# Entity / Component system
# ---------------------------------------------------------------------------

class TestComponent:
    def test_component_default_enabled(self):
        from atlas_nexus import Component
        c = Component()
        assert c.enabled is True

    def test_component_update_noop(self):
        from atlas_nexus import Component
        c = Component()
        c.update(0.016)  # should not raise

    def test_transform_component_integrates(self):
        from atlas_nexus import TransformComponent, Vector2
        tc = TransformComponent(0, 0)
        tc.velocity = Vector2(10, 0)
        tc.update(1.0)
        assert abs(tc.position.x - 10.0) < 1e-9

    def test_health_component_take_damage(self):
        from atlas_nexus import HealthComponent
        hc = HealthComponent(100)
        hc.take_damage(30)
        assert hc.current_health == 70.0

    def test_health_component_is_dead(self):
        from atlas_nexus import HealthComponent
        hc = HealthComponent(10)
        hc.take_damage(10)
        assert hc.is_dead is True

    def test_health_component_heal_capped(self):
        from atlas_nexus import HealthComponent
        hc = HealthComponent(100)
        hc.take_damage(50)
        hc.heal(200)
        assert hc.current_health == 100.0

    def test_health_ratio(self):
        from atlas_nexus import HealthComponent
        hc = HealthComponent(100)
        hc.take_damage(25)
        assert abs(hc.health_ratio - 0.75) < 1e-9


class TestEntity:
    def test_entity_add_and_get_component(self):
        from atlas_nexus import Entity, TransformComponent
        e = Entity("hero")
        tc = TransformComponent(1, 2)
        e.add_component(tc)
        result = e.get_component(TransformComponent)
        assert result is tc

    def test_entity_has_component(self):
        from atlas_nexus import Entity, HealthComponent
        e = Entity("enemy")
        assert e.has_component(HealthComponent) is False
        e.add_component(HealthComponent(50))
        assert e.has_component(HealthComponent) is True

    def test_entity_tags(self):
        from atlas_nexus import Entity
        e = Entity("bullet")
        e.add_tag("player_bullet")
        assert e.has_tag("player_bullet") is True
        assert e.has_tag("enemy") is False

    def test_entity_update_calls_components(self):
        from atlas_nexus import Entity, TransformComponent, Vector2
        e = Entity("ship")
        tc = TransformComponent(0, 0)
        tc.velocity = Vector2(5, 0)
        e.add_component(tc)
        e.update(1.0)
        assert abs(tc.position.x - 5.0) < 1e-9

    def test_entity_destroy_sets_flag(self):
        from atlas_nexus import Entity
        e = Entity("mine")
        e.destroy()
        assert e.active is False


# ---------------------------------------------------------------------------
# EntityManager
# ---------------------------------------------------------------------------

class TestEntityManager:
    def test_add_and_get_by_tag(self, entity_manager):
        from atlas_nexus import Entity
        e = Entity("p")
        e.add_tag("player")
        entity_manager.add(e)
        result = entity_manager.get_by_tag("player")
        assert e in result

    def test_remove_entity(self, entity_manager):
        from atlas_nexus import Entity
        e = Entity("x")
        e.add_tag("x")
        entity_manager.add(e)
        entity_manager.remove(e)
        entity_manager.update(0.016)  # flush deferred removal
        assert e not in entity_manager.get_by_tag("x")

    def test_dead_entities_cleaned_on_update(self, entity_manager):
        from atlas_nexus import Entity
        e = Entity("ghost")
        e.add_tag("ghost")
        entity_manager.add(e)
        e.active = False
        entity_manager.remove(e)
        entity_manager.update(0.016)
        assert e not in entity_manager.get_by_tag("ghost")

    def test_clear_removes_all(self, entity_manager):
        from atlas_nexus import Entity
        for i in range(5):
            entity_manager.add(Entity(f"e{i}"))
        entity_manager.clear()
        assert len(entity_manager.entities) == 0


# ---------------------------------------------------------------------------
# ScoreManager
# ---------------------------------------------------------------------------

class TestScoreManager:
    def test_initial_state(self, score_manager):
        sm = score_manager
        assert sm.score == 0
        assert sm.high_score == 0
        assert sm.multiplier == 1
        assert sm.wave == 1

    def test_add_score(self, score_manager):
        sm = score_manager
        sm.add_score(100)
        assert sm.score == 100

    def test_high_score_tracks(self, score_manager):
        sm = score_manager
        sm.add_score(500)
        sm.score = 0   # simulate reset without touching high_score
        sm.add_score(100)
        assert sm.high_score == 500

    def test_multiplier_applied(self, score_manager):
        sm = score_manager
        sm.multiplier = 3
        earned = sm.add_score(100)
        assert earned == 300
        assert sm.score == 300

    def test_combo_builds_multiplier(self, score_manager):
        sm = score_manager
        # 5 kills in a row should raise multiplier to 2
        for _ in range(5):
            sm.register_kill(10)
        assert sm.multiplier == 2

    def test_multiplier_capped_at_8(self, score_manager):
        sm = score_manager
        sm.multiplier = 8
        # Another batch of 5 should not exceed 8
        for _ in range(5):
            sm.register_kill(10)
        assert sm.multiplier <= 8

    def test_reset_clears_score(self, score_manager):
        sm = score_manager
        sm.add_score(9999)
        sm.multiplier = 5
        sm.reset()
        assert sm.score == 0
        assert sm.multiplier == 1

    def test_next_wave_increments(self, score_manager):
        sm = score_manager
        sm.next_wave()
        assert sm.wave == 2

    def test_level_up_every_5_waves(self, score_manager):
        sm = score_manager
        for _ in range(4):
            sm.next_wave()
        assert sm.level == 2   # wave 5 triggers level 2


# ---------------------------------------------------------------------------
# WaveManager
# ---------------------------------------------------------------------------

class TestWaveManager:
    def test_initial_state(self, wave_manager):
        wm = wave_manager
        assert wm.wave_number == 1
        assert wm.wave_complete is False

    def test_start_wave_builds_data(self, wave_manager):
        wm = wave_manager
        wm.start_wave(1)
        assert len(wm._wave_data) > 0

    def test_boss_wave_on_multiples_of_5(self, wave_manager):
        wm = wave_manager
        wm.start_wave(5)
        assert wm.is_boss_wave is True

    def test_non_boss_wave(self, wave_manager):
        wm = wave_manager
        wm.start_wave(3)
        assert wm.is_boss_wave is False

    def test_wave_complete_when_all_destroyed(self, wave_manager):
        wm = wave_manager
        wm.start_wave(1)
        # Fast-forward spawning
        wm.update(999.0)
        for _ in range(wm.enemies_spawned):
            wm.enemy_destroyed()
        assert wm.wave_complete is True

    def test_reset_clears_state(self, wave_manager):
        wm = wave_manager
        wm.start_wave(3)
        wm.reset()
        assert wm.wave_number == 1
        assert wm._wave_data == []

    def test_spawn_callback_invoked(self, wave_manager):
        wm = wave_manager
        spawned = []
        wm.on_enemy_spawn = lambda entry: spawned.append(entry)
        wm.start_wave(1)
        wm.update(999.0)
        assert len(spawned) > 0


# ---------------------------------------------------------------------------
# AtlasNexusEngine
# ---------------------------------------------------------------------------

class TestAtlasNexusEngine:
    def test_engine_has_managers(self, atlas_engine):
        from atlas_nexus import (
            EntityManager, ScoreManager, WaveManager, CollisionManager
        )
        eng = atlas_engine
        assert isinstance(eng.entity_manager, EntityManager)
        assert isinstance(eng.score_manager, ScoreManager)
        assert isinstance(eng.wave_manager, WaveManager)
        assert isinstance(eng.collision_manager, CollisionManager)

    def test_engine_update_does_not_raise(self, atlas_engine):
        from atlas_nexus import Entity, TransformComponent, Vector2
        atlas_engine.start()
        # Add an entity with movement so we can verify state changed
        e = Entity("ship")
        tc = TransformComponent(0, 0)
        tc.velocity = Vector2(10, 0)
        e.add_component(tc)
        atlas_engine.entity_manager.add(e)
        atlas_engine.update(0.016)
        # Position should have advanced (10 * 0.016 = 0.16)
        assert tc.position.x > 0
