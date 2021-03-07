"""Test gates defined in `qibo/core/cgates.py` and `qibo/core/gates.py` for density matrices."""
import pytest
import numpy as np
import qibo
from qibo import gates
from qibo.config import raise_error

_atol = 1e-8


def random_density_matrix(nqubits):
    """Generates a random density matrix.

    Note that the density matrix generated by this method is not necessarily
    positive. This is okay for most tests but may not work for some cases such
    as the entanglement entropy calculation.

    Args:
        nqubits (int): Number of qubits in the density matrix.

    Returns:
        Density matrix as a numpy array of shape (2 ** nqubits, 2 ** nqubits).
    """
    shape = 2 * (2 ** nqubits,)
    rho = np.random.random(shape) + 1j * np.random.random(shape)
    # Make Hermitian
    rho = (rho + rho.T.conj()) / 2.0
    # Normalize
    ids = np.arange(2 ** nqubits)
    rho[ids, ids] = rho[ids, ids] / np.trace(rho)
    return rho


def test_hgate_density_matrix(backend):
    original_backend = qibo.get_backend()
    qibo.set_backend(backend)
    initial_rho = random_density_matrix(2)
    gate = gates.H(1)
    gate.density_matrix = True
    final_rho = gate(np.copy(initial_rho))

    matrix = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    matrix = np.kron(np.eye(2), matrix)
    target_rho = matrix.dot(initial_rho).dot(matrix)
    np.testing.assert_allclose(final_rho, target_rho)
    qibo.set_backend(original_backend)


def test_rygate_density_matrix(backend):
    original_backend = qibo.get_backend()
    qibo.set_backend(backend)
    theta = 0.1234
    initial_rho = random_density_matrix(1)

    gate = gates.RY(0, theta=theta)
    gate.density_matrix = True
    final_rho = gate(np.copy(initial_rho))

    phase = np.exp(1j * theta / 2.0)
    matrix = phase * np.array([[phase.real, -phase.imag], [phase.imag, phase.real]])
    target_rho = matrix.dot(initial_rho).dot(matrix.T.conj())

    np.testing.assert_allclose(final_rho, target_rho, atol=_atol)
    qibo.set_backend(original_backend)


@pytest.mark.parametrize("gatename,gatekwargs",
                         [("H", {}), ("X", {}), ("Y", {}), ("Z", {}), ("I", {}),
                          ("RX", {"theta": 0.123}), ("RY", {"theta": 0.123}),
                          ("RZ", {"theta": 0.123}), ("U1", {"theta": 0.123}),
                          ("ZPow", {"theta": 0.123}),
                          ("U2", {"phi": 0.123, "lam": 0.321}),
                          ("U3", {"theta": 0.123, "phi": 0.321, "lam": 0.123})])
def test_one_qubit_gates(backend, gatename, gatekwargs):
    """Check applying one qubit gates to one qubit density matrix."""
    original_backend = qibo.get_backend()
    qibo.set_backend(backend)
    initial_rho = random_density_matrix(1)
    gate = getattr(gates, gatename)(0, **gatekwargs)
    gate.density_matrix = True
    final_rho = gate(np.copy(initial_rho))

    matrix = np.array(gate.unitary)
    target_rho = np.einsum("ab,bc,cd->ad", matrix, initial_rho, matrix.conj().T)
    np.testing.assert_allclose(final_rho, target_rho)
    qibo.set_backend(original_backend)


@pytest.mark.parametrize("gatename", ["H", "X", "Y", "Z"])
def test_controlled_by_one_qubit_gates(backend, gatename):
    original_backend = qibo.get_backend()
    qibo.set_backend(backend)
    initial_rho = random_density_matrix(2)
    gate = getattr(gates, gatename)(1).controlled_by(0)
    gate.density_matrix = True
    final_rho = gate(np.copy(initial_rho))

    from qibo import matrices
    matrix = getattr(matrices, gatename)
    cmatrix = np.eye(4, dtype=matrix.dtype)
    cmatrix[2:, 2:] = matrix
    target_rho = np.einsum("ab,bc,cd->ad", cmatrix, initial_rho, cmatrix.conj().T)
    np.testing.assert_allclose(final_rho, target_rho)
    qibo.set_backend(original_backend)


@pytest.mark.parametrize("gatename,gatekwargs",
                         [("CNOT", {}), ("CZ", {}), ("SWAP", {}),
                          ("CRX", {"theta": 0.123}), ("CRY", {"theta": 0.123}),
                          ("CRZ", {"theta": 0.123}), ("CU1", {"theta": 0.123}),
                          ("CZPow", {"theta": 0.123}),
                          ("CU2", {"phi": 0.123, "lam": 0.321}),
                          ("CU3", {"theta": 0.123, "phi": 0.321, "lam": 0.123}),
                          ("fSim", {"theta": 0.123, "phi": 0.543})])
def test_two_qubit_gates(backend, gatename, gatekwargs):
    """Check applying two qubit gates to two qubit density matrix."""
    original_backend = qibo.get_backend()
    qibo.set_backend(backend)
    initial_rho = random_density_matrix(2)
    gate = getattr(gates, gatename)(0, 1, **gatekwargs)
    gate.density_matrix = True
    final_rho = gate(np.copy(initial_rho))

    matrix = np.array(gate.unitary)
    target_rho = np.einsum("ab,bc,cd->ad", matrix, initial_rho, matrix.conj().T)
    np.testing.assert_allclose(final_rho, target_rho, atol=_atol)
    qibo.set_backend(original_backend)


def test_toffoli_gate(backend):
    """Check applying Toffoli to three qubit density matrix."""
    original_backend = qibo.get_backend()
    qibo.set_backend(backend)
    initial_rho = random_density_matrix(3)
    gate = gates.TOFFOLI(0, 1, 2)
    gate.density_matrix = True
    final_rho = gate(np.copy(initial_rho))

    matrix = np.array(gate.unitary)
    target_rho = np.einsum("ab,bc,cd->ad", matrix, initial_rho, matrix.conj().T)
    np.testing.assert_allclose(final_rho, target_rho)
    qibo.set_backend(original_backend)


@pytest.mark.parametrize("nqubits", [1, 2, 3])
def test_unitary_gate(backend, nqubits):
    """Check applying `gates.Unitary` to density matrix."""
    original_backend = qibo.get_backend()
    qibo.set_backend(backend)
    shape = 2 * (2 ** nqubits,)
    matrix = np.random.random(shape) + 1j * np.random.random(shape)
    initial_rho = random_density_matrix(nqubits)
    if backend == "custom" and nqubits > 2:
        with pytest.raises(NotImplementedError):
            gate = gates.Unitary(matrix, *range(nqubits))
    else:
        gate = gates.Unitary(matrix, *range(nqubits))
        gate.density_matrix = True
        final_rho = gate(np.copy(initial_rho))
        target_rho = np.einsum("ab,bc,cd->ad", matrix, initial_rho, matrix.conj().T)
        np.testing.assert_allclose(final_rho, target_rho)
    qibo.set_backend(original_backend)


def test_cu1gate_application_twoqubit(backend):
    """Check applying two qubit gate to three qubit density matrix."""
    original_backend = qibo.get_backend()
    qibo.set_backend(backend)
    theta = 0.1234
    nqubits = 3
    initial_rho = random_density_matrix(nqubits)
    gate = gates.CU1(0, 1, theta=theta)
    gate.density_matrix = True
    final_rho = gate(np.copy(initial_rho))

    matrix = np.eye(4, dtype=np.complex128)
    matrix[3, 3] = np.exp(1j * theta)
    matrix = np.kron(matrix, np.eye(2))
    target_rho = matrix.dot(initial_rho).dot(matrix.T.conj())
    np.testing.assert_allclose(final_rho, target_rho)
    qibo.set_backend(original_backend)


def test_flatten_density_matrix(backend):
    """Check ``Flatten`` gate works with density matrices."""
    original_backend = qibo.get_backend()
    qibo.set_backend(backend)
    target_rho = random_density_matrix(3)
    initial_rho = np.zeros(6 * (2,))
    gate = gates.Flatten(target_rho)
    gate.density_matrix = True
    final_rho = np.reshape(gate(initial_rho), (8, 8))
    np.testing.assert_allclose(final_rho, target_rho)
    qibo.set_backend(original_backend)


def test_controlled_by_no_effect(backend):
    """Check controlled_by SWAP that should not be applied."""
    original_backend = qibo.get_backend()
    qibo.set_backend(backend)
    from qibo.models import Circuit
    initial_rho = np.zeros((16, 16))
    initial_rho[0, 0] = 1

    c = Circuit(4, density_matrix=True)
    c.add(gates.X(0))
    c.add(gates.SWAP(1, 3).controlled_by(0, 2))
    final_rho = c(np.copy(initial_rho)).numpy()

    c = Circuit(4, density_matrix=True)
    c.add(gates.X(0))
    target_rho = c(np.copy(initial_rho)).numpy()
    np.testing.assert_allclose(final_rho, target_rho)
    qibo.set_backend(original_backend)


def test_controlled_with_effect(backend):
    """Check controlled_by SWAP that should be applied."""
    original_backend = qibo.get_backend()
    qibo.set_backend(backend)
    from qibo.models import Circuit
    initial_rho = np.zeros((16, 16))
    initial_rho[0, 0] = 1

    c = Circuit(4, density_matrix=True)
    c.add(gates.X(0))
    c.add(gates.X(2))
    c.add(gates.SWAP(1, 3).controlled_by(0, 2))
    final_rho = c(np.copy(initial_rho)).numpy()

    c = Circuit(4, density_matrix=True)
    c.add(gates.X(0))
    c.add(gates.X(2))
    c.add(gates.SWAP(1, 3))
    target_rho = c(np.copy(initial_rho)).numpy()
    np.testing.assert_allclose(final_rho, target_rho)
    qibo.set_backend(original_backend)


@pytest.mark.parametrize("nqubits", [4, 5])
def test_controlled_by_random(backend, nqubits):
    """Check controlled_by method on gate."""
    original_backend = qibo.get_backend()
    qibo.set_backend(backend)
    from qibo.models import Circuit
    from qibo.tests_new.test_core_gates import random_state
    initial_psi = random_state(nqubits)
    initial_rho = np.outer(initial_psi, initial_psi.conj())
    c = Circuit(nqubits, density_matrix=True)
    c.add(gates.RX(1, theta=0.789).controlled_by(2))
    c.add(gates.fSim(0, 2, theta=0.123, phi=0.321).controlled_by(1, 3))
    final_rho = c(np.copy(initial_rho))

    c = Circuit(nqubits)
    c.add(gates.RX(1, theta=0.789).controlled_by(2))
    c.add(gates.fSim(0, 2, theta=0.123, phi=0.321).controlled_by(1, 3))
    target_psi = c(np.copy(initial_psi))
    target_rho = np.outer(target_psi, np.conj(target_psi))
    np.testing.assert_allclose(final_rho, target_rho)
    qibo.set_backend(original_backend)


@pytest.mark.parametrize("nqubits,targets,results",
                         [(2, [1], [0]), (3, [1], 0), (4, [1, 3], [0, 1]),
                          (5, [0, 3, 4], [1, 1, 0])])
def test_collapse_gate(backend, nqubits, targets, results):
    original_backend = qibo.get_backend()
    qibo.set_backend(backend)
    initial_rho = random_density_matrix(nqubits)
    gate = gates.Collapse(*targets, result=results)
    gate.density_matrix = True
    final_rho = gate(np.copy(initial_rho))

    target_rho = np.reshape(initial_rho, 2 * nqubits * (2,))
    if isinstance(results, int):
        results = len(targets) * [results]
    for q, r in zip(targets, results):
        slicer = 2 * nqubits * [slice(None)]
        slicer[q], slicer[q + nqubits] = 1 - r, 1 - r
        target_rho[tuple(slicer)] = 0
        slicer[q], slicer[q + nqubits] = r, 1 - r
        target_rho[tuple(slicer)] = 0
        slicer[q], slicer[q + nqubits] = 1 - r, r
        target_rho[tuple(slicer)] = 0
    target_rho = np.reshape(target_rho, initial_rho.shape)
    target_rho = target_rho / np.trace(target_rho)
    np.testing.assert_allclose(final_rho, target_rho)
    qibo.set_backend(original_backend)


@pytest.mark.parametrize("qubit", [0, 1, 2])
def test_partial_trace_gate(backend, qubit):
    original_backend = qibo.get_backend()
    qibo.set_backend(backend)
    gate = gates.PartialTrace(qubit)
    gate.density_matrix = True
    initial_rho = random_density_matrix(3)
    final_state = gate(np.copy(initial_rho))

    zero_state = np.array([[1, 0], [0, 0]])
    target_state = np.reshape(initial_rho, 6 * (2,))
    if qubit == 0:
        target_state = np.einsum("aBCabc,Dd->DBCdbc", target_state, zero_state)
    elif qubit == 1:
        target_state = np.einsum("AbCabc,Dd->ADCadc", target_state, zero_state)
    elif qubit == 2:
        target_state = np.einsum("ABcabc,Dd->ABDabd", target_state, zero_state)
    target_state = np.reshape(target_state, (8, 8))
    np.testing.assert_allclose(final_state, target_state)
    qibo.set_backend(original_backend)


def test_partial_trace_gate_errors(backend):
    original_backend = qibo.get_backend()
    qibo.set_backend(backend)
    gate = gates.PartialTrace(0, 1)
    # attempt to create unitary matrix
    with pytest.raises(ValueError):
        gate.construct_unitary()
    # attempt to call on state vector
    state = np.random.random(16) + 1j * np.random.random(16)
    with pytest.raises(RuntimeError):
        gate(state)
    qibo.set_backend(original_backend)
