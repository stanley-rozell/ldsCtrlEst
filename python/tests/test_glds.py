import numpy as np
import pytest

import ldsctrlest

def test_glds_sys():
    ldsctrlest.gaussian.System()
    ldsctrlest.gaussian.System(2, 2, 2, .001)
    ldsctrlest.gaussian.System(2, 2, 2, .001, r0=.2)
    ldsctrlest.gaussian.System(2, 2, 2, .001, p0=.4)
    gs = ldsctrlest.gaussian.System(2, 2, 2, .001, p0=.4, q0=7)
    with pytest.raises(TypeError):
        ldsctrlest.gaussian.System(42)
    gs.__repr__()

    gs.Filter([1, 1], [2, 1])
    with pytest.raises(TypeError):
        gs.Filter()

    prev_x = gs.x
    gs.Simulate(3)
    gs.Reset()
    assert gs.x != prev_x
    with pytest.raises(TypeError):
        gs.Simulate()
    
    with pytest.raises(TypeError):
        ldsctrlest.gaussian.System(42)

def test_glds_sys_get_set():
    gs = ldsctrlest.gaussian.System(3, 2, 4, .001, p0=.4, q0=7)
    assert len(gs.x) == 2
    gs.x = [7, 7]
    assert np.all(gs.x == [7, 7])

    gs.x0
    gs.x0 = [1,2]
    gs.m
    gs.m = [3, 4]
    gs.set_m([3, 4], do_force_assign=True)
    gs.A
    gs.A = [[1, 2], [5, 6]]
    gs.B
    gs.B = np.zeros((gs.n_x, gs.n_u))
    gs.g
    gs.g = 5
    gs.C
    gs.C = np.zeros((gs.n_y, gs.n_x))
    gs.d = np.zeros(gs.n_y)

    gs.do_adapt_m
    gs.do_adapt_m = True

def test_glds_sys_get():
    gs = ldsctrlest.gaussian.System(2, 2, 2, .001, p0=.4, q0=7)
    gs.n_u
    gs.n_x
    gs.n_y
    gs.dt
    gs.P 
    gs.P_m
    gs.cx
    gs.y
    gs.Ke
    gs.Ke_m

def test_glds_sys_set():
    gs = ldsctrlest.gaussian.System(2, 2, 2, .001, p0=.4, q0=7)
    gs.Q = np.zeros((gs.n_x, gs.n_x))
    gs.Q_m = np.zeros((gs.n_x, gs.n_x))
    gs.P0 = np.zeros((gs.n_x, gs.n_x))
    gs.P0_m = np.zeros((gs.n_x, gs.n_x))
