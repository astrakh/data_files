"""Elemental budget for a 4 M_J 'distilled' super-Jupiter (S- and F-rich, N/Na/K-poor).

Abundances: Asplund et al. (2009) photospheric, log eps (H = 12).
Pipeline: solar -> host star (birth-environment offsets, dex)
          -> accreted gas (disk transfer factors + retort distillation of S, F)
          -> bulk planet (envelope + small dry core).
"""
import math

SOLAR = {  # element: (log eps, atomic mass)
    "H": (12.00, 1.008), "He": (10.93, 4.003), "C": (8.43, 12.011),
    "N": (7.83, 14.007), "O": (8.69, 15.999), "F": (4.56, 18.998),
    "Ne": (7.93, 20.180), "Na": (6.24, 22.990), "Mg": (7.60, 24.305),
    "Al": (6.45, 26.982), "Si": (7.51, 28.086), "P": (5.41, 30.974),
    "S": (7.12, 32.06), "Cl": (5.50, 35.45), "Ar": (6.40, 39.948),
    "K": (5.03, 39.098), "Ca": (6.34, 40.078), "Cr": (5.64, 51.996),
    "Fe": (7.50, 55.845), "Ni": (6.22, 58.693),
}
# Elements that sit in dry refractory dust in the 700-950 K zone (pre-distillation).
DUST = ["Na", "Mg", "Al", "Si", "P", "S", "Cl", "K", "Ca", "Cr", "Fe", "Ni", "F"]
# Oxygen locked in silicates/oxides per dust cation (rough: MgSiO3 + oxides).
DUST_O_PER = {"Mg": 1.0, "Si": 2.0, "Al": 1.5, "Ca": 1.0, "Na": 0.5, "K": 0.5, "P": 2.5}

# Lever 1 -- birth environment: alpha-rich, mildly metal-poor host, odd-Z (Na) suppressed,
# low secondary N, extra F from nu-process/WC-wind pollution, extra S from SN Ia + alpha.
HOST_DEX = {
    "He": 0.0, "C": -0.55, "N": -0.75, "O": -0.05, "F": +0.10, "Ne": -0.05,
    "Na": -0.65, "Mg": -0.05, "Al": -0.55, "Si": -0.05, "P": -0.35, "S": +0.05,
    "Cl": -0.35, "Ar": -0.05, "K": -0.45, "Ca": -0.05, "Cr": -0.35, "Fe": -0.35,
    "Ni": -0.40,
}

# Lever 2/3 -- disk transfer factors for the gas the planet actually accretes
# (relative to host). Volatiles: cold-trapped in outer rings (N2->NH3, CO->CO2/CH3OH
# processing by high ionisation). Refractories: held back by the 4 M_J gap filter.
TRANSFER = {
    "He": 1.0, "Ne": 1.0, "Ar": 0.9,
    "C": 0.15, "N": 0.05, "O": 0.12,
    "Na": 0.03, "K": 0.03, "Mg": 0.03, "Al": 0.03, "Si": 0.03, "P": 0.03,
    "Ca": 0.03, "Cr": 0.03, "Fe": 0.03, "Ni": 0.03, "Cl": 0.10,
    "S": 0.0, "F": 0.0,  # S, F come only from distillation (below)
}
M_J_EARTH = 317.83
M_PLANET = 4.0 * M_J_EARTH
M_CORE = 5.0            # Earth masses, dry rock+metal, stays stably stratified
M_RING = 70.0           # Earth masses of dry dust distilled in the gap-edge "retort"
F_RELEASE = {"S": 0.90, "F": 0.90}   # fraction released as H2S / HF at 750-950 K


def number_ratio(dex_map):
    return {el: 10 ** (SOLAR[el][0] - 12 + dex_map.get(el, 0.0)) for el in SOLAR}


def mass_fracs(nr):
    tot = sum(nr[el] * SOLAR[el][1] for el in nr)
    return {el: nr[el] * SOLAR[el][1] / tot for el in nr}


sun = number_ratio({})
host = number_ratio(HOST_DEX)
Xh = mass_fracs(host)

# Dust-to-gas ratio and composition of the host's dry refractory dust.
dust_mass = {el: Xh[el] for el in DUST}
dust_mass["O"] = sum(host[el] * DUST_O_PER.get(el, 0) for el in DUST) * SOLAR["O"][1] \
    / sum(host[e] * SOLAR[e][1] for e in host)
d2g = sum(dust_mass.values())

M_env = M_PLANET - M_CORE
env = {el: host[el] * TRANSFER.get(el, 1.0) for el in SOLAR}
env["H"] = 1.0
for el in ("S", "F"):
    released_mass = F_RELEASE[el] * M_RING * dust_mass[el] / d2g  # Earth masses
    # convert added mass to number ratio per H in envelope gas
    gas_H_mass = M_env * Xh["H"]
    env[el] += released_mass / SOLAR[el][1] / (gas_H_mass / SOLAR["H"][1])

Xe = mass_fracs(env)
Z_env = 1 - Xe["H"] - Xe["He"]
Z_bulk = (Z_env * M_env + M_CORE) / M_PLANET
Z_sun = 1 - mass_fracs(sun)["H"] - mass_fracs(sun)["He"]
Z_thorngren = 49.3 * 4.0 ** 0.61 / M_PLANET  # Thorngren+2016 mass-metallicity relation


def dex(el, comp):
    return math.log10(comp[el] / sun[el])


print(f"host dry-dust/gas = {d2g:.4f};  S in dust = {100*dust_mass['S']/d2g:.1f} wt%,"
      f"  F in dust = {1e6*dust_mass['F']/d2g:.0f} ppm")
print(f"\n{'el':>3} {'[X/H]host':>10} {'[X/H]env':>9} {'env X/H (num)':>14} {'xSun':>8}")
for el in SOLAR:
    if el == "H":
        continue
    print(f"{el:>3} {dex(el, host):10.2f} {dex(el, env):9.2f} {env[el]:14.3e} {env[el]/sun[el]:8.3f}")

S_N = env["S"] / env["N"]; S_N_sun = sun["S"] / sun["N"]
F_NaK = env["F"] / (env["Na"] + env["K"]); F_NaK_sun = sun["F"] / (sun["Na"] + sun["K"])
print(f"\nS/N        = {S_N:9.3f}  (solar {S_N_sun:.3f}, x{S_N/S_N_sun:.0f})")
print(f"F/(Na+K)   = {F_NaK:9.3f}  (solar {F_NaK_sun:.4f}, x{F_NaK/F_NaK_sun:.0f})")
print(f"S/O        = {env['S']/env['O']:9.3f}  (solar {sun['S']/sun['O']:.4f})")
print(f"C/O        = {env['C']/env['O']:9.3f}  (solar {sun['C']/sun['O']:.3f})")
print(f"\nZ_sun = {Z_sun:.4f}")
print(f"Z_env = {Z_env:.4f}  ({Z_env/Z_sun:.2f} x solar)")
print(f"Z_bulk (env + {M_CORE:.0f} M_E core) = {Z_bulk:.4f}  ({Z_bulk/Z_sun:.2f} x solar)")
print(f"Typical 4 M_J (Thorngren+16): Z ~ {Z_thorngren:.3f}  ({Z_thorngren/Z_sun:.1f} x solar)")
print("\nTop contributors to Z_env (mass fraction):")
for el, x in sorted(((e, Xe[e]) for e in Xe if e not in ("H", "He")), key=lambda t: -t[1])[:7]:
    print(f"  {el:>3} {x:.2e}  ({100*x/Z_env:.0f}% of Z_env)")


def sweep(rings=(5, 10, 25, 40, 70, 100, 150)):
    """Trade-off: distilled dust mass vs S/H, F/H and envelope metallicity."""
    print(f"\n{'M_ring':>7} {'[S/H]':>6} {'[F/H]':>6} {'Z_env/Zsun':>10} {'Z_bulk/Zsun':>11}")
    gas_H_mass = M_env * Xh["H"]
    for mr in rings:
        e = dict(env)
        for el in ("S", "F"):
            e[el] = F_RELEASE[el] * mr * dust_mass[el] / d2g / SOLAR[el][1] \
                / (gas_H_mass / SOLAR["H"][1])
        x = mass_fracs(e)
        z = 1 - x["H"] - x["He"]
        zb = (z * M_env + M_CORE) / M_PLANET
        print(f"{mr:7.0f} {dex('S', e):6.2f} {dex('F', e):6.2f} {z/Z_sun:10.2f} {zb/Z_sun:11.2f}")


sweep()
