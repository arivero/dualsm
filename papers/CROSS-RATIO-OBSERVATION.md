# A numerical observation on the two charged-meson cross-ratios

**Status.** Numerical observation, found on 26 November 2026 after the comparison had been made. It was not registered beforehand and no structure is known that hosts it. It is recorded here so that it can be tested, and it carries the weight of a coincidence until a hosting structure and a second consequence are found. Unreviewed. [Rule for coincidences](../AGENTS.md#what-counts-as-progress)

## The observation

For the six charged pseudoscalar mesons, labelled by their quark content, form the two cross-ratios of the [five-flavour matching note](paper-2-meson-mass-sum-rules/FIVE-FLAVOUR-MATCHING.md#what-six-charged-masses-test):
$$
 R_{ds}=\frac{M_{\pi^+}M_{D_s^+}}{M_{K^+}M_{D^+}},\qquad
 R_{db}=\frac{M_{\pi^+}M_{B_c^+}}{M_{B^+}M_{D^+}} .
$$

| Meson | Quarks | Mass (MeV) |
|---|---|---|
| $\pi^+$ | $u\bar d$ | $139.57039\pm0.00018$ |
| $K^+$ | $u\bar s$ | $493.6766\pm0.0154$ |
| $B^+$ | $u\bar b$ | $5279.406\pm0.071$ |
| $D^+$ | $c\bar d$ | $1869.661\pm0.048$ |
| $D_s^+$ | $c\bar s$ | $1968.351\pm0.069$ |
| $B_c^+$ | $c\bar b$ | $6274.47\pm0.32$ |

These masses give $\log R_{ds}=-1.21187$ and $\log R_{db}=-2.42227$, and
$$
 \frac{\log R_{ds}}{\log R_{db}}=0.50030\pm0.00002 ,
$$
which rounds to 0.5003. The value lies within 0.06 per cent of $1/2$, so that $R_{db}\approx R_{ds}^2$.

The relation is approximate. Solving $R_{db}=R_{ds}^2$ for the $B_c$ mass with the other five masses gives $6265.2\pm0.6$ MeV, against the measured $6274.47\pm0.32$ MeV. The difference is 9.3 MeV, or 1.5 per mille, and it is 13 standard deviations of the measurement errors. Exact equality with $1/2$ is therefore excluded by the data.

The same relation separates a light side from a heavy side:
$$
 \frac{M_K^2}{M_\pi}=1746.2\ \text{MeV},\qquad
 \frac{M_{D_s}^2M_B}{M_DM_{B_c}}=1743.6\ \text{MeV}.
$$

Masses: Particle Data Group, 2025 update of the Review of Particle Physics, fit values of the summary tables (S. Navas et al., Phys. Rev. D 110, 030001 (2024) and 2025 update), read from the PDG database file `pdgall-2025-v0.2.2.sqlite`. The uncertainty of the ratio is dominated by the $B_c$ mass.

## How it was found and how many relations were tried

The [proposition on the order of departure](paper-2-meson-mass-sum-rules/FIVE-FLAVOUR-MATCHING.md#the-first-departure-from-factorization) gives both logarithms the same coefficient $C$ near the flavour-symmetric point, so the ratio of the two logarithms is the one combination of the six masses that is free of $C$ at leading order. That single combination was evaluated with measured masses, as an orientation, while issue 5 was being evaluated. The proximity to $1/2$ was noticed after the number had been computed.

One statistic was examined. For a ratio that could plausibly fall anywhere between 0.3 and 0.7, the chance of landing within 0.0003 of one of the fractions $1/3$, $1/2$, $2/3$ is about 0.5 per cent. This figure leaves out the freedom in the choice of statistic.

## What the model gives

**Leading order.** The proposition gives $\log R_{ds}/\log R_{db}\to\Delta_{ds}/\Delta_{db}$ with $\Delta_{ij}=\log(m_i/m_j)$. With the quark masses of the Review ($m_u=2.16$, $m_d=4.70$, $m_s=92.9$ MeV at 2 GeV, $m_c(m_c)=1.2729$ GeV, $m_b(m_b)=4.186$ GeV) the right side is 0.44, and 0.43 when $m_b$ and $m_c$ are run roughly to 2 GeV. The measured ratio is 14 to 17 per cent higher. The physical masses lie far from the symmetric point, with $\Delta_{uc}\approx-6.3$, so the leading order has no claim to apply. Read at leading order all the same, the two measured logarithms would give $C=-0.064$ and $C=-0.056$.

**Classical meson metric.** For the metric $1/(h_i+h_j)$ of the same note the cross-ratios are exact functions of the quark masses,
$$
 R_{jk}=\frac{(m_u+m_j)(m_c+m_k)}{(m_u+m_k)(m_c+m_j)} ,
$$
and the ratio of logarithms is 0.52. The logarithms themselves are $-2.56$ and $-4.96$, about twice the measured ones (the measured values are 0.47 and 0.49 of them). With this metric the canonical mass of a pair is proportional to $m_a+m_j$. The light pseudoscalars obey $M^2\propto m_a+m_j$ (Gell-Mann, Oakes and Renner, a known result), which accounts for a factor near one half in the logarithms of the light pairs.

Neither value reproduces 0.5003. The model, as it stands, hosts no relation $R_{db}=R_{ds}^2$.

## A second consequence, tested

If the relation came from a flavour structure common to the meson multiplets, the vector mesons would show it too. With $D^{*+}$ (2010.264 MeV), $D_s^{*+}$ (2112.194 MeV), $B^*$ (5324.745 MeV), $\rho^+$ and $K^{*+}$ near 775 and 892 MeV, and the unmeasured $B_c^*$ placed anywhere from the $B_c$ mass to 300 MeV above it, the vector ratio of logarithms lies between 0.10 and 0.14. The value $1/2$ would need a $B_c^*$ of 11.5 GeV. The vector multiplet does not share the relation.

The proximity to $1/2$ is therefore specific to the pseudoscalars, where the pion and the kaon are light for chiral reasons. This points to the physical values of the light-quark masses and the chiral scale, and away from a Kähler structure common to all pairs.

## What would give it weight

- **A hosting structure.** A metric or mechanism, evaluated at the physical mass ratios without expansion, that yields 0.5003 and fixes $C$. The meson Kähler metric on the full-rank branch at $(3,5)$ is the open input of issue 5, and this number is a target for it.
- **A second consequence at other quark masses.** Lattice QCD ensembles with a varied strange or charm mass give the six masses away from their physical values. A structural relation keeps the ratio at $1/2$ as the masses move. Chiral and heavy-quark scaling make it drift. This test decides between the two readings.
- **The dictionary.** The comparison identifies the canonical masses of the model with physical meson masses. That identification is a hypothesis of this line of work and is untested.

All six masses are measured, so the relation predicts no new number as it stands.

## Reproduce

`python3 scripts/verify_cross_ratio_observation.py` (Python 3, standard library) recomputes every number above: the ratio with its propagated uncertainty, the $B_c$ mass from the other five, the leading-order and classical-metric values and the vector analogue.

[Issue 5](https://github.com/arivero/dualsm/issues/5)
