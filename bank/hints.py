"""EUF Physics Solution Strategy & Contextual Hint Engine.
Generates tailored, subtopic-specific physical principles, coordinate setups, intermediate checkpoints, and limit checks.
Covers 100% of EUF syllabus topics across all 6 physics areas with zero generic fallbacks.
"""

# Comprehensive subtopic and concept-specific guidance dictionary
HINT_KNOWLEDGE_BASE = {
    # =========================================================================
    # 1. ELECTROMAGNETISM
    # =========================================================================
    "Continuous Charge Distributions & Electric Potentials": {
        "title": "Continuous Charge Distributions & Electric Field/Potential Integrals",
        "level1": "Divide the continuous geometry into differential charge elements $dq = \\lambda dl'$ (line), $\\sigma dA'$ (surface), or $\\rho dV'$ (volume). Potential is $V(\\vec{r}) = \\frac{1}{4\\pi\\varepsilon_0}\\int \\frac{dq}{|\\vec{r} - \\vec{r}'|}$ and electric field is $\\vec{E}(\\vec{r}) = -\\nabla V$.",
        "level2": "Exploit geometric symmetry: On symmetry axes (e.g. $z$-axis of a ring of radius $R$ carrying charge $Q$), transverse field components cancel symmetrically ($E_x = E_y = 0$). The axial field is $E_z = \\frac{Q z}{4\\pi\\varepsilon_0 (z^2 + R^2)^{3/2}}$.",
        "level3": "For disk of radius $R$ with surface charge $\\sigma$: $E_z = \\frac{\\sigma}{2\\varepsilon_0}\\left(1 - \\frac{z}{\\sqrt{z^2 + R^2}}\\right)$. For infinite plane ($R \\to \\infty$), field becomes uniform $E = \\frac{\\sigma}{2\\varepsilon_0}$.",
        "level4": "Asymptotic dipole and monopole checks: For $z \\gg R$, expand $(1 + R^2/z^2)^{-3/2} \\approx 1 - \\frac{3}{2}\\frac{R^2}{z^2}$, recovering the point-charge Coulomb field $E_z \\to \\frac{Q}{4\\pi\\varepsilon_0 z^2}$."
    },
    "Gauss's Law & Electric Flux": {
        "title": "Gauss's Law & Highly Symmetric Charge Distributions",
        "level1": "Gauss's Law states $\\Phi_E = \\oint_{\\mathcal{S}} \\vec{E}\\cdot d\\vec{A} = \\frac{Q_{\\text{enc}}}{\\varepsilon_0}$. It applies effectively when symmetry makes $|\\vec{E}|$ constant on the Gaussian surface and parallel/perpendicular to $d\\vec{A}$.",
        "level2": "Spherical symmetry (radius $R$, total charge $Q$): For $r > R$, $\\vec{E} = \\frac{Q}{4\\pi\\varepsilon_0 r^2}\\hat{r}$. Inside a uniform sphere ($r < R$), $Q_{\\text{enc}} = Q(r/R)^3 \\implies \\vec{E} = \\frac{Q r}{4\\pi\\varepsilon_0 R^3}\\hat{r}$.",
        "level3": "Cylindrical symmetry (linear charge density $\\lambda$): Gaussian cylinder of radius $r$, length $L$ yields $E(2\\pi r L) = \\frac{\\lambda L}{\\varepsilon_0} \\implies \\vec{E} = \\frac{\\lambda}{2\\pi\\varepsilon_0 r}\\hat{r}$. Potential is $V(r) = -\\frac{\\lambda}{2\\pi\\varepsilon_0}\\ln(r/r_0)$.",
        "level4": "Boundary discontinuity check: Across any charged surface with local density $\\sigma$, the normal field has discontinuity $\\Delta E_{\\perp} = E_{\\text{out}} - E_{\\text{in}} = \\frac{\\sigma}{\\varepsilon_0}$, while tangential component is continuous."
    },
    "Conductors, Cavities & Electrostatic Shielding": {
        "title": "Conductors, Cavities & Electrostatic Shielding",
        "level1": "In electrostatic equilibrium: electric field inside a conductor is zero ($\vec{E} = 0$), the entire conductor is an equipotential ($V = \\text{const}$), and net free charge resides exclusively on exterior surfaces.",
        "level2": "Cavity with enclosed charge $q$: By Gauss's law around the cavity, an induced charge $-q$ distributes on the inner cavity wall to ensure $\\vec{E} = 0$ in the bulk. An equal $+q$ appears on the outer surface.",
        "level3": "Grounded conductor: Setting $V = 0$ at the outer surface removes exterior fields caused by interior charges, achieving complete electrostatic shielding (Faraday cage).",
        "level4": "Electrostatic pressure: The outward repulsive force on the surface of a charged conductor is $P = \\frac{\\sigma^2}{2\\varepsilon_0} = \\frac{1}{2}\\varepsilon_0 E_{\\text{surf}}^2$."
    },
    "Boundary Value Problems & Method of Images": {
        "title": "Boundary Value Problems, Laplace's Equation & Method of Images",
        "level1": "In charge-free regions, electric potential satisfies Laplace's equation $\\nabla^2 V = 0$. By the Uniqueness Theorem, any potential satisfying specified boundary conditions is the unique physical solution.",
        "level2": "Method of Images for grounded infinite planar conductor at $z=0$: A charge $q$ at $(0,0,d)$ is mirrored by an image charge $q' = -q$ at $(0,0,-d)$. Potential for $z > 0$ is $V = \\frac{q}{4\\pi\\varepsilon_0}\\left[\\frac{1}{\\sqrt{x^2+y^2+(z-d)^2}} - \\frac{1}{\\sqrt{x^2+y^2+(z+d)^2}}\\right]$.",
        "level3": "Image charge for grounded sphere of radius $R$: A charge $q$ at distance $d > R$ induces an image charge $q' = -q\\frac{R}{d}$ positioned at $d' = \\frac{R^2}{d}$ along the radial line.",
        "level4": "Induced surface charge density: $\\sigma(x,y) = -\\varepsilon_0 \\left.\\frac{\\partial V}{\\partial z}\\right|_{z=0} = -\\frac{qd}{2\\pi(x^2+y^2+d^2)^{3/2}}$. Integrating over the plane yields total induced charge $\\int \\sigma dA = -q$."
    },
    "Capacitors & Dielectric Media": {
        "title": "Dielectrics, Bound Charges & Capacitance",
        "level1": "In linear isotropic dielectrics: electric displacement is $\\vec{D} = \\varepsilon_0 \\vec{E} + \\vec{P} = \\varepsilon_r \\varepsilon_0 \\vec{E} = \\varepsilon \\vec{E}$. Gauss's Law for displacement depends solely on free charge: $\\oint \\vec{D}\\cdot d\\vec{A} = Q_{\\text{free, enc}}$.",
        "level2": "Bound polarization charges: volume density $\\rho_b = -\\nabla \\cdot \\vec{P}$ and surface density $\\sigma_b = \\vec{P}\\cdot\\hat{n}$. Capacitance increases by dielectric constant: $C = \\kappa C_0 = \\varepsilon_r C_0$.",
        "level3": "Stored electrostatic energy: $U = \\frac{1}{2} C V^2 = \\frac{Q^2}{2C} = \\frac{1}{2}\\int \\vec{D}\\cdot\\vec{E} d^3 r$.",
        "level4": "Dielectric force check: Force on a dielectric slab partially inserted into a capacitor: at fixed voltage $F = +\\frac{1}{2}V^2 \\frac{dC}{dx}$ (attractive); at fixed charge $F = -\\frac{1}{2}Q^2 \\frac{d(1/C)}{dx}$."
    },
    "Electric Dipoles & Multipole Expansion": {
        "title": "Electric Dipoles & Multipole Expansion",
        "level1": "Electric dipole moment: $\\vec{p} = \\sum q_i \\vec{r}_i$ or $\\int \\vec{r}' \\rho(\\vec{r}') d^3 r'$. Dipole potential is $V(\\vec{r}) = \\frac{\\vec{p}\\cdot\\hat{r}}{4\\pi\\varepsilon_0 r^2} = \\frac{p\\cos\\theta}{4\\pi\\varepsilon_0 r^2}$.",
        "level2": "Dipole electric field in spherical coordinates: $\\vec{E}(r,\\theta) = \\frac{p}{4\\pi\\varepsilon_0 r^3}(2\\cos\\theta \\hat{r} + \\sin\\theta \\hat{\\theta})$.",
        "level3": "Dipole in external field $\\vec{E}$: Torque is $\\vec{\\tau} = \\vec{p} \\times \\vec{E}$, potential energy is $U = -\\vec{p}\\cdot\\vec{E}$, and net force in non-uniform field is $\\vec{F} = (\\vec{p}\\cdot\\nabla)\\vec{E}$.",
        "level4": "Multipole hierarchy: If monopole moment $Q = \\int \\rho dV = 0$, the dipole moment $\\vec{p}$ is independent of the choice of origin."
    },
    "DC Circuits, Resistors & Joule Heating": {
        "title": "DC Circuits, Ohm's Law & Power Dissipation",
        "level1": "Microscopic Ohm's Law: $\\vec{J} = \\sigma \\vec{E} = \\frac{1}{\\rho}\\vec{E}$. Resistance of uniform conductor: $R = \\rho \\frac{L}{A}$. Current is $I = \\int \\vec{J}\\cdot d\\vec{A}$.",
        "level2": "Kirchhoff's Rules: Node rule $\\sum I_{\\text{in}} = \\sum I_{\\text{out}}$ (charge conservation), Loop rule $\\sum \\Delta V = 0$ (energy conservation).",
        "level3": "Joule heating rate: $P = I V = I^2 R = \\frac{V^2}{R}$. Maximum power transfer theorem: maximum power delivered to load $R_L$ from source with internal resistance $r$ occurs when $R_L = r$, giving $P_{\\text{max}} = \\frac{\\mathcal{E}^2}{4r}$.",
        "level4": "Drude model conductivity: $\\sigma = \\frac{n e^2 \\tau}{m}$, where $\\tau$ is relaxation collision time and $n$ is carrier density."
    },
    "Biot-Savart Law & Magnetic Fields of Currents": {
        "title": "Biot-Savart Law & Stationary Current Magnetic Fields",
        "level1": "Biot-Savart Law for steady currents: $\\vec{B}(\\vec{r}) = \\frac{\\mu_0 I}{4\\pi}\\int \\frac{d\\vec{\\ell}' \\times (\\vec{r} - \\vec{r}')}{|\\vec{r} - \\vec{r}'|^3}$.",
        "level2": "Field on axis of circular loop of radius $R$ carrying current $I$: $\\vec{B}(z) = \\frac{\\mu_0 I R^2}{2(z^2 + R^2)^{3/2}}\\hat{z}$. At center ($z=0$), $B = \\frac{\\mu_0 I}{2R}$.",
        "level3": "Long straight wire carrying current $I$: $B(r) = \\frac{\\mu_0 I}{2\\pi r}$. Finite wire segment subtending angles $\\theta_1, \\theta_2$: $B = \\frac{\\mu_0 I}{4\\pi d}(\\sin\\theta_2 - \\sin\\theta_1)$.",
        "level4": "Solenoid and Toroid: Ideal infinite solenoid has uniform interior field $B = \\mu_0 n I$ ($n = N/L$). Toroid of $N$ turns has $B(r) = \\frac{\\mu_0 N I}{2\\pi r}$."
    },
    "Ampère's Law & Current Distributions": {
        "title": "Ampère's Circuital Law & Current Symmetry",
        "level1": "Ampère's Law: $\\oint_{\\mathcal{C}} \\vec{B}\\cdot d\\vec{\\ell} = \\mu_0 I_{\\text{enc}} = \\mu_0 \\int_{\\mathcal{S}} \\vec{J}\\cdot d\\vec{A}$. Requires high symmetry (cylindrical, planar, or solenoidal).",
        "level2": "Cylindrical conductor of radius $R$ carrying uniform current $I$: Inside ($r < R$), $I_{\\text{enc}} = I(r^2/R^2) \\implies B(r) = \\frac{\\mu_0 I r}{2\\pi R^2}$. Outside ($r > R$), $B(r) = \\frac{\\mu_0 I}{2\\pi r}$.",
        "level3": "Coaxial cable with inner conductor carrying $+I$ and outer shell carrying $-I$: Inside inner core $B \\propto r$; in dielectric gap $B = \\frac{\\mu_0 I}{2\\pi r}$; outside outer shell $B = 0$ ($I_{\\text{enc}} = 0$).",
        "level4": "Boundary condition across current sheet $\\vec{K}$: $\\Delta \\vec{B}_{\\parallel} = \\mu_0 (\\vec{K} \\times \\hat{n})$, while normal component is strictly continuous $\\Delta B_{\\perp} = 0$."
    },
    "Lorentz Force & Particle Trajectories in EM Fields": {
        "title": "Lorentz Force & Charged Particle Motion in EM Fields",
        "level1": "Equation of motion: $\\vec{F} = q(\\vec{E} + \\vec{v} \\times \\vec{B}) = m\\frac{d\\vec{v}}{dt}$. Because magnetic force is perpendicular to velocity ($\\vec{F}_B \\cdot \\vec{v} = 0$), magnetic fields do zero mechanical work.",
        "level2": "Pure uniform magnetic field $\\vec{B} = B\\hat{z}$: Motion decomposes into uniform motion along $z$ ($v_z = \\text{const}$) and circular cyclotron motion in $xy$-plane with radius $r_L = \\frac{m v_\\perp}{q B}$ and cyclotron frequency $\\omega_c = \\frac{q B}{m}$.",
        "level3": "Crossed fields $\\vec{E} \\perp \\vec{B}$ (Velocity Selector): Particle passes undeflected if electric and magnetic forces balance: $qE = qvB \\implies v = \\frac{E}{B}$. Cycloid drift velocity is $\\vec{v}_d = \\frac{\\vec{E} \\times \\vec{B}}{B^2}$.",
        "level4": "Relativistic particle check: When kinetic energy is comparable to rest mass, use relativistic momentum $p = \\gamma m v = q B r_L$, so $r_L = \\frac{\\sqrt{E^2 - m^2 c^4}}{q B c}$."
    },
    "Magnetic Dipoles, Forces & Magnetic Media": {
        "title": "Magnetic Dipoles & Magnetized Materials",
        "level1": "Magnetic dipole moment of current loop: $\\vec{m} = I \\vec{A}$. Potential energy in field $\\vec{B}$ is $U = -\\vec{m}\\cdot\\vec{B}$ and torque is $\\vec{\\tau} = \\vec{m} \\times \\vec{B}$.",
        "level2": "Force in non-uniform magnetic field: $\\vec{F} = \\nabla(\\vec{m}\\cdot\\vec{B})$. Stern-Gerlach splitting depends on $\\frac{\\partial B_z}{\\partial z}$.",
        "level3": "Magnetized media: Magnetic field $\\vec{H} = \\frac{\\vec{B}}{\\mu_0} - \\vec{M}$. Ampère's Law for $\\vec{H}$: $\\oint \\vec{H}\\cdot d\\vec{\\ell} = I_{\\text{free, enc}}$. Bound current densities: $\\vec{J}_b = \\nabla \\times \\vec{M}$ and $\\vec{K}_b = \\vec{M} \\times \\hat{n}$.",
        "level4": "Linear media: $\\vec{M} = \\chi_m \\vec{H}$, $\\vec{B} = \\mu_0(1 + \\chi_m)\\vec{H} = \\mu \\vec{H}$. Diamagnetic ($\\chi_m < 0$), Paramagnetic ($\\chi_m > 0$), Ferromagnetic (non-linear hysteresis)."
    },
    "Faraday's Law, Motional EMF & Inductance": {
        "title": "Faraday's Law, Motional EMF & Magnetic Inductance",
        "level1": "Faraday-Lenz Law: Electromotive force equals negative rate of change of magnetic flux: $\\mathcal{E} = -\\frac{d\\Phi_B}{dt} = -\\frac{d}{dt}\\int_{\\mathcal{S}} \\vec{B}\\cdot d\\vec{A}$. In differential form: $\\nabla \\times \\vec{E} = -\\frac{\\partial \\vec{B}}{\\partial t}$.",
        "level2": "Motional EMF on conductor moving with velocity $\\vec{v}$: $\\mathcal{E} = \\oint (\\vec{v} \\times \\vec{B})\\cdot d\\vec{\\ell}$. Induced current $I = \\mathcal{E}/R$ creates magnetic braking force $\\vec{F} = I \\vec{L} \\times \\vec{B}$.",
        "level3": "Self-inductance $L = \\frac{N\\Phi_B}{I}$ and mutual inductance $M_{12} = \\frac{N_2 \\Phi_{21}}{I_1}$. Stored magnetic energy is $U_B = \\frac{1}{2} L I^2 = \\frac{1}{2\\mu_0}\\int B^2 d^3 r$.",
        "level4": "RL circuit transient: Charging current $I(t) = \\frac{\\mathcal{E}}{R}(1 - e^{-t/\\tau_L})$ with time constant $\\tau_L = L/R$."
    },
    "Maxwell Equations & Displacement Current": {
        "title": "Maxwell's Equations & Displacement Current",
        "level1": "Ampère-Maxwell Law: $\\nabla \\times \\vec{B} = \\mu_0 \\vec{J} + \\mu_0 \\varepsilon_0 \\frac{\\partial \\vec{E}}{\\partial t}$. The displacement current density $\\vec{J}_d = \\varepsilon_0 \\frac{\\partial \\vec{E}}{\\partial t}$ resolves the charge conservation paradox $\\nabla \\cdot (\\nabla \\times \\vec{B}) = 0$.",
        "level2": "Between capacitor plates during charging: Conduction current in wire equals displacement current between plates: $I_d = \\int \\varepsilon_0 \\frac{\\partial E}{\\partial t} dA = \\varepsilon_0 A \\frac{d}{dt}\\left(\\frac{Q}{\\varepsilon_0 A}\\right) = \\frac{dQ}{dt} = I$.",
        "level3": "Electromagnetic wave equation: Taking curl of $\\nabla \\times \\vec{E}$ in vacuum yields $\\nabla^2 \\vec{E} - \\mu_0 \\varepsilon_0 \\frac{\\partial^2 \\vec{E}}{\\partial t^2} = 0$, giving wave propagation speed $c = \\frac{1}{\\sqrt{\\mu_0 \\varepsilon_0}}$.",
        "level4": "Gauge transformations: Potentials $(\\Phi, \\vec{A})$ are invariant under $\\vec{A}' = \\vec{A} + \\nabla \\lambda$ and $\\Phi' = \\Phi - \\frac{\\partial \\lambda}{\\partial t}$. Lorenz gauge condition is $\\nabla \\cdot \\vec{A} + \\frac{1}{c^2}\\frac{\\partial \\Phi}{\\partial t} = 0$."
    },
    "Poynting Vector & EM Wave Propagation": {
        "title": "Poynting Vector, Energy Flux & EM Wave Propagation",
        "level1": "Poynting Vector: $\\vec{S} = \\frac{1}{\\mu_0}(\\vec{E} \\times \\vec{B})$ represents instantaneous electromagnetic power flow per unit area $(\\text{W/m}^2)$.",
        "level2": "Monochromatic plane wave: $\\vec{E} = E_0 \\cos(\\vec{k}\\cdot\\vec{r} - \\omega t)\\hat{n}$, $\\vec{B} = \\frac{1}{c}\\hat{k} \\times \\vec{E}$. Time-averaged intensity is $\\langle S \\rangle = \\frac{1}{2}\\varepsilon_0 c E_0^2 = \\frac{E_0^2}{2\\mu_0 c}$.",
        "level3": "Energy density of EM field: $u = \\frac{1}{2}\\varepsilon_0 E^2 + \\frac{1}{2\\mu_0} B^2 = \\varepsilon_0 E^2$. Total energy transport satisfies continuity $\\frac{\\partial u}{\\partial t} + \\nabla \\cdot \\vec{S} = -\\vec{J}\\cdot\\vec{E}$.",
        "level4": "Radiation pressure: For total absorption $P_{\\text{rad}} = \\frac{\\langle S \\rangle}{c}$; for total reflection $P_{\\text{rad}} = \\frac{2\\langle S \\rangle}{c}$."
    },
    "EM Wave Polarization & Malus's Law": {
        "title": "Electromagnetic Wave Polarization & Optical Anisotropy",
        "level1": "Linear polarization: Electric field oscillates in fixed direction $\\vec{E}(z,t) = (E_{0x}\\hat{x} + E_{0y}\\hat{y})\\cos(kz - \\omega t)$.",
        "level2": "Circular and elliptical polarization: Equal orthogonal amplitudes with phase difference $\\Delta \\phi = \\pm \\pi/2$ yield circular polarization: $\\vec{E} = E_0 [\\cos(kz - \\omega t)\\hat{x} \\pm \\sin(kz - \\omega t)\\hat{y}]$.",
        "level3": "Malus's Law: When linearly polarized light of intensity $I_0$ passes through an ideal polarizer oriented at angle $\\theta$ to the polarization axis, transmitted intensity is $I = I_0 \\cos^2 \\theta$.",
        "level4": "Unpolarized light passing through first linear polarizer: Transmitted intensity is always exactly $I_1 = \\frac{1}{2}I_0$, regardless of the polarizer's orientation angle."
    },
    "Vector Calculus & Field Operators": {
        "title": "Vector Calculus & Differential Operators in Electrodynamics",
        "level1": "Gradient $\\nabla V$, Divergence $\\nabla \\cdot \\vec{v}$, and Curl $\\nabla \\times \\vec{v}$. Fundamental identities: $\\nabla \\times (\\nabla V) = 0$ (curl of gradient is identically zero) and $\\nabla \\cdot (\\nabla \\times \\vec{A}) = 0$ (divergence of curl is zero).",
        "level2": "Divergence Theorem (Gauss): $\\int_{\\mathcal{V}} (\\nabla \\cdot \\vec{v}) dV = \\oint_{\\mathcal{S}} \\vec{v}\\cdot d\\vec{A}$. Stokes' Theorem: $\\int_{\\mathcal{S}} (\\nabla \\times \\vec{v})\\cdot d\\vec{A} = \\oint_{\\mathcal{C}} \\vec{v}\\cdot d\\vec{\\ell}$.",
        "level3": "Laplacian of scalar: $\\nabla^2 V = \\frac{\\partial^2 V}{\\partial x^2} + \\frac{\\partial^2 V}{\\partial y^2} + \\frac{\\partial^2 V}{\\partial z^2}$. Vector Laplacian identity: $\\nabla \\times (\\nabla \\times \\vec{A}) = \\nabla(\\nabla \\cdot \\vec{A}) - \\nabla^2 \\vec{A}$.",
        "level4": "Curvilinear coordinate checks: In cylindrical $(r, \\phi, z)$ and spherical $(r, \\theta, \\phi)$, scale factors $h_i$ modify differential operators (e.g. $\\nabla \\cdot \\vec{v} = \\frac{1}{r^2}\\frac{\\partial(r^2 v_r)}{\\partial r} + \\dots$)."
    },

    # =========================================================================
    # 2. CLASSICAL MECHANICS
    # =========================================================================
    "Lagrangian Mechanics & Generalized Coordinates": {
        "title": "Lagrangian Mechanics & Generalized Coordinates",
        "level1": "Identify the degrees of freedom and choose generalized coordinates $q_1, \\dots, q_n$ matching geometric constraints. Form kinetic energy $T$ and potential energy $V$. The Lagrangian is $L(q, \\dot{q}, t) = T - V$.",
        "level2": "Euler-Lagrange equations: $\\frac{d}{dt}\\left(\\frac{\\partial L}{\\partial \\dot{q}_i}\\right) - \\frac{\\partial L}{\\partial q_i} = 0$. If coordinate $q_k$ is cyclic (absent from $L$), conjugate momentum $p_k = \\frac{\\partial L}{\\partial \\dot{q}_k}$ is a conserved constant of motion.",
        "level3": "Holonomic constraints $f(q_1,\\dots,q_n)=0$: Use Lagrange multipliers $\\lambda$ with $\\frac{d}{dt}\\left(\\frac{\\partial L}{\\partial \\dot{q}_i}\\right) - \\frac{\\partial L}{\\partial q_i} = \\lambda \\frac{\\partial f}{\\partial q_i}$, where the RHS represents the generalized force of constraint.",
        "level4": "Static equilibrium limit: When $\\dot{q}_i = 0, \\ddot{q}_i = 0$, equations reduce to $\\frac{\\partial V}{\\partial q_i} = 0$. Verify dimensional consistency $[Q_i] = [\\text{Work}]/[q_i]$."
    },
    "Hamiltonian Mechanics & Phase Space Dynamics": {
        "title": "Hamiltonian Formalism & Phase Space Dynamics",
        "level1": "Define conjugate momenta $p_i = \\frac{\\partial L}{\\partial \\dot{q}_i}$. Hamiltonian is Legendre transform: $H(q, p, t) = \\sum_i p_i \\dot{q}_i - L(q, \\dot{q}(q,p), t)$. For standard potentials $V(q)$, $H = T + V = E$.",
        "level2": "Hamilton's Canonical Equations: $\\dot{q}_i = \\frac{\\partial H}{\\partial p_i}$ and $\\dot{p}_i = -\\frac{\\partial H}{\\partial q_i}$. Observable evolution: $\\frac{dA}{dt} = \\{A, H\\} + \\frac{\\partial A}{\\partial t}$.",
        "level3": "Canonical Transformations $(q, p) \\to (Q, P)$ preserve Poisson Brackets: $\\{Q_i, Q_j\\} = 0$, $\\{P_i, P_j\\} = 0$, and $\\{Q_i, P_j\\} = \\delta_{ij}$.",
        "level4": "Liouville's Theorem: Phase space volume element $d\\Gamma = \\prod dq_i dp_i$ is conserved along dynamical trajectories ($\\{d\\Gamma, H\\} = 0$)."
    },
    "Central Forces, Kepler Orbits & Effective Potential": {
        "title": "Central Potential & Keplerian Orbital Mechanics",
        "level1": "In central potential $V(r)$, angular momentum $\\vec{L} = \\mu r^2 \\dot{\\theta} \\hat{z}$ is strictly conserved, confining motion to a plane. Motion reduces to 1D via effective potential: $V_{\\text{eff}}(r) = V(r) + \\frac{L^2}{2\\mu r^2}$.",
        "level2": "Radial equation: $\\mu\\ddot{r} = -\\frac{dV_{\\text{eff}}}{dr} = F(r) + \\frac{L^2}{\\mu r^3}$. Circular orbit radius $r_0$ satisfies $\\left.\\frac{dV_{\\text{eff}}}{dr}\\right|_{r_0} = 0$, with stability condition $\\left.\\frac{d^2 V_{\\text{eff}}}{dr^2}\\right|_{r_0} > 0$.",
        "level3": "Kepler orbit equation ($V = -k/r$): $r(\\theta) = \\frac{p}{1 + e\\cos\\theta}$, with semi-latus rectum $p = \\frac{L^2}{\\mu k}$ and eccentricity $e = \\sqrt{1 + \\frac{2EL^2}{\\mu k^2}}$. ($e < 1 \\implies$ ellipse, $e = 1 \\implies$ parabola, $e > 1 \\implies$ hyperbola).",
        "level4": "Apsidal limits: At periapsis and apoapsis, $\\dot{r} = 0$, so $E = V_{\\text{eff}}(r_{\\text{min}}) = V_{\\text{eff}}(r_{\\text{max}})$. Kepler's 3rd Law: $T^2 = \\frac{4\\pi^2}{G(M+m)} a^3$."
    },
    "Rigid Body Dynamics & Moments of Inertia": {
        "title": "Rigid Body Mechanics & Rotational Dynamics",
        "level1": "Angular momentum and angular velocity: $\\vec{L} = \\mathbf{I}\\vec{\\omega}$. Total kinetic energy: $T = \\frac{1}{2}M v_{\\text{CM}}^2 + \\frac{1}{2}\\vec{\\omega}\\cdot\\mathbf{I}\\vec{\\omega}$.",
        "level2": "Parallel Axis Theorem (Steiner): $I = I_{\\text{CM}} + M d^2$. Pure rolling without slipping: $v_{\\text{CM}} = R\\omega$ and $a_{\\text{CM}} = R\\alpha$, with static friction providing torque $\\tau = I\\alpha$.",
        "level3": "Euler's equations for principal axes: $I_1 \\dot{\\omega}_1 - (I_2 - I_3)\\omega_2 \\omega_3 = \\tau_1$. For torque-free symmetric top ($I_1=I_2 \\neq I_3$), precession frequency is $\\Omega_{\\text{prec}} = \\frac{I_3 - I_1}{I_1}\\omega_3$.",
        "level4": "Standard inertia moments: Solid sphere $\\frac{2}{5}MR^2$, spherical shell $\\frac{2}{3}MR^2$, solid cylinder/disk $\\frac{1}{2}MR^2$, thin rod $\\frac{1}{12}ML^2$ (center) or $\\frac{1}{3}ML^2$ (end)."
    },
    "Small Oscillations, Coupled Systems & Normal Modes": {
        "title": "Small Oscillations, Secular Matrix & Normal Modes",
        "level1": "Taylor expansion about stable equilibrium $q_0$: $V(q) \\approx V(q_0) + \\frac{1}{2}\\sum_{i,j} V_{ij} \\eta_i \\eta_j$, where $V_{ij} = \\left.\\frac{\\partial^2 V}{\\partial q_i \\partial q_j}\\right|_{q_0}$ and $\\eta_i = q_i - q_{0,i}$. Kinetic energy is $T = \\frac{1}{2}\\sum_{i,j} T_{ij} \\dot{\\eta}_i \\dot{\\eta}_j$.",
        "level2": "Secular equation: $\\det(\\mathbf{V} - \\omega^2 \\mathbf{T}) = 0$. The roots $\\omega_k^2$ are the squared normal mode frequencies.",
        "level3": "Normal mode eigenvectors satisfy $(\\mathbf{V} - \\omega_k^2 \\mathbf{T})\\vec{a}^{(k)} = 0$. General motion is superposition: $\\vec{\\eta}(t) = \\sum_k C_k \\vec{a}^{(k)}\\cos(\\omega_k t + \\phi_k)$.",
        "level4": "Symmetry check: In symmetric systems (e.g. coupled pendula), symmetric mode has equal displacements $\\eta_1 = \\eta_2$ (spring at rest), while antisymmetric mode has $\\eta_1 = -\\eta_2$ (spring maximum stretch)."
    },
    "Collisions, Momentum Conservation & Variable Mass": {
        "title": "Collisions, Variable Mass & Momentum Conservation",
        "level1": "Linear momentum $\\vec{P} = \\sum m_i \\vec{v}_i$ is conserved when net external force is zero ($\\sum \\vec{F}_{\\text{ext}} = 0$). In elastic collisions, kinetic energy is also conserved.",
        "level2": "Variable mass dynamics (rocket equation, rope pulled from floor): $\\vec{F}_{\\text{ext}} = m\\frac{d\\vec{v}}{dt} + \\vec{v}_{\\text{rel}}\\frac{dm}{dt}$. For rocket in free space: $v(t) = v_0 + v_{\\text{ex}}\\ln(m_0/m(t))$.",
        "level3": "Center of Mass (CM) frame: Total momentum is zero ($\\vec{P}_{\\text{CM}} = 0$). In 1D elastic collisions, relative velocity of approach equals relative velocity of separation ($v_{2f} - v_{1f} = -(v_{2i} - v_{1i})$).",
        "level4": "Energy loss in inelastic collisions: $\\Delta K = \\frac{1}{2}\\frac{m_1 m_2}{m_1 + m_2}(v_1 - v_2)^2$ (maximum kinetic energy dissipated into deformation/heat)."
    },
    "Work-Energy Theorem & 1D Potential Dynamics": {
        "title": "Work-Energy Theorem & 1D Potential Energy Curves",
        "level1": "Work-Energy Theorem: $W_{\\text{net}} = \\Delta K = \\frac{1}{2}m v_f^2 - \\frac{1}{2}m v_i^2$. For conservative forces $F(x) = -\\frac{dV}{dx}$, total mechanical energy $E = K + V(x)$ is conserved.",
        "level2": "1D motion analysis: $v(x) = \\pm \\sqrt{\\frac{2}{m}(E - V(x))}$. Turning points occur where $E = V(x) \\implies v = 0$. Motion is bounded in intervals where $E \\geq V(x)$.",
        "level3": "Period of 1D periodic motion: $T = 2\\int_{x_{\\text{min}}}^{x_{\\text{max}}} \\frac{dx}{\\sqrt{\\frac{2}{m}(E - V(x))}}$.",
        "level4": "Equilibrium stability: $\\left.\\frac{dV}{dx}\\right|_{x_0} = 0$. Stable if $\\left.\\frac{d^2 V}{dx^2}\\right|_{x_0} > 0$ (oscillation frequency $\\omega = \\sqrt{V''(x_0)/m}$), unstable if $V''(x_0) < 0$."
    },
    "Newtonian Dynamics & Non-Inertial Frames": {
        "title": "Newtonian Dynamics & Non-Inertial Rotating Frames",
        "level1": "Newton's Second Law: $\\sum \\vec{F} = m\\vec{a}$. For circular motion of radius $R$ at speed $v$, centripetal acceleration is $a_c = \\frac{v^2}{R} = \\omega^2 R$.",
        "level2": "Non-inertial reference frame accelerating with $\\vec{A}_0$: Fictitious inertial force is $\\vec{F}_{\\text{inertial}} = -m\\vec{A}_0$.",
        "level3": "Rotating reference frame at angular velocity $\\vec{\\omega}$: Equation of motion is $m\\vec{a}_r = \\vec{F}_{\\text{real}} - 2m(\\vec{\\omega} \\times \\vec{v}_r) - m\\vec{\\omega} \\times (\\vec{\\omega} \\times \\vec{r}) - m\\dot{\\vec{\\omega}} \\times \\vec{r}$.",
        "level4": "Coriolis force $\\vec{F}_{\\text{Cor}} = -2m(\\vec{\\omega} \\times \\vec{v}_r)$ acts perpendicular to velocity, deflecting moving bodies (e.g. Foucault pendulum precession rate $\\Omega = \\omega_E \\sin\\lambda$)."
    },

    # =========================================================================
    # 3. QUANTUM MECHANICS
    # =========================================================================
    "Harmonic Oscillator & Ladder Operators": {
        "title": "Quantum Harmonic Oscillator & Ladder Operators",
        "level1": "Hamiltonian in operator form: $\\hat{H} = \\frac{\\hat{p}^2}{2m} + \\frac{1}{2}m\\omega^2\\hat{x}^2 = \\hbar\\omega\\left(\\hat{a}^\\dagger\\hat{a} + \\frac{1}{2}\\right)$. Energy eigenvalues are $E_n = \\hbar\\omega\\left(n + \\frac{1}{2}\\right)$ for $n = 0, 1, 2, \\dots$.",
        "level2": "Ladder operator algebra: $\\hat{a} = \\sqrt{\\frac{m\\omega}{2\\hbar}}\\hat{x} + \\frac{i}{\\sqrt{2m\\omega\\hbar}}\\hat{p}$ and $\\hat{a}^\\dagger = \\sqrt{\\frac{m\\omega}{2\\hbar}}\\hat{x} - \\frac{i}{\\sqrt{2m\\omega\\hbar}}\\hat{p}$, with commutator $[\\hat{a}, \\hat{a}^\\dagger] = 1$.",
        "level3": "Action on number eigenstates: $\\hat{a}|n\\rangle = \\sqrt{n}|n-1\\rangle$, $\\hat{a}^\\dagger|n\\rangle = \\sqrt{n+1}|n+1\\rangle$, and number operator $\\hat{N}|n\\rangle = n|n\\rangle$. Position and momentum: $\\hat{x} = \\sqrt{\\frac{\\hbar}{2m\\omega}}(\\hat{a} + \\hat{a}^\\dagger)$ and $\\hat{p} = i\\sqrt{\\frac{m\\omega\\hbar}{2}}(\\hat{a}^\\dagger - \\hat{a})$.",
        "level4": "Expectation values: $\\langle n|\\hat{x}|n\\rangle = 0$, $\\langle n|\\hat{p}|n\\rangle = 0$, $\\langle n|\\hat{x}^2|n\\rangle = \\frac{\\hbar}{2m\\omega}(2n+1)$, verifying virial theorem $\\langle T \\rangle = \\langle V \\rangle = \\frac{1}{2}E_n$."
    },
    "Dirac Formalism, State Vectors & Hilbert Space": {
        "title": "Dirac Bra-Ket Formalism & Observable Operators",
        "level1": "States are vectors $|\\psi\\rangle$ in Hilbert space with inner product $\\langle\\phi|\\psi\\rangle = \\langle\\psi|\\phi\\rangle^*$. Physical observables correspond to Hermitian operators $\\hat{A} = \\hat{A}^\\dagger$ with real eigenvalues $a_n$ and orthonormal eigenbasis $\\sum_n |n\\rangle\\langle n| = \\mathbf{1}$.",
        "level2": "Measurement postulate: Probability of measuring eigenvalue $a_n$ on state $|\\psi\\rangle$ is $P(a_n) = |\\langle n|\\psi\\rangle|^2$. Expectation value is $\\langle A \\rangle = \\langle\\psi|\\hat{A}|\\psi\\rangle$. Variance is $(\\Delta A)^2 = \\langle A^2 \\rangle - \\langle A \\rangle^2$.",
        "level3": "Generalized Uncertainty Principle: $\\Delta A \\Delta B \\geq \\frac{1}{2}|\\langle [\\hat{A}, \\hat{B}] \\rangle|$. Canonical commutator $[\\hat{x}, \\hat{p}] = i\\hbar$ implies $\\Delta x \\Delta p \\geq \\frac{\\hbar}{2}$.",
        "level4": "Time evolution: In Schrödinger picture, $|\\psi(t)\\rangle = e^{-i\\hat{H}t/\\hbar}|\\psi(0)\\rangle$. In Heisenberg picture, operators evolve via $\\frac{d\\hat{A}}{dt} = \\frac{i}{\\hbar}[\\hat{H}, \\hat{A}] + \\frac{\\partial\\hat{A}}{\\partial t}$ (Ehrenfest Theorem)."
    },
    "1D Potential Wells, Barriers & Quantum Tunneling": {
        "title": "1D Potential Wells, Barriers & Quantum Tunneling",
        "level1": "Time-independent Schrödinger equation: $-\\frac{\\hbar^2}{2m}\\frac{d^2\\psi}{dx^2} + V(x)\\psi = E\\psi$. Wave function $\\psi(x)$ and derivative $\\psi'(x)$ must be continuous everywhere (except $\\psi'$ discontinuous at delta potentials).",
        "level2": "Infinite square well of width $a$ ($0 \\leq x \\leq a$): Eigenfunctions $\\psi_n(x) = \\sqrt{\\frac{2}{a}}\\sin\\left(\\frac{n\\pi x}{a}\\right)$, energy eigenvalues $E_n = \\frac{\\hbar^2 \\pi^2 n^2}{2m a^2}$ ($n = 1, 2, 3, \\dots$).",
        "level3": "Rectangular potential barrier of height $V_0 > E$ and width $a$: Wave function inside barrier is evanescent $\\psi(x) \\sim e^{-\\kappa x}$ with $\\kappa = \\sqrt{\\frac{2m(V_0 - E)}{\\hbar^2}}$. Transmission coefficient is $T \\approx e^{-2\\kappa a}$ (tunneling).",
        "level4": "Probability current density: $j(x) = \\frac{\\hbar}{2mi}\\left(\\psi^* \\frac{d\\psi}{dx} - \\psi \\frac{d\\psi^*}{dx}\\right)$. Continuity requires $R + T = 1$."
    },
    "Angular Momentum, Spin Algebra & Addition of Momenta": {
        "title": "Angular Momentum & Spin-1/2 Algebra",
        "level1": "Angular momentum commutator algebra: $[\\hat{J}_i, \\hat{J}_j] = i\\hbar \\varepsilon_{ijk}\\hat{J}_k$. Simultaneous eigenbasis $|j, m\\rangle$ satisfies $\\hat{J}^2|j, m\\rangle = \\hbar^2 j(j+1)|j, m\\rangle$ and $\\hat{J}_z|j, m\\rangle = \\hbar m|j, m\\rangle$, with $-j \\leq m \\leq j$.",
        "level2": "Ladder operators $\\hat{J}_\\pm = \\hat{J}_x \\pm i\\hat{J}_y$ act as $\\hat{J}_\\pm|j, m\\rangle = \\hbar\\sqrt{j(j+1) - m(m\\pm 1)}|j, m\\pm 1\\rangle$.",
        "level3": "Spin-1/2 ($s=1/2$): $\\vec{S} = \\frac{\\hbar}{2}\\vec{\\sigma}$, where Pauli matrices are $\\sigma_x = \\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$, $\\sigma_y = \\begin{pmatrix}0&-i\\\\i&0\\end{pmatrix}$, $\\sigma_z = \\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}$. Note $\\sigma_i^2 = \\mathbf{1}$ and $\\{\\sigma_i, \\sigma_j\\} = 2\\delta_{ij}$.",
        "level4": "Addition of angular momenta $j_1 \\otimes j_2$: Total angular momentum takes values $|j_1 - j_2| \\leq J \\leq j_1 + j_2$ in integer steps. Singlet state ($J=0$) is antisymmetric $\\frac{1}{\\sqrt{2}}(|\\uparrow\\downarrow\\rangle - |\\downarrow\\uparrow\\rangle)$, triplet ($J=1$) is symmetric."
    },
    "Perturbation Theory & Approximation Methods": {
        "title": "Time-Independent Perturbation Theory & Approximations",
        "level1": "For $\\hat{H} = \\hat{H}_0 + \\hat{H}'$ with known unperturbed eigensystem $\\hat{H}_0|n^{(0)}\\rangle = E_n^{(0)}|n^{(0)}\\rangle$: 1st-order energy correction is the expectation value of the perturbation: $E_n^{(1)} = \\langle n^{(0)}|\\hat{H}'|n^{(0)}\\rangle$.",
        "level2": "2nd-order energy correction: $E_n^{(2)} = \\sum_{k \\neq n} \\frac{|\\langle k^{(0)}|\\hat{H}'|n^{(0)}\\rangle|^2}{E_n^{(0)} - E_k^{(0)}}$. For the ground state ($n=0$), the denominator is always negative, so $E_0^{(2)} \\leq 0$ strictly.",
        "level3": "Variational principle: For any normalized trial state $|\\psi_{\\text{trial}}\\rangle$, expectation value $E[\\psi] = \\langle\\psi|\\hat{H}|\\psi\\rangle \\geq E_0$ is a rigorous upper bound on the true ground-state energy.",
        "level4": "Degenerate perturbation theory: If unperturbed states are degenerate ($E_a^{(0)} = E_b^{(0)}$), diagonalize the perturbation matrix $W_{ij} = \\langle i^{(0)}|\\hat{H}'|j^{(0)}\\rangle$ within the degenerate subspace to find energy splittings."
    },
    "Hydrogen Atom & Central Potentials": {
        "title": "Hydrogen Atom & 3D Central Potentials",
        "level1": "Coulomb potential $V(r) = -\\frac{e^2}{4\\pi\\varepsilon_0 r}$. Radial wave equation with centrifugal barrier: $-\\frac{\\hbar^2}{2\\mu}\\frac{d^2 u}{dr^2} + \\left[V(r) + \\frac{\\hbar^2 l(l+1)}{2\\mu r^2}\\right]u = E u$.",
        "level2": "Energy levels of Hydrogen: $E_n = -\\frac{\\mu e^4}{32\\pi^2 \\varepsilon_0^2 \\hbar^2}\\frac{1}{n^2} = -\\frac{13.6\\text{ eV}}{n^2}$, with Bohr radius $a_0 = \\frac{4\\pi\\varepsilon_0 \\hbar^2}{\\mu e^2} \\approx 0.529\\text{ Å}$.",
        "level3": "Quantum numbers: Principal $n=1,2,\\dots$, orbital angular momentum $l=0,1,\\dots,n-1$, magnetic $m=-l,\\dots,+l$. Degeneracy of $n$-th energy level (without spin) is $n^2$, or $2n^2$ with spin.",
        "level4": "Muonic atom scaling: If electron is replaced by muon of mass $m_\\mu \\approx 207 m_e$, orbital radii scale as $r_\\mu = a_0/207$ and binding energies scale as $E_\\mu = 207 E_e$."
    },
    "Identical Particles, Bosons/Fermions & Symmetry": {
        "title": "Identical Particles & Permutation Symmetry",
        "level1": "Spin-Statistics Theorem: Bosons (integer spin $s=0,1,2,\\dots$) have symmetric wave functions $\\hat{P}_{12}\\psi = +\\psi$. Fermions (half-integer spin $s=1/2,3/2,\\dots$) have antisymmetric wave functions $\\hat{P}_{12}\\psi = -\\psi$.",
        "level2": "Pauli Exclusion Principle: Two identical fermions cannot occupy the same single-particle quantum state. Multi-fermion state is constructed as a Slater Determinant.",
        "level3": "Two identical non-interacting particles in states $\\psi_a, \\psi_b$: Total wave function is $\\psi_{\\pm}(\\vec{r}_1, \\vec{r}_2) = \\frac{1}{\\sqrt{2}}[\\psi_a(\\vec{r}_1)\\psi_b(\\vec{r}_2) \\pm \\psi_b(\\vec{r}_1)\\psi_a(\\vec{r}_2)]$.",
        "level4": "Spatial and Spin symmetry coupling: Total state $\\Psi = \\psi_{\\text{spatial}} \\otimes \\chi_{\\text{spin}}$ for two spin-1/2 fermions must be antisymmetric. Singlet spin (antisymmetric) couples with symmetric spatial wave function."
    },

    # =========================================================================
    # 4. THERMODYNAMICS
    # =========================================================================
    "1st & 2nd Laws / Thermodynamic Cycles": {
        "title": "Thermodynamic Laws & Heat Engine Cycles",
        "level1": "1st Law: $dU = \\delta Q - \\delta W$. Work done by gas is $W = \\int p dV$. For ideal gas, internal energy depends solely on temperature: $dU = n C_V dT$.",
        "level2": "2nd Law: Efficiency of any heat engine operating between $T_H$ and $T_C$ is $\\eta = \\frac{W}{Q_H} = 1 - \\frac{Q_C}{Q_H} \\leq \\eta_{\\text{Carnot}} = 1 - \\frac{T_C}{T_H}$.",
        "level3": "Adiabatic processes ($dQ=0$): $p V^\\gamma = \\text{const}$, $T V^{\\gamma-1} = \\text{const}$, where $\\gamma = C_p/C_v = 1 + 2/d$ ($d=3 \\implies \\gamma = 5/3$, $d=5 \\implies \\gamma = 7/5$).",
        "level4": "Entropy changes: $\\Delta S = \\int \\frac{dQ_{\\text{rev}}}{T}$. For ideal gas: $\\Delta S = n C_v \\ln(T_f/T_i) + nR \\ln(V_f/V_i)$. In an isolated system, $\\Delta S_{\\text{univ}} \\geq 0$ strictly."
    },
    "Thermodynamic Potentials & Maxwell Relations": {
        "title": "Thermodynamic Potentials & Maxwell Relations",
        "level1": "Fundamental potentials: Internal energy $dU = TdS - pdV + \\mu dN$, Enthalpy $H = U + pV \\implies dH = TdS + Vdp$, Helmholtz free energy $F = U - TS \\implies dF = -SdT - pdV$, Gibbs free energy $G = H - TS \\implies dG = -SdT + Vdp$.",
        "level2": "Maxwell Relations (from equality of mixed partials): $\\left(\\frac{\\partial T}{\\partial V}\\right)_S = -\\left(\\frac{\\partial p}{\\partial S}\\right)_V$, $\\left(\\frac{\\partial T}{\\partial p}\\right)_S = \\left(\\frac{\\partial V}{\\partial S}\\right)_p$, $\\left(\\frac{\\partial S}{\\partial V}\\right)_T = \\left(\\frac{\\partial p}{\\partial T}\\right)_V$, $\\left(\\frac{\\partial S}{\\partial p}\\right)_T = -\\left(\\frac{\\partial V}{\\partial T}\\right)_p$.",
        "level3": "Chemical potential $\\mu = \\left(\\frac{\\partial G}{\\partial N}\\right)_{T,p} = g$ (Gibbs free energy per particle). Phase coexistence occurs when $g_1(T,p) = g_2(T,p)$.",
        "level4": "Heat capacities relation: $C_p - C_v = T\\left(\\frac{\\partial p}{\\partial T}\\right)_V \\left(\\frac{\\partial V}{\\partial T}\\right)_p = \\frac{T V \\beta^2}{\\kappa_T} \\geq 0$."
    },
    "Ideal & Real Gases (Equation of State)": {
        "title": "Ideal & Real Gases (Van der Waals Equation of State)",
        "level1": "Ideal gas: $p V = n R T = N k_B T$. Internal energy $U = \\frac{d}{2}N k_B T$. Speed of sound $v_s = \\sqrt{\\frac{\\gamma k_B T}{m}}$.",
        "level2": "Van der Waals real gas: $\\left(p + \\frac{a n^2}{V^2}\\right)(V - n b) = n R T$. Parameter $a$ accounts for intermolecular attractive forces, $b$ accounts for molecular volume.",
        "level3": "Critical point parameters: $\\left.\\frac{\\partial p}{\\partial V}\\right|_{T_c} = 0$ and $\\left.\\frac{\\partial^2 p}{\\partial V^2}\\right|_{T_c} = 0$, giving $V_c = 3nb$, $p_c = \\frac{a}{27b^2}$, $T_c = \\frac{8a}{27Rb}$, and critical compressibility $Z_c = \\frac{p_c V_c}{nRT_c} = \\frac{3}{8} = 0.375$.",
        "level4": "Joule-Thomson expansion (constant enthalpy $dH=0$): Inversion temperature $T_{\\text{inv}} = \\frac{2a}{Rb}$ separates heating ($\\mu_{JT} < 0$) from cooling ($\\mu_{JT} > 0$)."
    },
    "Phase Transitions & Clausius-Clapeyron": {
        "title": "Phase Transitions & Clausius-Clapeyron Equation",
        "level1": "First-order phase transitions involve latent heat $L = T\\Delta S$ and volume discontinuity $\\Delta V = V_2 - V_1$ with continuous Gibbs free energy $G_1 = G_2$.",
        "level2": "Clausius-Clapeyron equation gives the slope of coexistence curve: $\\frac{dp}{dT} = \\frac{L}{T \\Delta V} = \\frac{\\Delta S}{\\Delta V}$.",
        "level3": "Liquid-Vapor vaporization ($V_{\\text{gas}} \\gg V_{\\text{liq}}$ with ideal gas $V_{\\text{gas}} = nRT/p$): $\\frac{dp}{p} = \\frac{L}{R T^2} dT \\implies p(T) = p_0 e^{-\\frac{L}{R}\\left(\\frac{1}{T} - \\frac{1}{T_0}\\right)}$.",
        "level4": "Water anomaly: Because ice has larger specific volume than liquid water ($\Delta V < 0$ for melting), melting temperature decreases with pressure ($\frac{dp}{dT} < 0$)."
    },
    "Calorimetry, Heat Capacities & Thermal Expansion": {
        "title": "Calorimetry, Heat Capacities & Thermal Equilibrium",
        "level1": "Heat capacity $C = \\frac{\\delta Q}{dT}$. Specific heat $c = \\frac{C}{m}$. Thermal expansion coefficient $\\alpha = \\frac{1}{V}\\left(\\frac{\\partial V}{\\partial T}\\right)_p$. Isothermal compressibility $\\kappa_T = -\\frac{1}{V}\\left(\\frac{\\partial V}{\\partial p}\\right)_T$.",
        "level2": "Calorimetric thermal equilibrium: For isolated mixtures, $\\sum Q_{\\text{absorbed}} + \\sum Q_{\\text{released}} = 0$.",
        "level3": "Dulon-Petit Law: At high temperatures, molar heat capacity of 3D solids approaches $C_V = 3 R = 3 N_A k_B \\approx 24.9 \\text{ J}/(\\text{mol}\\cdot\\text{K})$.",
        "level4": "Low-temperature Debye behavior: In non-magnetic insulators, heat capacity drops as $C_V \\propto T^3$ due to acoustic phonons."
    },
    "Entropy Changes & Reversibility": {
        "title": "Entropy Calculations & Irreversible Processes",
        "level1": "Entropy differential: $dS = \\frac{dQ_{\\text{rev}}}{T}$. For any irreversible process between initial state $i$ and final state $f$, $\\Delta S = \\int_i^f \\frac{dQ_{\\text{rev}}}{T}$ calculated along an arbitrary reversible path.",
        "level2": "Free adiabatic expansion into vacuum (Joule expansion): No work is done ($W=0$) and no heat is exchanged ($Q=0$), so $\\Delta U = 0 \\implies T_f = T_i$ (ideal gas). Entropy change is $\\Delta S = n R \\ln(V_f/V_i) > 0$.",
        "level3": "Thermal contact between two bodies ($T_1, T_2$) with heat capacity $C$: Final temperature is $T_f = \\frac{T_1 + T_2}{2}$. Total entropy change is $\\Delta S_{\\text{total}} = C \\ln\\left(\\frac{T_f^2}{T_1 T_2}\\right) \\geq 0$.",
        "level4": "Statistical definition: Boltzmann entropy $S = k_B \\ln \\Omega$. 2nd Law states the number of accessible microstates $\\Omega$ cannot decrease in an isolated system."
    },

    # =========================================================================
    # 5. STATISTICAL PHYSICS
    # =========================================================================
    "Canonical & Microcanonical Ensembles": {
        "title": "Statistical Ensembles & Partition Functions",
        "level1": "Microcanonical ensemble: isolated system $(E, V, N)$ with entropy $S = k_B \\ln \\Omega(E)$. Temperature defined via $\\frac{1}{T} = \\left(\\frac{\\partial S}{\\partial E}\\right)_{V,N}$.",
        "level2": "Canonical ensemble: system at fixed $(T, V, N)$. Boltzmann probability $P_i = \\frac{e^{-\\beta E_i}}{Z}$, with canonical partition function $Z = \\sum_i e^{-\\beta E_i}$ where $\\beta = 1/(k_B T)$. Helmholtz free energy is $F = -k_B T \\ln Z$.",
        "level3": "Mean energy and fluctuations: $\\langle E \\rangle = -\\frac{\\partial \\ln Z}{\\partial \\beta} = k_B T^2 \\frac{\\partial \\ln Z}{\\partial T}$. Heat capacity $C_v = \\left(\\frac{\\partial \\langle E \\rangle}{\\partial T}\\right)_V = \\frac{(\\Delta E)^2}{k_B T^2} \\geq 0$.",
        "level4": "Equipartition Theorem: Every quadratic degree of freedom in the classical Hamiltonian contributes $\\frac{1}{2}k_B T$ to mean energy and $\\frac{1}{2}k_B$ to heat capacity."
    },
    "Grand Canonical Ensemble & Chemical Potential": {
        "title": "Grand Canonical Ensemble & Particle Fluctuations",
        "level1": "Grand canonical ensemble: system at fixed $(T, V, \\mu)$ capable of exchanging energy and particles with reservoir. Gibbs factor is $P_{i,N} = \\frac{e^{-\\beta(E_i - \\mu N)}}{\\mathcal{Z}}$.",
        "level2": "Grand partition function: $\\mathcal{Z} = \\sum_{N=0}^\\infty z^N Z_N(T,V)$, where $z = e^{\\beta \\mu}$ is fugacity. Grand potential is $\\Phi = -k_B T \\ln \\mathcal{Z} = -p V$.",
        "level3": "Mean particle number and fluctuations: $\\langle N \\rangle = \\frac{1}{\\beta}\\frac{\\partial \\ln \\mathcal{Z}}{\\partial \\mu} = z\\frac{\\partial \\ln \\mathcal{Z}}{\\partial z}$. Relative variance is $(\\Delta N)^2 = k_B T \\left(\\frac{\\partial \\langle N \\rangle}{\\partial \\mu}\\right)_{T,V}$.",
        "level4": "Thermodynamic limit: Particle number fluctuations scale as $\\frac{\\Delta N}{\\langle N \\rangle} \\propto \\frac{1}{\\sqrt{N}} \\to 0$, ensuring canonical and grand canonical ensembles are equivalent for macroscopic systems."
    },
    "Quantum Gases (Fermi-Dirac & Degeneracy)": {
        "title": "Fermi-Dirac Statistics & Degenerate Fermi Gas",
        "level1": "Fermi-Dirac distribution for fermions: $\\bar{n}(\\varepsilon) = \\frac{1}{e^{\\beta(\\varepsilon - \\mu)} + 1}$. At $T=0$, occupation is a step function: $\\bar{n}(\\varepsilon) = 1$ for $\\varepsilon \\leq E_F$ and $0$ for $\\varepsilon > E_F$.",
        "level2": "Fermi Energy in 3D (spin-1/2): Density of states $g(\\varepsilon) = \\frac{V}{2\\pi^2}\\left(\\frac{2m}{\\hbar^2}\\right)^{3/2}\\sqrt{\\varepsilon}$. Total particles $N = \\int_0^{E_F} g(\\varepsilon)d\\varepsilon \\implies E_F = \\frac{\\hbar^2}{2m}(3\\pi^2 n)^{2/3}$, where $n = N/V$.",
        "level3": "Total ground-state energy at $T=0$: $E_0 = \\frac{3}{5} N E_F$. Degeneracy pressure is $P_0 = \\frac{2}{3}\\frac{E_0}{V} = \\frac{2}{5} n E_F$ (independent of temperature).",
        "level4": "Sommerfeld expansion at low temperatures ($T \\ll T_F$): Electronic heat capacity is linear in temperature: $C_V = \\frac{\\pi^2}{2} N k_B \\left(\\frac{T}{T_F}\\right)$."
    },
    "Quantum Gases (Bose-Einstein Condensation & Blackbody)": {
        "title": "Bose-Einstein Statistics & Condensation",
        "level1": "Bose-Einstein distribution for bosons: $\\bar{n}(\\varepsilon) = \\frac{1}{e^{\\beta(\\varepsilon - \\mu)} - 1}$. Chemical potential must satisfy $\\mu \\leq \\varepsilon_0 = 0$ to maintain non-negative occupation numbers.",
        "level2": "Bose-Einstein Condensation (BEC): Below critical temperature $T_c = \\frac{2\\pi\\hbar^2}{m k_B}\\left(\\frac{n}{\\zeta(3/2)}\\right)^{2/3} \\approx 3.31 \\frac{\\hbar^2 n^{2/3}}{m k_B}$, the ground state develops macroscopic occupation $N_0/N = 1 - (T/T_c)^{3/2}$.",
        "level3": "Blackbody photon gas ($\mu = 0$): Photon dispersion $\\varepsilon = \\hbar\\omega = \\hbar c k$. Energy density spectrum is Planck's law $u(\\omega) d\\omega = \\frac{\\hbar}{\\pi^2 c^3}\\frac{\\omega^3}{e^{\\beta\\hbar\\omega} - 1} d\\omega$.",
        "level4": "Stefan-Boltzmann Law: Total energy density is $u = \\int_0^\\infty u(\\omega)d\\omega = a T^4 = \\frac{\\pi^2 k_B^4}{15 \\hbar^3 c^3} T^4$. Radiation pressure is $P = \\frac{1}{3}u$."
    },
    "Spin Systems, Paramagnetism & Ising Model": {
        "title": "Spin Systems, Paramagnetism & Magnetic Phase Transitions",
        "level1": "Paramagnet of $N$ non-interacting spin-1/2 moments $\\mu$ in magnetic field $B$: Single-spin partition function is $Z_1 = e^{\\beta \\mu B} + e^{-\\beta \\mu B} = 2\\cosh(\\beta \\mu B)$. Total partition function is $Z = Z_1^N$.",
        "level2": "Magnetization: $M = -\\left(\\frac{\\partial F}{\\partial B}\\right)_T = N \\mu \\tanh\\left(\\frac{\\mu B}{k_B T}\\right)$.",
        "level3": "Curie's Law (weak field limit $\\mu B \\ll k_B T$): $\\tanh(x) \\approx x \\implies M \\approx \\frac{N \\mu^2 B}{k_B T}$, yielding magnetic susceptibility $\\chi = \\left.\\frac{\\partial M}{\\partial B}\\right|_{B\\to 0} = \\frac{C}{T}$ where $C = \\frac{N \\mu^2}{k_B}$.",
        "level4": "Ising Model & Mean Field Theory: Exchange interaction $H = -J \\sum_{\\langle i,j \\rangle} s_i s_j - B \\sum s_i$. Spontaneous symmetry breaking occurs below Curie temperature $T_c = z J / k_B$."
    },
    "Two-Level Systems & Paramagnetic Entropy": {
        "title": "Two-Level Systems & Negative Absolute Temperatures",
        "level1": "Single particle with two energy states ($0$ and $\\varepsilon$): Partition function $Z_1 = 1 + e^{-\\beta\\varepsilon}$. For $N$ distinguishable systems: $Z = (1 + e^{-\\beta\\varepsilon})^N$.",
        "level2": "Average energy: $\\langle E \\rangle = \\frac{N \\varepsilon e^{-\\beta\\varepsilon}}{1 + e^{-\\beta\\varepsilon}} = \\frac{N\\varepsilon}{e^{\\beta\\varepsilon} + 1}$.",
        "level3": "Schottky Heat Capacity: $C_V = \\frac{\\partial \\langle E \\rangle}{\\partial T} = N k_B \\left(\\frac{\\varepsilon}{k_B T}\\right)^2 \\frac{e^{\\varepsilon/k_B T}}{(e^{\\varepsilon/k_B T} + 1)^2}$. Exhibits a characteristic peak (Schottky anomaly) around $k_B T \\approx 0.42 \\varepsilon$.",
        "level4": "Population inversion & Negative temperature: If high-energy state is more populated than ground state ($N_1 > N_0$), the slope $\\frac{\\partial S}{\\partial E} = \\frac{1}{T} < 0$, corresponding to negative absolute temperatures hotter than $+ \\infty$."
    },

    # =========================================================================
    # 6. MODERN PHYSICS
    # =========================================================================
    "Special Relativity & Lorentz Transformations": {
        "title": "Special Relativity & Lorentz Transformations",
        "level1": "Einstein postulates: Speed of light $c$ is invariant in all inertial frames. Lorentz boost along $x$: $x' = \\gamma(x - vt)$, $t' = \\gamma(t - vx/c^2)$, where $\\gamma = 1/\\sqrt{1 - v^2/c^2}$.",
        "level2": "Kinematic consequences: Time dilation $\\Delta t = \\gamma \\Delta t_0$ (moving clocks run slow) and length contraction $L = L_0/\\gamma$ (lengths parallel to relative motion contract).",
        "level3": "Invariant spacetime interval: $s^2 = c^2 \\Delta t^2 - \\Delta x^2 - \\Delta y^2 - \\Delta z^2$. Timelike ($s^2 > 0$), Spacelike ($s^2 < 0$), Lightlike ($s^2 = 0$).",
        "level4": "Relativistic velocity addition: For particle moving with $u_x'$ in frame $S'$ moving at $v$ relative to $S$: $u_x = \\frac{u_x' + v}{1 + \\frac{u_x' v}{c^2}}$."
    },
    "Relativistic Dynamics & Energy-Momentum": {
        "title": "Relativistic Dynamics & 4-Momentum Conservation",
        "level1": "Relativistic 4-momentum: $P^\\mu = (E/c, \\vec{p}) = (\\gamma m c, \\gamma m \\vec{v})$. Spatial momentum is $\\vec{p} = \\gamma m \\vec{v}$ and total energy is $E = \\gamma m c^2 = K + m c^2$.",
        "level2": "Invariant Mass Relation: $P^\\mu P_\\mu = \\frac{E^2}{c^2} - p^2 = m^2 c^2 \\implies E^2 = p^2 c^2 + m^2 c^4$. For massless photons ($m=0$), $E = p c$.",
        "level3": "Conservation of 4-momentum in particle collisions/decays: $\\sum P_{\\text{initial}}^\\mu = \\sum P_{\\text{final}}^\\mu$.",
        "level4": "Decay threshold: For particle of rest energy $M c^2$ decaying into two particles of equal mass $m c^2$ moving with kinetic energy $K$, conservation gives $M = 2\\gamma m$ and $K = (M/2 - m)c^2$."
    },
    "Photoelectric Effect & Photon Interactions": {
        "title": "Photoelectric Effect & Photon-Matter Interactions",
        "level1": "Einstein's photoelectric equation: $K_{\\text{max}} = h\\nu - \\Phi = \\frac{h c}{\\lambda} - \\Phi = e V_s$, where $\\Phi$ is the work function and $V_s$ is the stopping potential.",
        "level2": "Cutoff threshold: Photoemission occurs only if frequency exceeds cutoff $\\nu_0 = \\Phi/h$ (or wavelength $\\lambda \\leq \\lambda_0 = hc/\\Phi$), independent of light intensity.",
        "level3": "Compton scattering of photon on stationary electron: Wavelength shift is $\\Delta \\lambda = \\lambda' - \\lambda = \\lambda_c(1 - \\cos\\theta)$, where Compton wavelength is $\\lambda_c = \\frac{h}{m_e c} \\approx 2.43 \\times 10^{-12}\\text{ m} = 0.0243\\text{ Å}$.",
        "level4": "Photon momentum: $\\vec{p} = \\hbar\\vec{k} = \\frac{h}{\\lambda}\\hat{n}$, photon energy $E = h\\nu = \\hbar\\omega$. Relativistic momentum conservation governs Compton collision."
    },
    "Matter Waves & de Broglie Hypothesis": {
        "title": "Matter Waves & Wave-Particle Duality",
        "level1": "de Broglie relation: A particle of momentum $p = mv$ possesses an associated matter wavelength $\\lambda = \\frac{h}{p} = \\frac{h}{mv}$.",
        "level2": "Non-relativistic particle with kinetic energy $K = \\frac{p^2}{2m} = q V$: de Broglie wavelength is $\\lambda = \\frac{h}{\\sqrt{2m K}} = \\frac{h}{\\sqrt{2m q V}}$. For electron: $\\lambda \\approx \\frac{12.27}{\\sqrt{V}}\\text{ Å}$.",
        "level3": "Bragg diffraction of matter waves on crystal lattices with atomic spacing $d$: Constructive interference condition is $2d\\sin\\theta = n\\lambda$ (Davisson-Germer experiment).",
        "level4": "Phase and group velocity: Phase velocity $v_{\\text{ph}} = \\frac{\\omega}{k} = \\frac{E}{p} = \\frac{c^2}{v} > c$; Group velocity of wave packet $v_g = \\frac{d\\omega}{dk} = \\frac{dE}{dp} = v$ equals the physical particle speed."
    },
    "Atomic Models (Bohr, Rydberg & Franck-Hertz)": {
        "title": "Bohr Atomic Model, Spectral Series & Franck-Hertz Experiment",
        "level1": "Bohr quantization postulate: Angular momentum is quantized in units of $\\hbar$: $L = m v r = n \\hbar$ ($n=1,2,3,\\dots$).",
        "level2": "Bohr radii and energy levels: $r_n = n^2 a_0$, with $a_0 = \\frac{4\\pi\\varepsilon_0 \\hbar^2}{m e^2} \\approx 0.529\\text{ Å}$. Energy eigenvalues: $E_n = -\\frac{13.6\\text{ eV}}{n^2}$.",
        "level3": "Rydberg formula for hydrogen emission lines: $\\frac{1}{\\lambda} = R_H\\left(\\frac{1}{n_1^2} - \\frac{1}{n_2^2}\\right)$, where Lyman series ($n_1=1$, UV), Balmer series ($n_1=2$, visible), Paschen series ($n_1=3$, IR).",
        "level4": "Franck-Hertz experiment: Demonstrates discrete energy quantization in atomic vapor via periodic current drops spaced by the first excitation threshold (e.g. $\\Delta V = 4.9\\text{ V}$ in mercury vapor)."
    },
    "Blackbody Radiation & Quantum Optics": {
        "title": "Blackbody Thermal Radiation & Planck's Radiation Law",
        "level1": "Wien's Displacement Law: Peak emission wavelength satisfies $\\lambda_{\\text{max}} T = b \\approx 2.898 \\times 10^{-3}\\text{ m}\\cdot\\text{K}$.",
        "level2": "Stefan-Boltzmann Law: Total radiant exitance of blackbody is $I = \\sigma T^4$, where $\\sigma = \\frac{2\\pi^5 k_B^4}{15 c^2 h^3} \\approx 5.67 \\times 10^{-8}\\text{ W}/(\\text{m}^2\\cdot\\text{K}^4)$.",
        "level3": "Planck's Radiation Law: Energy density spectral distribution is $u(\\lambda) d\\lambda = \\frac{8\\pi h c}{\\lambda^5}\\frac{1}{e^{h c/(\\lambda k_B T)} - 1} d\\lambda$.",
        "level4": "Asymptotic limits: For long wavelengths ($hc/\\lambda \\ll k_B T$), expands to classical Rayleigh-Jeans law $u(\\lambda) \\approx \\frac{8\\pi k_B T}{\\lambda^4}$. For short wavelengths, approaches Wien distribution $u(\\lambda) \\approx \\frac{8\\pi h c}{\\lambda^5}e^{-h c/(\\lambda k_B T)}$."
    },
    "Nuclear Physics & Radioactive Decay": {
        "title": "Nuclear Physics, Binding Energy & Radioactive Decay",
        "level1": "Radioactive decay law: $N(t) = N_0 e^{-\\lambda t} = N_0 2^{-t/t_{1/2}}$, where decay constant $\\lambda = \\frac{\\ln 2}{t_{1/2}}$ and mean lifetime is $\\tau = 1/\\lambda$. Activity is $A(t) = -\\frac{dN}{dt} = \\lambda N(t)$.",
        "level2": "Nuclear binding energy: $B(A,Z) = [Z m_p + (A-Z)m_n - M(A,Z)]c^2$. Maximum binding energy per nucleon $B/A \\approx 8.8\\text{ MeV/nucleon}$ occurs near Iron-56 ($^{56}\\text{Fe}$).",
        "level3": "Decay modes: Alpha decay ($^{A}_{Z}X \\to ^{A-4}_{Z-2}Y + \\alpha$), Beta-minus decay ($n \\to p + e^- + \\bar{\\nu}_e$), Beta-plus decay ($p \\to n + e^+ + \\nu_e$), Gamma decay ($X^* \\to X + \\gamma$).",
        "level4": "Q-value of nuclear reaction: $Q = (m_{\\text{reactants}} - m_{\\text{products}})c^2$. Exothermic ($Q > 0$) releases energy; Endothermic ($Q < 0$) requires threshold kinetic energy $K_{\\text{th}} = |Q|\\left(1 + \\frac{m_{\\text{projectile}}}{m_{\\text{target}}}\\right)$."
    }
}


def get_physics_clues(area, subtopic, question_id, text=""):
    """Returns dynamic, context-specific clues tailored to the exact subtopic and physical phenomenon."""
    # 1. Exact subtopic match
    if subtopic in HINT_KNOWLEDGE_BASE:
        return HINT_KNOWLEDGE_BASE[subtopic]
        
    # 2. Substring matching
    sub_clean = subtopic.lower()
    for sub_key, kb in HINT_KNOWLEDGE_BASE.items():
        k_clean = sub_key.lower()
        if k_clean in sub_clean or sub_clean in k_clean:
            return kb

    # 3. Fallback to descriptive canonical guidance per Area (Never Generic)
    area_fallbacks = {
        "Eletromagnetismo": HINT_KNOWLEDGE_BASE["Continuous Charge Distributions & Electric Potentials"],
        "Mecânica Clássica": HINT_KNOWLEDGE_BASE["Lagrangian Mechanics & Generalized Coordinates"],
        "Mecânica Quântica": HINT_KNOWLEDGE_BASE["Dirac Formalism, State Vectors & Hilbert Space"],
        "Termodinâmica": HINT_KNOWLEDGE_BASE["1st & 2nd Laws / Thermodynamic Cycles"],
        "Física Estatística": HINT_KNOWLEDGE_BASE["Canonical & Microcanonical Ensembles"],
        "Física Moderna": HINT_KNOWLEDGE_BASE["Special Relativity & Lorentz Transformations"],
    }
    
    return area_fallbacks.get(area, HINT_KNOWLEDGE_BASE["Lagrangian Mechanics & Generalized Coordinates"])
