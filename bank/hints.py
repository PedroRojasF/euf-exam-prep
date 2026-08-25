"""EUF Physics Solution Strategy & Contextual Hint Engine.
Generates tailored, subtopic-specific physical principles, coordinate setups, intermediate checkpoints, and limit checks.
"""

import re

# Comprehensive subtopic and concept-specific guidance dictionary
HINT_KNOWLEDGE_BASE = {
    # CLASSICAL MECHANICS
    "Lagrangian Mechanics & Constraints": {
        "title": "Lagrangian Mechanics & Generalized Coordinates",
        "level1": "Identify the degrees of freedom and choose generalized coordinates $q_1, \\dots, q_n$ that match the geometric symmetry. Set up kinetic energy $T$ and potential energy $V$. The Lagrangian is $L(q, \\dot{q}, t) = T - V$.",
        "level2": "Apply the Euler-Lagrange equations: $\\frac{d}{dt}\\left(\\frac{\\partial L}{\\partial \\dot{q}_i}\\right) - \\frac{\\partial L}{\\partial q_i} = 0$. If a coordinate $q_k$ is cyclic (absent from $L$), the conjugate momentum $p_k = \\frac{\\partial L}{\\partial \\dot{q}_k}$ is a strictly conserved constant of motion.",
        "level3": "For systems with holonomic constraints $f(q_1, \\dots, q_n) = 0$, either eliminate redundant variables or use Lagrange multipliers $\\lambda$ with modified equations: $\\frac{d}{dt}\\left(\\frac{\\partial L}{\\partial \\dot{q}_i}\\right) - \\frac{\\partial L}{\\partial q_i} = \\lambda \\frac{\\partial f}{\\partial q_i}$.",
        "level4": "Check physical limits: For static equilibrium ($\\dot{q}_i = 0, \\ddot{q}_i = 0$), the equations reduce to $\\frac{\\partial V}{\\partial q_i} = 0$. Verify dimensional consistency of generalized forces $[Q_i] = [\\text{Work}]/[q_i]$."
    },
    "Hamiltonian Mechanics & Phase Space": {
        "title": "Hamiltonian Formalism & Phase Space Dynamics",
        "level1": "Define conjugate momenta $p_i = \\frac{\\partial L}{\\partial \\dot{q}_i}$. Construct the Hamiltonian via Legendre transform: $H(q, p, t) = \\sum_i p_i \\dot{q}_i - L(q, \\dot{q}(q,p), t)$. If $L$ has no explicit time dependence, $H$ is conserved.",
        "level2": "Apply Hamilton's Canonical Equations: $\\dot{q}_i = \\frac{\\partial H}{\\partial p_i}$ and $\\dot{p}_i = -\\frac{\\partial H}{\\partial q_i}$. Time evolution of any observable $A(q, p)$ follows $\\frac{dA}{dt} = \\{A, H\\} + \\frac{\\partial A}{\\partial t}$.",
        "level3": "For Canonical Transformations $(q, p) \\to (Q, P)$, check Poisson Brackets: $\\{Q_i, Q_j\\} = 0$, $\\{P_i, P_j\\} = 0$, and $\\{Q_i, P_j\\} = \\delta_{ij}$. Alternatively, identify generating functions $F_1(q, Q), F_2(q, P)$.",
        "level4": "Phase space trajectory check: Liouville's Theorem ensures phase volume $d\\Gamma = \\prod dq_i dp_i$ is incompressible ($\\{d\\Gamma, H\\} = 0$). Check energy surfaces $H(q,p) = E$ for closed periodic orbits."
    },
    "Central Forces & Kepler Orbits": {
        "title": "Central Potential & Orbital Dynamics",
        "level1": "In a central potential $V(r)$, angular momentum $\\vec{L} = \\vec{r} \\times \\vec{p} = m r^2 \\dot{\\theta} \\hat{z}$ is strictly conserved, confining motion to a plane. Motion reduces to 1D via effective potential: $V_{\\text{eff}}(r) = V(r) + \\frac{L^2}{2mr^2}$.",
        "level2": "Radial equation of motion: $m\\ddot{r} = -\\frac{dV_{\\text{eff}}}{dr} = F(r) + \\frac{L^2}{mr^3}$. Circular orbits occur at the local minimum of $V_{\\text{eff}}$: $\\left.\\frac{dV_{\\text{eff}}}{dr}\\right|_{r_0} = 0$. Stability requires $\\left.\\frac{d^2 V_{\\text{eff}}}{dr^2}\\right|_{r_0} > 0$.",
        "level3": "For Keplerian gravity $V(r) = -\\frac{k}{r}$: The orbit equation is $r(\\theta) = \\frac{p}{1 + e\\cos\\theta}$, with semi-latus rectum $p = \\frac{L^2}{mk}$ and eccentricity $e = \\sqrt{1 + \\frac{2EL^2}{mk^2}}$. $E < 0 \\implies$ ellipse, $E = 0 \\implies$ parabola, $E > 0 \\implies$ hyperbola.",
        "level4": "Apsidal limits: At periapsis and apoapsis, radial velocity is zero ($\\dot{r} = 0$), so total energy is purely $E = V_{\\text{eff}}(r_{\\text{min}}) = V_{\\text{eff}}(r_{\\text{max}})$. Check Kepler's 3rd law: $T^2 = \\frac{4\\pi^2}{G(M+m)} a^3$."
    },
    "Rigid Body & Rotational Dynamics": {
        "title": "Rigid Body Mechanics & Rotation",
        "level1": "Relate angular momentum to angular velocity: $\\vec{L} = \\mathbf{I} \\vec{\\omega}$. Kinetic energy separates into translation of CM and rotation about CM: $T = \\frac{1}{2}M v_{\\text{CM}}^2 + \\frac{1}{2}\\vec{\\omega} \\cdot \\mathbf{I} \\vec{\\omega}$.",
        "level2": "Apply Parallel Axis Theorem (Steiner) for an axis shifted by distance $d$: $I = I_{\\text{CM}} + M d^2$. For pure rolling without slipping on a surface: $v_{\\text{CM}} = R \\omega$ and $a_{\\text{CM}} = R \\alpha$, with friction providing the torque $\\tau = I \\alpha$.",
        "level3": "Equations of rotational motion: $\\vec{\\tau}_{\\text{ext}} = \\left(\\frac{d\\vec{L}}{dt}\\right)_{\\text{inertial}} = \\left(\\frac{d\\vec{L}}{dt}\\right)_{\\text{body}} + \\vec{\\omega} \\times \\vec{L}$ (Euler's Equations for principal axes: $I_1 \\dot{\\omega}_1 - (I_2 - I_3)\\omega_2 \\omega_3 = \\tau_1$).",
        "level4": "Standard inertia moments from formula sheet: Solid sphere $\\frac{2}{5}MR^2$, spherical shell $\\frac{2}{3}MR^2$, solid cylinder/disk $\\frac{1}{2}MR^2$, thin rod $\\frac{1}{12}ML^2$ (center) or $\\frac{1}{3}ML^2$ (end)."
    },
    "Small Oscillations & Normal Modes": {
        "title": "Small Oscillations & Matrix Normal Modes",
        "level1": "Taylor expand potential about stable equilibrium $q_0$: $V(q) \\approx V(q_0) + \\frac{1}{2}\\sum_{i,j} V_{ij} \\eta_i \\eta_j$, where $V_{ij} = \\left.\\frac{\\partial^2 V}{\\partial q_i \\partial q_j}\\right|_{q_0}$ and $\\eta_i = q_i - q_{0,i}$. Kinetic energy is $T \\approx \\frac{1}{2}\\sum_{i,j} T_{ij} \\dot{\\eta}_i \\dot{\\eta}_j$.",
        "level2": "Set up the generalized eigenvalue secular determinant: $\\det(\\mathbf{V} - \\omega^2 \\mathbf{T}) = 0$. Roots $\\omega_k^2$ give the squared normal mode eigenfrequencies.",
        "level3": "Find normal mode eigenvectors $\\vec{a}^{(k)}$ by solving $(\\mathbf{V} - \\omega_k^2 \\mathbf{T})\\vec{a}^{(k)} = 0$. General motion is a linear superposition: $\\vec{\\eta}(t) = \\sum_k C_k \\vec{a}^{(k)} \\cos(\\omega_k t + \\phi_k)$.",
        "level4": "Symmetry check: For symmetric coupled systems (e.g. identical pendula), symmetric mode has $\\eta_1 = \\eta_2$ (spring uncompressed), antisymmetric mode has $\\eta_1 = -\\eta_2$ (spring maximum oscillation)."
    },
    "Collisions & Momentum Conservation": {
        "title": "Collisions, Variable Mass & Momentum Conservation",
        "level1": "In the absence of net external forces ($\\sum \\vec{F}_{\\text{ext}} = 0$), total linear momentum $\\vec{P} = \\sum m_i \\vec{v}_i$ is strictly conserved. In elastic collisions, total kinetic energy is also conserved.",
        "level2": "For variable mass systems (e.g. chain lifted from floor, rocket propulsion): Apply impulse-momentum theorem $\\vec{F}_{\\text{ext}} = \\frac{d\\vec{p}}{dt} = m\\frac{d\\vec{v}}{dt} + \\vec{v}_{\\text{rel}}\\frac{dm}{dt}$.",
        "level3": "In the Center of Mass (CM) frame, total momentum is identically zero ($\\vec{P}_{\\text{CM}} = 0$). For 1D elastic collisions: relative velocity of separation equals negative of relative velocity of approach ($v_{2f} - v_{1f} = -(v_{2i} - v_{1i})$).",
        "level4": "Energy dissipation check: In perfectly inelastic collisions, kinetic energy loss is $\\Delta K = \\frac{1}{2}\\frac{m_1 m_2}{m_1 + m_2}(v_1 - v_2)^2$. Verify that total mechanical energy does not increase."
    },

    # ELECTROMAGNETISM
    "Electrostatics & Boundary Value Problems": {
        "title": "Electrostatics & Boundary Value Problems",
        "level1": "For continuous charge distributions, electric field is $\\vec{E}(\\vec{r}) = \\frac{1}{4\\pi\\epsilon_0}\\int \\frac{\\rho(\\vec{r}')(\\vec{r} - \\vec{r}')}{|\\vec{r} - \\vec{r}'|^3} d^3 r'$. On symmetry axes (rings, disks), transverse components cancel by parity.",
        "level2": "Apply Gauss's Law $\\oint \\vec{E} \\cdot d\\vec{A} = \\frac{Q_{\\text{enc}}}{\\epsilon_0}$ for spherical, cylindrical, or planar symmetries. Electric potential satisfies Laplace equation $\\nabla^2 V = 0$ in charge-free regions and Poisson $\\nabla^2 V = -\\rho/\\epsilon_0$.",
        "level3": "Boundary conditions at conductor surfaces: $E_{\\parallel} = 0$, $E_{\\perp} = \\frac{\\sigma}{\\epsilon_0}$. For Method of Images with a grounded sphere of radius $R$ and charge $q$ at $d > R$: image charge $q' = -q\\frac{R}{d}$ is located at distance $d' = \\frac{R^2}{d}$.",
        "level4": "Asymptotic dipole and monopole checks: Far from any bounded charge distribution ($r \\gg R$), potential approaches $V(r) \\to \\frac{Q_{\\text{net}}}{4\\pi\\epsilon_0 r} + \\frac{\\vec{p}\\cdot\\hat{r}}{4\\pi\\epsilon_0 r^2}$. Verify units: $[E] = \\text{V/m} = \\text{N/C}$."
    },
    "Capacitors & Dielectric Media": {
        "title": "Dielectrics, Polarization & Capacitance",
        "level1": "In linear dielectric media: electric displacement is $\\vec{D} = \\epsilon_0 \\vec{E} + \\vec{P} = \\epsilon_r \\epsilon_0 \\vec{E} = \\epsilon \\vec{E}$. Gauss's law for displacement depends only on free charges: $\\oint \\vec{D} \\cdot d\\vec{A} = Q_{\\text{free, enc}}$.",
        "level2": "Bound charge densities: volume charge $\\rho_b = -\\nabla \\cdot \\vec{P}$ and surface charge $\\sigma_b = \\vec{P} \\cdot \\hat{n}$. Capacitance is $C = \\frac{Q_{\\text{free}}}{V}$. Energy stored is $U = \\frac{1}{2} C V^2 = \\frac{1}{2}\\int \\vec{D}\\cdot\\vec{E} d^3 r$.",
        "level3": "Boundary conditions across dielectric interfaces: normal displacement discontinuity $\\Delta D_{\\perp} = \\sigma_{\\text{free}}$ and tangential field continuity $\\Delta E_{\\parallel} = 0$.",
        "level4": "Dielectric force check: Force on a partially inserted dielectric slab with constant voltage is $F = +\\frac{1}{2}V^2 \\frac{dC}{dx}$ (attractive into capacitor), whereas at constant charge $F = -\\frac{1}{2}Q^2 \\frac{d(1/C)}{dx}$."
    },
    "Magnetostatics & Magnetic Fields": {
        "title": "Magnetostatics & Vector Potential",
        "level1": "Magnetic field produced by steady currents $\\vec{J}$ follows Biot-Savart law: $\\vec{B}(\\vec{r}) = \\frac{\\mu_0}{4\\pi}\\int \\frac{\\vec{J}(\\vec{r}') \\times (\\vec{r}-\\vec{r}')}{|\\vec{r}-\\vec{r}'|^3} d^3 r'$ or Ampère's Law $\\oint \\vec{B}\\cdot d\\vec{\\ell} = \\mu_0 I_{\\text{enc}}$.",
        "level2": "Magnetic vector potential $\\vec{A}$ satisfies $\\vec{B} = \\nabla \\times \\vec{A}$ and $\\nabla \\cdot \\vec{A} = 0$ (Coulomb gauge), leading to Poisson equation $\\nabla^2 \\vec{A} = -\\mu_0 \\vec{J}$.",
        "level3": "Magnetic dipole moment of planar current loop: $\\vec{m} = I \\vec{S}$. Torque in external field is $\\vec{\\tau} = \\vec{m} \\times \\vec{B}$ and potential energy is $U = -\\vec{m}\\cdot\\vec{B}$. Field of magnetic dipole is $\\vec{B}(\\vec{r}) = \\frac{\\mu_0}{4\\pi r^3}[3(\\vec{m}\\cdot\\hat{r})\\hat{r} - \\vec{m}]$.",
        "level4": "Boundary conditions: $\\Delta B_{\\perp} = 0$ and $\\Delta B_{\\parallel} = \\mu_0 K \\times \\hat{n}$. In magnetized materials: $\\vec{H} = \\frac{\\vec{B}}{\\mu_0} - \\vec{M}$ with $\\oint \\vec{H}\\cdot d\\vec{\\ell} = I_{\\text{free, enc}}$."
    },
    "Electromagnetic Induction & Faraday": {
        "title": "Faraday's Law & Electromagnetic Induction",
        "level1": "Faraday-Lenz Law: Induced electromotive force equals negative time rate of magnetic flux: $\\mathcal{E} = -\\frac{d\\Phi_B}{dt} = -\\frac{d}{dt}\\int \\vec{B}\\cdot d\\vec{A}$. In differential form: $\\nabla \\times \\vec{E} = -\\frac{\\partial\\vec{B}}{\\partial t}$.",
        "level2": "Motional EMF for conductors moving with velocity $\\vec{v}$ in magnetic field: $\\mathcal{E} = \\oint (\\vec{v} \\times \\vec{B})\\cdot d\\vec{\\ell}$. Induced current is $I = \\mathcal{E}/R$ creating magnetic braking force $\\vec{F} = I \\vec{L} \\times \\vec{B}$.",
        "level3": "Self-inductance $L = \\frac{N\\Phi_B}{I}$ and mutual inductance $M_{12} = \\frac{N_2\\Phi_{21}}{I_1}$. Stored magnetic energy is $U_B = \\frac{1}{2} L I^2 = \\frac{1}{2\\mu_0}\\int B^2 d^3 r$.",
        "level4": "Lenz's Law check: The induced current always opposes the change in flux that produced it. Check RL time constant $\\tau = L/R$."
    },
    "Maxwell Equations & EM Waves": {
        "title": "Maxwell's Equations, Poynting Vector & EM Waves",
        "level1": "Maxwell's equations in vacuum: $\\nabla\\cdot\\vec{E}=0$, $\\nabla\\cdot\\vec{B}=0$, $\\nabla\\times\\vec{E}=-\\frac{\\partial\\vec{B}}{\\partial t}$, $\\nabla\\times\\vec{B}=\\mu_0\\epsilon_0\\frac{\\partial\\vec{E}}{\\partial t}$. Wave equation yields speed of light $c = 1/\\sqrt{\\mu_0\\epsilon_0}$.",
        "level2": "Plane wave relations: $\\vec{E}(\\vec{r},t) = \\vec{E}_0 e^{i(\\vec{k}\\cdot\\vec{r} - \\omega t)}$, with $\\vec{B} = \\frac{1}{\\omega}(\\vec{k} \\times \\vec{E})$ so $\\vec{E} \\perp \\vec{B} \\perp \\vec{k}$ and $|\vec{E}| = c|\\vec{B}|$.",
        "level3": "Energy flux given by Poynting Vector $\\vec{S} = \\frac{1}{\\mu_0}(\\vec{E} \\times \\vec{B})$. Time-averaged intensity is $\\langle S \\rangle = \\frac{1}{2}\\epsilon_0 c |E_0|^2$. Energy density is $u = \\frac{1}{2}\\epsilon_0 E^2 + \\frac{1}{2\\mu_0} B^2 = \\epsilon_0 E^2$.",
        "level4": "Radiation pressure: For total absorption $P_{\\text{rad}} = \\frac{\\langle S \\rangle}{c}$, for perfect reflection $P_{\\text{rad}} = \\frac{2\\langle S \\rangle}{c}$. Check refractive index $n = \\sqrt{\\epsilon_r \\mu_r}$ and Snell's law $n_1 \\sin\\theta_1 = n_2 \\sin\\theta_2$."
    },

    # QUANTUM MECHANICS
    "Harmonic Oscillator & Ladder Operators": {
        "title": "Quantum Harmonic Oscillator & Ladder Operators",
        "level1": "Hamiltonian in operator form: $\\hat{H} = \\frac{\\hat{p}^2}{2m} + \\frac{1}{2}m\\omega^2\\hat{x}^2 = \\hbar\\omega\\left(\\hat{a}^\\dagger\\hat{a} + \\frac{1}{2}\\right)$. Energy eigenvalues are $E_n = \\hbar\\omega\\left(n + \\frac{1}{2}\\right)$ for $n = 0, 1, 2, \\dots$.",
        "level2": "Ladder operator algebra: $\\hat{a} = \\sqrt{\\frac{m\\omega}{2\\hbar}}\\hat{x} + \\frac{i}{\\sqrt{2m\\omega\\hbar}}\\hat{p}$ and $\\hat{a}^\\dagger = \\sqrt{\\frac{m\\omega}{2\\hbar}}\\hat{x} - \\frac{i}{\\sqrt{2m\\omega\\hbar}}\\hat{p}$, with commutator $[\\hat{a}, \\hat{a}^\\dagger] = 1$.",
        "level3": "Action on number eigenstates: $\\hat{a}|n\\rangle = \\sqrt{n}|n-1\\rangle$, $\\hat{a}^\\dagger|n\\rangle = \\sqrt{n+1}|n+1\\rangle$, and number operator $\\hat{N}|n\\rangle = n|n\\rangle$. Express position and momentum: $\\hat{x} = \\sqrt{\\frac{\\hbar}{2m\\omega}}(\\hat{a} + \\hat{a}^\\dagger)$ and $\\hat{p} = i\\sqrt{\\frac{m\\omega\\hbar}{2}}(\\hat{a}^\\dagger - \\hat{a})$.",
        "level4": "Expectation values: $\\langle n|\\hat{x}|n\\rangle = 0$, $\\langle n|\\hat{p}|n\\rangle = 0$, $\\langle n|\\hat{x}^2|n\\rangle = \\frac{\\hbar}{2m\\omega}(2n+1)$, verifying virial theorem $\\langle T \\rangle = \\langle V \\rangle = \\frac{1}{2}E_n$."
    },
    "Dirac Formalism & Hilbert Space": {
        "title": "Dirac Bra-Ket Formalism & Observable Operators",
        "level1": "States are vectors $|\\psi\\rangle$ in Hilbert space with inner product $\\langle\\phi|\\psi\\rangle = \\langle\\psi|\\phi\\rangle^*$. Physical observables correspond to Hermitian operators $\\hat{A} = \\hat{A}^\\dagger$ with real eigenvalues $a_n$ and orthonormal eigenbasis $\\sum_n |n\\rangle\\langle n| = \\mathbf{1}$.",
        "level2": "Probability of measuring eigenvalue $a_n$ on state $|\\psi\\rangle$ is $P(a_n) = |\\langle n|\\psi\\rangle|^2$. Expectation value is $\\langle A \\rangle = \\langle\\psi|\\hat{A}|\\psi\\rangle$. Variance is $(\\Delta A)^2 = \\langle A^2 \\rangle - \\langle A \\rangle^2$.",
        "level3": "Generalized Robertson-Schrödinger Uncertainty: $\\Delta A \\Delta B \\geq \\frac{1}{2}|\\langle [\\hat{A}, \\hat{B}] \\rangle|$. Canonical position-momentum commutator $[\\hat{x}_i, \\hat{p}_j] = i\\hbar\\delta_{ij}$ leads to $\\Delta x \\Delta p \\geq \\frac{\\hbar}{2}$.",
        "level4": "Time evolution: In Schrödinger picture, $|\\psi(t)\\rangle = e^{-i\\hat{H}t/\\hbar}|\\psi(0)\\rangle$. In Heisenberg picture, operators evolve via $\\frac{d\\hat{A}}{dt} = \\frac{i}{\\hbar}[\\hat{H}, \\hat{A}] + \\frac{\\partial\\hat{A}}{\\partial t}$ (Ehrenfest Theorem)."
    },
    "Angular Momentum & Spin Algebra": {
        "title": "Angular Momentum & Spin-1/2 Algebra",
        "level1": "Angular momentum commutator algebra: $[\\hat{J}_i, \\hat{J}_j] = i\\hbar \\epsilon_{ijk}\\hat{J}_k$. Simultaneous eigenbasis $|j, m\\rangle$ satisfies $\\hat{J}^2|j, m\\rangle = \\hbar^2 j(j+1)|j, m\\rangle$ and $\\hat{J}_z|j, m\\rangle = \\hbar m|j, m\\rangle$, with $-j \\leq m \\leq j$.",
        "level2": "Ladder operators $\\hat{J}_\\pm = \\hat{J}_x \\pm i\\hat{J}_y$ act as $\\hat{J}_\\pm|j, m\\rangle = \\hbar\\sqrt{j(j+1) - m(m\\pm 1)}|j, m\\pm 1\\rangle$.",
        "level3": "For spin-1/2 ($s=1/2$): $\\vec{S} = \\frac{\\hbar}{2}\\vec{\\sigma}$, where Pauli matrices are $\\sigma_x = \\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$, $\\sigma_y = \\begin{pmatrix}0&-i\\\\i&0\\end{pmatrix}$, $\\sigma_z = \\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}$. Note $\\sigma_i^2 = \\mathbf{1}$ and $\\{\\sigma_i, \\sigma_j\\} = 2\\delta_{ij}$.",
        "level4": "Addition of angular momenta $j_1 \\otimes j_2$: Total angular momentum takes values $|j_1 - j_2| \\leq J \\leq j_1 + j_2$ in integer steps. Singlet state ($J=0$) is antisymmetric $\\frac{1}{\\sqrt{2}}(|\\uparrow\\downarrow\\rangle - |\\downarrow\\uparrow\\rangle)$, triplet ($J=1$) is symmetric."
    },
    "Perturbation Theory & Approximations": {
        "title": "Time-Independent Perturbation Theory",
        "level1": "For $\\hat{H} = \\hat{H}_0 + \\hat{H}'$ with known unperturbed eigensystem $\\hat{H}_0|n^{(0)}\\rangle = E_n^{(0)}|n^{(0)}\\rangle$: 1st-order energy correction is the expectation value of the perturbation: $E_n^{(1)} = \\langle n^{(0)}|\\hat{H}'|n^{(0)}\\rangle$.",
        "level2": "2nd-order energy correction: $E_n^{(2)} = \\sum_{k \\neq n} \\frac{|\\langle k^{(0)}|\\hat{H}'|n^{(0)}\\rangle|^2}{E_n^{(0)} - E_k^{(0)}}$. For the ground state ($n=0$), the denominator is always negative, so $E_0^{(2)} \\leq 0$ strictly decreases.",
        "level3": "1st-order state correction: $|n^{(1)}\\rangle = \\sum_{k \\neq n} \\frac{\\langle k^{(0)}|\\hat{H}'|n^{(0)}\\rangle}{E_n^{(0)} - E_k^{(0)}} |k^{(0)}\\rangle$.",
        "level4": "Degenerate Perturbation Theory: If $E_a^{(0)} = E_b^{(0)}$, diagonalize the perturbation matrix $W_{ij} = \\langle i^{(0)}|\\hat{H}'|j^{(0)}\\rangle$ within the degenerate subspace before computing energy shifts to lift degeneracy."
    },

    # THERMODYNAMICS & STATISTICAL PHYSICS
    "1st & 2nd Laws / Thermodynamic Cycles": {
        "title": "Thermodynamic Laws & Cycles",
        "level1": "1st Law: $dU = \\delta Q - \\delta W$. For quasi-static processes: $dU = TdS - pdV + \\mu dN$. Work done by gas is $W = \\int p dV$.",
        "level2": "2nd Law: Efficiency of any heat engine operating between $T_H$ and $T_C$ is $\\eta = \\frac{W}{Q_H} = 1 - \\frac{Q_C}{Q_H} \\leq \\eta_{\\text{Carnot}} = 1 - \\frac{T_C}{T_H}$. For a refrigerator, COP is $\\beta = \\frac{Q_C}{W} \\leq \\frac{T_C}{T_H - T_C}$.",
        "level3": "Ideal gas adiabatic relation ($dQ=0$): $p V^\\gamma = \\text{const}$, $T V^{\\gamma-1} = \\text{const}$, where $\\gamma = C_p/C_v = 1 + 2/d$ ($d=3 \\implies \\gamma = 5/3$, $d=5 \\implies \\gamma = 7/5$).",
        "level4": "Entropy changes: $\\Delta S = \\int \\frac{dQ_{\\text{rev}}}{T}$. For ideal gas: $\\Delta S = C_v \\ln(T_f/T_i) + nR \\ln(V_f/V_i)$. In an isolated system, $\\Delta S_{\\text{univ}} \\geq 0$ strictly."
    },
    "Canonical & Microcanonical Ensembles": {
        "title": "Statistical Ensembles & Partition Functions",
        "level1": "Microcanonical ensemble: isolated system $(E, V, N)$ with entropy $S = k_B \\ln \\Omega(E)$. Temperature defined via $\\frac{1}{T} = \\left(\\frac{\\partial S}{\\partial E}\\right)_{V,N}$.",
        "level2": "Canonical ensemble: system at fixed $(T, V, N)$. Boltzmann probability $P_i = \\frac{e^{-\\beta E_i}}{Z}$, with canonical partition function $Z = \\sum_i e^{-\\beta E_i}$ where $\\beta = 1/(k_B T)$. Helmholtz free energy is $F = -k_B T \\ln Z$.",
        "level3": "Mean energy and fluctuations: $\\langle E \\rangle = -\\frac{\\partial \\ln Z}{\\partial \\beta} = k_B T^2 \\frac{\\partial \\ln Z}{\\partial T}$. Heat capacity $C_v = \\left(\\frac{\\partial \\langle E \\rangle}{\\partial T}\\right)_V = \\frac{(\\Delta E)^2}{k_B T^2} \\geq 0$.",
        "level4": "Equipartition Theorem: Every quadratic degree of freedom in the classical Hamiltonian contributes $\\frac{1}{2}k_B T$ to mean energy and $\\frac{1}{2}k_B$ to heat capacity."
    },
    "Quantum Gases (Fermi-Dirac & Bose-Einstein)": {
        "title": "Quantum Gases (Fermi-Dirac & Bose-Einstein)",
        "level1": "Mean occupation number of single-particle energy level $\\epsilon_i$: $\\bar{n}_i = \\frac{1}{e^{\\beta(\\epsilon_i - \\mu)} \\pm 1}$, where $(+)$ is Fermi-Dirac (fermions, spin half-integer) and $(-)$ is Bose-Einstein (bosons, spin integer).",
        "level2": "Degenerate Fermi Gas ($T \\to 0$): $\\bar{n}(\\epsilon) = 1$ for $\\epsilon \\leq E_F$ and $0$ for $\\epsilon > E_F$. Fermi energy in 3D: $E_F = \\frac{\\hbar^2}{2m}(3\\pi^2 n)^{2/3}$. Electronic heat capacity is linear: $C_V = \\frac{\\pi^2}{2} N k_B \\left(\\frac{T}{T_F}\\right)$.",
        "level3": "Bose-Einstein Condensation (BEC): Below critical temperature $T_c \\propto \\frac{\\hbar^2}{m k_B} n^{2/3}$, macroscopic fraction $N_0/N = 1 - (T/T_c)^{3/2}$ condenses into zero-momentum ground state.",
        "level4": "Blackbody photon gas (chemical potential $\\mu = 0$): Planck radiation law $u(\\omega) d\\omega = \\frac{\\hbar}{\\pi^2 c^3}\\frac{\\omega^3}{e^{\\beta\\hbar\\omega} - 1} d\\omega$, leading to Stefan-Boltzmann law $U = a V T^4$ and pressure $P = \\frac{1}{3}u$."
    },

    # MODERN PHYSICS
    "Special Relativity & Lorentz Transformations": {
        "title": "Special Relativity & 4-Vectors",
        "level1": "Einstein postulates: Speed of light $c$ is constant in all inertial frames. Lorentz boost along $x$: $x' = \\gamma(x - vt)$, $t' = \\gamma(t - vx/c^2)$, where $\\gamma = 1/\\sqrt{1 - v^2/c^2}$.",
        "level2": "Time dilation $\\Delta t = \\gamma \\Delta t_0$ (moving clocks run slow) and length contraction $L = L_0/\\gamma$ (moving rods shorten along motion axis). Spacetime invariant interval: $s^2 = c^2 \\Delta t^2 - \\Delta x^2 - \\Delta y^2 - \\Delta z^2$.",
        "level3": "Relativistic 4-momentum $P^\\mu = (E/c, \\vec{p}) = (\\gamma m c, \\gamma m \\vec{v})$. Invariant mass relation: $P^\\mu P_\\mu = \\frac{E^2}{c^2} - p^2 = m^2 c^2 \\implies E^2 = p^2 c^2 + m^2 c^4$.",
        "level4": "Relativistic Doppler effect for source moving with velocity $v$: longitudinal frequency shift $\\nu = \\nu_0 \\sqrt{\\frac{1 - v/c}{1 + v/c}}$ (receding) or $\\nu = \\nu_0 \\sqrt{\\frac{1 + v/c}{1 - v/c}}$ (approaching)."
    }
}


def get_physics_clues(area, subtopic, question_id, text=""):
    """Returns dynamic, context-specific clues tailored to the exact subtopic and physical phenomenon."""
    # Look for matching subtopic in knowledge base
    if subtopic in HINT_KNOWLEDGE_BASE:
        return HINT_KNOWLEDGE_BASE[subtopic]
        
    # Search by keywords if exact subtopic not found
    for sub_key, kb in HINT_KNOWLEDGE_BASE.items():
        if sub_key.lower() in subtopic.lower() or subtopic.lower() in sub_key.lower():
            return kb

    # Fallback to Area-level physics guidance
    area_fallbacks = {
        "Mecânica Clássica": HINT_KNOWLEDGE_BASE["Lagrangian Mechanics & Constraints"],
        "Eletromagnetismo": HINT_KNOWLEDGE_BASE["Electrostatics & Boundary Value Problems"],
        "Mecânica Quântica": HINT_KNOWLEDGE_BASE["Dirac Formalism & Hilbert Space"],
        "Termodinâmica": HINT_KNOWLEDGE_BASE["1st & 2nd Laws / Thermodynamic Cycles"],
        "Física Estatística": HINT_KNOWLEDGE_BASE["Canonical & Microcanonical Ensembles"],
        "Física Moderna": HINT_KNOWLEDGE_BASE["Special Relativity & Lorentz Transformations"],
    }
    
    return area_fallbacks.get(area, HINT_KNOWLEDGE_BASE["Lagrangian Mechanics & Constraints"])
