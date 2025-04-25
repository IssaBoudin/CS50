import builtins
import pytest
from unittest.mock import Mock

import project

#I believe button. But this is very important for threading. Fingers crossed.
class DummyThread:
    def __init__(self, *args, **kwargs):
        pass
    def start(self):
        pass

#Figlet needs help exiting correctly.
def stub_figlet(final):
    raise SystemExit(0)

#Reset global score before/after each test.
@pytest.fixture(autouse=True)
def reset_score():
    project.score = 0
    yield
    project.score = 0

#Does main call pick function?
def test_main_calls_pick(monkeypatch):
    monkeypatch.setattr(project, "pick", lambda: (_ for _ in ()).throw(RuntimeError("done")))
    with pytest.raises(RuntimeError) as exc:
        project.main()
    assert "done" in str(exc.value)

#Does "1" call addition function?
def test_pick_calls_addition(monkeypatch):
    inputs = iter(["1"])
    def fake_input(prompt):
        try:
            return next(inputs)
        except StopIteration:
            raise RuntimeError("stop")
    monkeypatch.setattr(builtins, "input", fake_input)

    called = {}
    monkeypatch.setattr(project, "addition", lambda: called.setdefault('addition', True))

    with pytest.raises(RuntimeError):
        project.pick()
    assert called.get('addition') is True

#Does countdown print "GAME OVER", stop music, play negative sound, and lastly call figlet?
def test_countdown_flow(monkeypatch, capsys):
    #Does it sleep?
    monkeypatch.setattr(project.time, "sleep", lambda x: None)
    #Does pygame stop?
    music_stop = Mock()
    monkeypatch.setattr(project.pygame.mixer.music, "stop", music_stop)
    #Guitar sound?
    played = {}
    class Neg:
        def play(self): return self
        def wait_done(self): played['done'] = True
    monkeypatch.setattr(project.sa.WaveObject, "from_wave_file", lambda _: Neg())
    #Fake so we don't actually exit the program.
    fig_called = {}
    monkeypatch.setattr(project, "figlet", lambda s: fig_called.setdefault('figlet', s))

    project.countdown()

    out = capsys.readouterr().out
    assert "GAME OVER" in out
    assert music_stop.called, "pygame.mixer.music.stop() was not called"
    assert played.get('done', False), "NegativeGuitar.wav.play().wait_done() was not called"
    assert fig_called.get('figlet', "").startswith("Score:")

#Does get_level disallow bad/out-of-range input? Does good input "2" work?
def test_get_level(monkeypatch):
    inputs = iter(["foo", "0", "4", "2"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    assert project.get_level() == 2

#Does addition work with hard-coded x & y values? Does it output score?
def test_addition_all_correct(monkeypatch):
    monkeypatch.setattr(project, "get_level", lambda: 1)
    monkeypatch.setattr(project, "generate_integer", lambda lvl: 2)
    monkeypatch.setattr(builtins, "input", lambda _: "4")
    monkeypatch.setattr(project.threading, "Thread", DummyThread)
    monkeypatch.setattr(project, "figlet", stub_figlet)

    with pytest.raises(SystemExit):
        project.addition()
    assert project.score == 10

#Does subtraction work with hard-coded x & y values? (answer 2)
def test_subtraction_all_correct(monkeypatch):
    monkeypatch.setattr(project, "get_level", lambda: 1)
    def gen(level):
        val = 5 if gen.count % 2 == 0 else 3
        gen.count += 1
        return val
    gen.count = 0
    monkeypatch.setattr(project, "generate_integer", gen)
    monkeypatch.setattr(builtins, "input", lambda _: "2")
    monkeypatch.setattr(project.threading, "Thread", DummyThread)
    monkeypatch.setattr(project, "figlet", stub_figlet)

    with pytest.raises(SystemExit):
        project.subtraction()
    assert project.score == 10

#Does multiplication work with hard-coded x & y values? (answer 12)
def test_multiplication_all_correct(monkeypatch):
    monkeypatch.setattr(project, "get_level", lambda: 1)
    def gen(level):
        val = 3 if gen.count % 2 == 0 else 4
        gen.count += 1
        return val
    gen.count = 0
    monkeypatch.setattr(project, "generate_integer", gen)
    monkeypatch.setattr(builtins, "input", lambda _: "12")
    monkeypatch.setattr(project.threading, "Thread", DummyThread)
    monkeypatch.setattr(project, "figlet", stub_figlet)

    with pytest.raises(SystemExit):
        project.multiplication()
    assert project.score == 10

#Does division work with hard-coded x & y values? (answer 4)
def test_division_all_correct(monkeypatch):
    monkeypatch.setattr(project, "get_level", lambda: 1)
    def gen(level):
        val = 8 if gen.count % 2 == 0 else 2
        gen.count += 1
        return val
    gen.count = 0
    monkeypatch.setattr(project, "generate_integer", gen)
    monkeypatch.setattr(builtins, "input", lambda _: "4")
    monkeypatch.setattr(project.threading, "Thread", DummyThread)
    monkeypatch.setattr(project, "figlet", stub_figlet)

    with pytest.raises(SystemExit):
        project.division()
    assert project.score == 10

#Does generate_integer return the correct ranges?
def test_generate_integer_ranges():
    for lvl, lo, hi in [(1, 0, 9), (2, 10, 99), (3, 100, 999)]:
        for _ in range(50):
            v = project.generate_integer(lvl)
            assert lo <= v <= hi

#Does figlet render and exit?
def test_figlet_exits_and_prints(monkeypatch, capsys):
    class DummyF:
        def setFont(self, **kw): pass
        def renderText(self, txt): return f"[FIGLET:{txt}]"
    monkeypatch.setattr(project, "Figlet", lambda: DummyF())
    class DummyW:
        def play(self): return self
        def wait_done(self): pass
    monkeypatch.setattr(project.sa.WaveObject, "from_wave_file", lambda _: DummyW())

    with pytest.raises(SystemExit):
        project.figlet("HELLO")
    out = capsys.readouterr().out
    assert "[FIGLET:HELLO]" in out
