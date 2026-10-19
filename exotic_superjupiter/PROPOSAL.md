# A "distilled" 4 M_J super-Jupiter: S- and F-rich, N/Na/K-starved, sub-solar Z

Goal: maximise F/H and S/H while minimising N, Na, K (maximise S/N and F/(Na+K))
and keeping the total metallicity Z low. The numbers below come from `budget.py`
(Asplund+2009 solar scale).

## Core idea

S and F are the only two "rock-forming" elements that leave dust in a narrow
temperature window:

| carrier | 50% condensation T (Lodders 2003) | behaviour 750–950 K |
|---|---|---|
| N (N2, NH3) | 20–130 K | gas everywhere → must be removed *before* the gas arrives |
| C, O (CO, CO2, H2O) | 20–150 K | same |
| **S** (FeS, troilite) | 664–704 K | **released as H2S** |
| **F** (F-apatite, micas) | 734 K | **released as HF** |
| Cl (sodalite) | 948 K | stays solid |
| **Na** (feldspar) | 958 K | **stays solid** |
| **K** (feldspar) | 1006 K | **stays solid** |
| Mg, Si, Fe, Ca, Al | 1300–1650 K | stay solid |

So the recipe is: feed the planet gas that has (1) already lost its C/N/O ices
far out, (2) had a large mass of dry dust "boiled" at 750–950 K beside it, and
(3) not carried any of that dust's residue (Na, K, Mg, Si, Fe) in with it.
S and F are added nearly pure, so Z stays low.

## Levers, in order

### 1. Birth environment (host-star composition)
- **Mildly metal-poor, α-rich host** ([Fe/H] ≈ −0.35, [α/Fe] ≈ +0.3, thick-disk/bulge-like):
  S rides with α (and gets extra from SN Ia pollution), while Fe-peak elements and the total dust mass drop.
- **Odd-Z effect**: low-metallicity massive stars give low Na/Mg and Al/Mg → [Na/H] ≈ −0.65.
- **Low N**: secondary N scales as Z². Avoid regions polluted by hot-bottom-burning
  (4–8 M☉) AGB stars and WN winds → [N/H] ≈ −0.75.
- **Extra F**: pre-enrichment from the ν-process (²⁰Ne(ν,ν'p)¹⁹F) in a nearby CCSN, and/or
  a **WC-phase** Wolf–Rayet wind, which is F-rich *and* N-poor because ¹⁴N has burned via
  ¹⁸F→¹⁸O→¹⁹F. Avoid N-rich WN winds and novae (¹⁵N-rich).
- **Host mass ≈ 1–1.3 M☉, massive disk (0.15 M☉, low α ≈ 10⁻⁴)**: the disk is cold enough
  outside to freeze out N2/CO, warm enough inside for an 800 K zone, and has enough dust
  to feed the distillation step. Low turbulence gives deep gaps and strong dust trapping.
- **Mild external FUV only**: strong external photoevaporation would destroy the outer cold traps.

### 2. Strip C, N, O from the gas before it reaches the planet
- **High ionisation** (enhanced cosmic-ray or stellar X-ray flux) slowly converts N2 → NH3/NH4⁺ salts
  and CO → CO2/CH3OH/organics on grains (Eistrup+ 2016/18). This moves N and C from
  ~20 K ices to ~100–150 K ices, which are much easier to cold-trap.
- **Outer rings and planets** (a TW Hya/AS 209-like ring system at ~3–50 AU) trap icy pebbles.
  Gas that flows inward past them is depleted in C, N and O. TW Hya shows CO/H2 lowered by
  10–100×, and ringed disks show weak inner H2O (Banzatti+2020).
- Noble gases (Ne, Ar) can't be filtered. They set a floor on Z of about 0.1×Z☉.

### 3. Planet formation: the "migrating retort"
1. **Small dry core** (~5 M⊕) forms early at ~1 AU, inside the water line, from C-poor
   (enstatite-chondrite-like, S-rich) pebbles. In a thin inner disk the pebble-isolation
   mass is only ~5 M⊕ (∝ h³), so the core stays small and opens a pressure bump early.
   *(Alternative: gravitational-instability fragment with no core. This lowers bulk Z by about 0.3 Z☉.)*
2. **Delay runaway accretion** (dusty, high-opacity envelope) until ~2–3 Myr. By then the
   early pulse of ice vapours (H2O, CO, N2) has drained into the star. The inner viscous
   timescale is ~0.2 Myr at 1 AU for α ≈ 10⁻³.
3. Meanwhile the **outer gap edge traps ~70 M⊕ of dry dust**: FeS, F-apatite, feldspar, silicates, metal.
4. **Runaway gas accretion while migrating inward (type II)** from ~1 AU to ~0.1 AU. The trapped
   dust ring is carried into the 750–950 K window. Wall irradiation of the opened gap and the
   planet's accretion luminosity help heat it.
   **FeS + H2 → Fe + H2S** and **apatite/mica → HF** release S and F into the gas at the gap
   edge, and that gas flows through the gap into the planet. Na, K, Cl, Mg, Si, Fe, Ca and P
   stay in the solid residue. A 4 M_J gap is a very efficient pebble filter (assume 3% leakage).
5. **Stop before 1000 K**: X-ray photoevaporation opens an inner hole and parks the planet at
   ~0.1 AU before its ring reaches the alkali-release line. Inward-diffusing Na/K vapour from
   hotter regions recondenses at the ~1000 K line (cold finger) and never reaches the planet.
6. **No late solid accretion**: the deep gap, no crossing of planetesimal belts, no giant impacts.
   The ring residue turns into rocky planetesimals or falls onto the star.

### 4. Atmospheric levers (if the target is the *observed* photospheric ratio)
At a ≈ 0.1 AU (T_eq ≈ 850–950 K) with high gravity (log g ≈ 3.9):
- **Na2S and KCl clouds cold-trap Na and K** below the photosphere, giving another ≥10–100×
  photospheric depletion. Because Na is so scarce, Na2S uses up a negligible amount of S.
- **Low N → no NH4SH cloud**, so S stays as H2S. **Low O → little SO2.**
- With T > 800 K there are **no S8 hazes** (these form below ~750 K), so S stays in the gas.
- **F stays as HF**: with Na, K and Ca depleted, no NaF, KF or CaF2 sinks form.

## Resulting composition (envelope, `budget.py`)

| | X/H (number) | × solar | [X/H] |
|---|---|---|---|
| **S** | 2.2×10⁻⁴ | **16** | **+1.21** |
| **F** | 6.7×10⁻⁷ | **18** | **+1.26** |
| **N** | 6.0×10⁻⁷ | **0.009** | −2.05 |
| **Na** | 1.2×10⁻⁸ | **0.007** | −2.17 |
| **K** | 1.1×10⁻⁹ | **0.011** | −1.97 |
| C | 1.1×10⁻⁵ | 0.04 | −1.37 |
| O | 5.2×10⁻⁵ | 0.11 | −0.97 |
| Mg, Si | ~1×10⁻⁶ | 0.03 | −1.57 |
| Fe | 4.2×10⁻⁷ | 0.013 | −1.87 |
| Ne | 7.6×10⁻⁵ | 0.9 | −0.05 |

Key ratios:
- **S/N ≈ 360** (solar 0.195) → **~1800× solar**
- **F/(Na+K) ≈ 52** (solar 0.020) → **~2600× solar**
- S/O ≈ 4 (solar 0.027): sulfur becomes the most abundant metal after Ne, ahead of O
- C/O ≈ 0.22
- **Z_env ≈ 0.0071 (0.53 Z☉)**; **Z_bulk ≈ 0.011 (0.82 Z☉)** with a 5 M⊕ core (0.53 Z☉ with no core).
  A typical 4 M_J planet (Thorngren+2016) has Z ≈ 0.09 (~7 Z☉).
- About 72% of Z_env is sulfur, 16% Ne and 9% O. S is the price of high S/H.

## Trade-off knob: how much dust is distilled

| M_ring (M⊕) | [S/H] | [F/H] | Z_env/Z☉ | Z_bulk/Z☉ |
|---|---|---|---|---|
| 10 | +0.37 | +0.42 | 0.20 | 0.50 |
| 25 | +0.77 | +0.82 | 0.28 | 0.58 |
| 40 | +0.97 | +1.02 | 0.37 | 0.66 |
| **70 (fiducial)** | **+1.21** | **+1.26** | **0.53** | **0.82** |
| 100 | +1.37 | +1.42 | 0.69 | 0.98 |
| 150 | +1.54 | +1.59 | 0.96 | 1.25 |

Around 100 M⊕ of distilled dust, S/H reaches ~25× solar while the bulk is still at solar Z.
S/N and F/(Na+K) increase linearly with ring mass.

## Caveats and weakest links
- The **C/N/O removal and the S/F supply pull against each other**. Outer traps that remove ices
  also block refractory pebbles, so the S/F dust has to reach the inner ring *before* the traps
  close, and its ice vapours have to drain away before runaway. This only works with the right
  **timing**.
- About 70 M⊕ of dust is ~40% of all the refractory dust in a 0.15 M☉ metal-poor disk.
  That is aggressive.
- The kinetics of HF release from F-apatite in H2 at 750–950 K are poorly known. F may come out
  more slowly than S.
- Refractory carbon is released at the soot line (~500 K), outside the retort, and can push C back up.
- The host's Fe/S ≈ 1 is just enough to put all S into FeS. Any excess S would already be H2S gas
  (which is harmless here).
- Every step is individually plausible, but their combination is extremely rare. This is an
  end-member planet, not a typical outcome.
