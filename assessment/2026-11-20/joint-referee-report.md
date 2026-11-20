# Review: dualsm (final version, 20 November 2026)

**Reviewers.** First review: Claude Opus 5.5, 19 November 2026. Second referee: Claude Fable 5.2 (xhigh), 20 November, read-only, hand derivation only. This final version merges both and was checked against the repository at the state below.

**Repository state this review matches.** `master` = `origin/master` = `6ec0e1e` (20 Nov 00:26), working tree clean. The science is unchanged since `3281dd9` (18 Nov 19:02). The two later commits only add the no-pull-request rule to `AGENTS.md`.

**Scope.** The five commits of 18 November, all authored by `GPT-6.2 Astra Max`:

| Commit | Subject |
|---|---|
| `c157b0f` | Paper 3: derive the eight-flavour lattice mass-exponent test |
| `7007cd5` | Test the reciprocal Koide claim and the lepton scale response |
| `112798d` | Determine the free coupling in five-flavour electromagnetic matching (closes #1) |
| `d0c7d84` | Paper 3: classify local supercurrents and derive an adjoint lattice test (closes #2) |
| `3281dd9` | Test composite flavour matching beyond a single endpoint channel |

## Verdict

**No wrong result was found by either referee.** Every derivation re-done by hand holds. The open problems are hidden assumptions and omitted data in Paper 3, stale summaries, and missing novelty and review records. The 18 November results are author-checked only. The repository has no "referee pending" marker for them.

## Open actions, ranked

`P3` abbreviates `papers/paper-3-emergent-susy-lattice`. Nothing in this list has been applied in the repository.

### 1. The six-flavour adjoint candidate rests on an unstated assumption (medium)

```
P3/paper.tex:538
6 & $17/2880$ & $41/320$ & fundamental current excluded, adjoint candidate open\\
P3/paper.tex:556
candidate squarks. These checks give kinematically allowed candidates
P3/SUMMARY.md:41
... The local current channel exists and the continuous anomalies and Euler inequality pass. The flow is open.
```

- The SQCD fixed point carries the Konishi scalar $K=Q^\dagger Q+\tilde Q^\dagger\tilde Q$, a singlet under every symmetry the argument uses.
- Second referee's hand estimate (NSVZ with one-loop $\gamma$): $\Delta_K=2+\beta'(\alpha_*)\approx23/7<4$. The estimate is rough at this coupling.
- A relevant $K$ gives the squarks mass and drives SQCD into the scalar-free adjoint theory. A flow from that theory back to the same SQCD point would close a loop and contradict the strict decrease of $a$.
- The candidate therefore survives only if $\Delta_K\ge4$.

**Action:** state this condition beside the table and in `SUMMARY.md`.

### 2. Paper 3 quotes the LSD model-comparison scores and omits the LSD exponent (medium)

```
P3/paper.tex:999
the Akaike information criteria were $33.3$ and $60.1$ respectively.
```

- Table II of arXiv:2305.03665 (read by the second referee) gives $\gamma_*=1.073(28)$ at leading order and $1.207(41)$, $1.200(44)$ at next-to-leading order. The NLO corrections reach 46% of the leading term.
- The hyperscaling power $1/(1+\gamma_*)\approx0.48$ compares with the proposed $8/9$.
- Every number the paper cites lies above $\gamma_m=1/8$: LSD, LatKMI ($0.6$–$1$, from memory) and the paper's own twelve-flavour entries.

**Action:** add $\gamma_*$ to the comparison table and to `P3/SUMMARY.md:60`, and say that existing fits disfavour $1/8$ unless the simulated masses lie far from scaling.

### 3. The title contradicts the paper's own proposition (medium)

```
P3/paper.tex:81
\title{\textbf{Lattice Signatures of Emergent Supersymmetry\\
P3/paper.tex:439
Equality of one mass exponent remains a testable, weaker hypothesis.
index.html:39
... lattice signatures of emergent SUSY, and the number of generations.</p>
```

The paper excludes the emergent-supersymmetry mechanism for fundamental-only QCD and excludes the same-rank SQCD endpoint at $N_f=7,8$ by the Euler anomaly. After that, a slope $32/9$ would be a coincidence of exponents. `papers/RESEARCH-PLAN.md:25` still frames the test as "the emergent-SUSY scenario vs the confining scenario".

**Action:** retitle, and call $1/8$ a benchmark with no supporting mechanism in the abstract, the site index and the research plan.

### 4. Three SUMMARY files contradict their papers (medium)

| File | Says | Paper says |
|---|---|---|
| `papers/paper-2-meson-mass-sum-rules/SUMMARY.md:9,47` | "verified at 8%", "ratio = 0.92 (8% accuracy)" | `paper.tex:83`: "$m_s m_t/m_b^2 = 1.13$, so the relation holds at the $13\%$ level" |
| `papers/paper-4-generation-number/SUMMARY.md:8` | "Kutasov-Schwimmer with k >= 2 admits no integer generation number" | `paper.tex:112-113`: "The SO route and Kutasov--Schwimmer duality with $k \geq 2$ also contain $\ngen = 3$" |
| `papers/paper-1-sp-duality-sm/SUMMARY.md:16` | "Intriligator-Seiberg hep-th/9506101" | `paper.tex:9,1040`: Intriligator–Pouliot hep-th/9505006 |

The Paper 2 summary still ends "## Self-Check: PASSED" (line 76). Commit `112798d` edited that file and left the headline.

**Action:** regenerate the three summaries from the current sources.

### 5. No root README and no novelty status (medium)

`git log -- README.md` is empty. The standing instruction is that every project says what is new, known, conditional or unreviewed. Reading of the 18 November results after both reviews:

| Result | Status |
|---|---|
| Five-flavour matching leaves $g_Y$ free, ratio $\propto g_Y^{-3}$ | Negative result, elementary once posed. The spectator coupling is free by construction (`papers/paper-2-meson-mass-sum-rules/FIVE-FLAVOUR-MATCHING.md:57`). Unreviewed. |
| Reciprocal-Koide unique spectrum $(r^{-2},1,r^2)$ | Elementary algebra, source unknown. The cited PLB paper (arXiv:2606.10060) does not contain it, and one search found no prior statement. |
| Rank-two lift leaves Koide at first order; seesaw line test | New as stated, elementary, unreviewed. |
| Correction to the sBootstrap Goldstino example | A correct correction of earlier own work, using standard Nelson–Seiberg facts. |
| Paper 3 supercurrent exclusion (baryon number, $C$, flavour centre) | Plausibly new in this packaging. Three searches found no prior statement. Issue #2 itself says priority is unestablished. Unreviewed. |
| Paper 3 Euler-anomaly exclusion of $N_f=7,8$ same-rank endpoints | Direct application of the $a$-theorem with the standard SQCD $a$. Unreviewed. |

**Action:** add a root README carrying this table.

### 6. The review record stops at the March text (low)

- `assessment/` holds a layered review record (`papers/`, `audit/`, `adjudication/`, `reassessment/` and `FINAL-SCORECARD.md`). It describes the March version of Paper 3: `assessment/FINAL-SCORECARD.md:40` still gives `REVISE` for the old text.
- Commit `c157b0f` added one correction banner, at `assessment/reassessment/papers/paper-3-emergent-susy-lattice.md:7`.
- The new proposition of `d0c7d84` ("a vacuum preserving baryon number and unitary charge conjugation $C$ cannot carry exactly one Weyl Poincaré supercharge") appears in the PDF with no sign that it is unrefereed.
- Issues #1 and #2 were closed on the day they were answered.

**Action:** add a dated review layer under `assessment/` for the 18 November work and link the referee reports from it.

### 7. The target ratio should state its inputs and error (low)

```
papers/paper-2-meson-mass-sum-rules/FIVE-FLAVOUR-MATCHING.md:3
The target is $R_\ell=[(m_e+m_\mu+m_\tau)/6]/[\alpha(0)\sqrt{M_Z^2-M_W^2}]\simeq0.9980$, using the tabulated direct line-shape masses. Replacing the numerator with $(m_p+m_n)/6$ gives $0.9952$.
```

- Issue #1 names the source: PDG 2026 electroweak inputs, $M_W=80.3625(77)$ and $M_Z=91.1879(20)$ GeV (`~/pdghist/data/2026/electroweak.yaml:36-48`).
- By hand: $\sqrt{M_Z^2-M_W^2}\,\alpha(0)=314.473$ MeV, so the two ratios are $0.99802$ and $0.99523$. The quoted values reproduce.
- The fourth digit follows $M_W$: $\delta R/R=M_W\,\delta M_W/(M_Z^2-M_W^2)=3.3\times10^{-4}$, so $R_\ell=0.9980(3)$. A 9 MeV shift of $M_W$ moves $R_\ell$ by $4\times10^{-4}$.

**Action:** name the inputs and quote $R_\ell=0.9980(3)$.

### 8. The O'Raifeartaigh correction exists only in this repository (low)

```
related-papers/phys3_sbootstrap_v4d.tex:1854
term $\delta W \sim \varepsilon\,\Phi_0\Phi_2$) lifts the goldstino
index.html:47
<p>Frozen 2026-03-22 snapshot: 37 TeX sources with PDFs ...
```

The mirrored manuscript still states the goldstino mass $m_0\sim\varepsilon^2/m$, which `papers/COMPOSITE-FLAVOUR-MATCHING.md` corrects. The banner in `related-papers/README.md` is good. The Paper 3 mirror in that folder was rewritten on 18 November, so "frozen" is inaccurate.

**Action:** fix the manuscript in its home repository and reword "Frozen".

### 9. Citations (low)

- `P3/paper.tex:203` cites `Appelquist1988` (the 1986 walking paper, bibitem at line 1211) for $N_f^*\approx4N_c$. That estimate belongs to Appelquist–Terning–Wijewardhana 1996 (from memory).
- Anber–Lohitsiri–Sulejmanpasic, arXiv:2306.01849 (abstract read), study the same adjoint-plus-fundamental theory and are absent.
- `lectures/lecture-11.tex:767,771` cite two chatgpt.site pages as bibliography entries (`AlphaVacuum`, `AlphaShape`). **Action:** archive that content in a repository and cite the archive.

### 10. Smaller points (low)

- `lectures/lecture-06.tex:585` still says "Whether emergent SUSY survives at **finite** $N_c$ and $N_f$ ... is an **open question**", with no pointer to Paper 3's obstruction for fundamental-only $(3,6)$. **Action:** add a cross-reference.
- `papers/COMPOSITE-FLAVOUR-MATCHING.md` ends with a paragraph on Euclid I.29 and the parallel postulate. It adds nothing to the physics and could go.
- For odd $N_f$ the charge-conjugation argument leaves the case of two same-chirality supercharges exchanged by $C$ untested at $N_f=5,7$. The paper says so at `P3/paper.tex:493-495`; the SUMMARY table cell could repeat it.

## What was verified by hand

Both referees re-derived the items below and agree.

**`papers/COMPOSITE-FLAVOUR-MATCHING.md`**

- Koide branch $b(a)=2(1+a)+\sqrt{3(1+4a+a^2)}$, with $b(0)=2+\sqrt3$ and $b'(0)=2+2\sqrt3$.
- Rank-two lifting gives $m_e=\epsilon^2\lVert Bn\rVert^2+O(\epsilon^4)$, hence $db/da=0$ at onset. The explicit counterexample $\mathrm{diag}(\epsilon^2,1,b(\epsilon)^2)$.
- $Q=9s^2/(3s^2+6\lvert c\rvert^2)$, the light amplitude $s(1-\cos\epsilon+\sin\epsilon)$ and the heavy endpoints $s(3\mp\sqrt3)/2$.
- The projection identity $P\mathcal Y^2P-(P\mathcal YP)^2=[(1-P)\mathcal YP]^\dagger[(1-P)\mathcal YP]$.
- The Riemann–Roch kernel $h^0(L(-p-q))=1$.
- The seesaw block relation $m_+^2+m_-^2=M^2+\frac{\lvert h_L\rvert^2+\lvert h_R\rvert^2}{\lvert h_Lh_R\rvert}m_+m_-$, with slope $\ge2$.
- The O'Raifeartaigh correction: the supersymmetric vacua $A^2=-f/3g$, $X=-mA/\epsilon$, $B=-2f/(3\epsilon)$ solve all three F-equations. For $\epsilon\ne0$ the old background fails stationarity, $W_{ij}\bar F_j=(\epsilon^2v,\,m\epsilon v,\,\epsilon f)$.
- The double-ratio factorization criterion for a $2\times3$ weight array.

**`papers/paper-2-meson-mass-sum-rules/FIVE-FLAVOUR-MATCHING.md`**

- Hypercharges from $Y=t_f+B/15$: quarks $2/3,-1/3$, magnetic $q_U,q_D=\mp1/2$.
- The mass matrix $f^2dd^T$, the inverse-propagator decomposition, and $e^{-2}$, $M_N^2$, $M_C^2$.
- $\Pi_Y=f^2/(t+g_m^2f^2)$ from integrating out $a_3$.
- Infrared count $\sum Q'^2=8+2+2=12$. It also follows on the magnetic side, where the surviving $q_i$ component has $Q'=\tfrac12+Y=(0,0,1,1)$.
- Branch superpotential $W=-2S+\operatorname{tr}mM$, $S^3=\Lambda^4\det m$, Hessian $m_im_j/S$.
- The counterexample ratio $4\pi\Sigma_u(g_w^2+g_Y^2)/(3v_wg_w^2g_Y^3)$, and the meson weights $(12,6,6)=2\,(6,3,3)$.

**`lectures/lecture-11.tex`**

- The positive arc $0\le\delta\le\pi/12$ with $\delta=2/9$ inside it; $e_3=\frac{z_0^3}{2}(\sqrt2\cos3\delta-1)$; the degree-five reduction to $a+be_3$.
- Direct plus reciprocal Koide gives $t^3-6t^2+6t-1=(t-1)(t^2-5t+1)$, hence the unique spectrum $(r^{-2},1,r^2)$ with $r=(5+\sqrt{21})/2$. At $\delta=2/9$ the ratios are $0.0048366$ and $0.059460$, and $Q(1/m_d,1/m_s,1/m_b)=1.5046$.

**`P3/paper.tex` and `P3/SUMMARY.md`**

- $R(Q)=5/8$, $\Delta_{F_M}=23/8$, $y_m=9/8$, $\gamma_m^*=1/8$, and the general $\gamma_m^*=(3N_c-N_f)/N_f$.
- Mode-number slope $32/9$, $\rho\propto\lambda^{23/9}$, $\lvert x\rvert^{-23/4}$, $m^{8/9}$.
- The proposition: $(-1)^F=(-1)^{N_cB}$, the flavour-centre condition $N_f\mid N_cB$, the $-\mathbf 1_8$ argument and the $C$ step $b=-b$.
- The mixed anomalies $\operatorname{Tr}B\,SU(N_f)^2_{L,R}=\pm1/2$ and $\operatorname{Tr}R_*SU(N_f)^2=-N_c^2/2N_f$, forcing $b=0$, $u=1$.
- The Euler table in exact fractions: $106/225$, $17/2880$, $-2101/8820$, $-3359/9216$ and $89/150$, $41/320$, $-341/2940$, $-3721/15360$; $a_{\rm UV}=19/9$, $a_{\rm SQCD}=2535/1024$, soft UV $5/2$.
- The adjoint-plus-six example: $b_0=5$, $b_1=-22$, $\alpha_*=10\pi/11$, zero colour anomaly of $X$, the $X$ charges of $O$, $P$ and $\lambda\psi$, and the power laws $\lvert x\rvert^{-3}$, $\lvert x\rvert^{-5}$.
- Two-loop QCD $\gamma_m$ at the Banks–Zaks zero: $4.19$ ($N_f=10$), $0.77$ ($N_f=12$), no zero at $N_f=8$.

**`papers/RESEARCH-PLAN.md:45-53`** (second referee): $\Lambda_3=\Lambda_6^{7/9}(m_tm_bm_c)^{2/27}$ and the slopes $2/9$, $-7/9$.

Before the user's instruction to stop running programs: `scripts/verify_koide_vev.py` passed 57/57, and `paper.tex`, `lecture-11.tex` and `exercise-09.tex` rebuilt without undefined references in a scratch copy. The Paper 3 mirror in `related-papers/` is byte-identical to its source (`cmp`).

## Limits of this review

- The Konishi estimate of action 1 is a rough one-loop evaluation at strong coupling, and its decoupling step is uncontrolled.
- Sources read directly by the second referee: arXiv:2305.03665 Tables I–II; the abstract pages of 1105.1510, 2306.01849 and 2606.10060 (plus its HTML); issues #1 and #2; the local pdghist file. Cited from memory: Tanizaki's faithful group, Anselmi–Grisaru–Johansen, Appelquist–Terning–Wijewardhana, Ryttov–Shrock and the LatKMI values.
- Not checked: statements resting on conneskk (interval-length scaling, Berger radius, Lemma 52) and on the alphaology site; AMPS eq. (2) and the bound $\gamma_m\le1$; the PDFs against their sources after the 18 November edits.
- Priority was checked by three searches only.
