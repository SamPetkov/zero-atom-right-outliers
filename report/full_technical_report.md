# Right-outlier theory for self-coupled sample covariance matrices with zero diagonal weights

**Author:** Samuil Petkov  
**Status:** research manuscript/preprint; not peer reviewed  
**License:** CC BY 4.0  
**AI-use disclosure:** OpenAI GPT-5.6 Pro assisted substantively under the author's direction; the author remains responsible for independent verification.

**Resolution date:** 20 July 2026  
**Status:** Complete resolution of the stated nonnegative zero-gap theorem.  
**Proof mechanism:** Exact active-column reduction plus a marked extension of the invertible-weight theorem of Ben Arous–Gheissari–Huang–Jagannath.

---

## 1. Exact theorem statement

Let the model, fixed parameters, geometric realization, Gaussian-mixture columns, and measurable weights \(h_b:\mathbb R^q\to[0,M]\) be as in the problem statement. Assume

\[
h_b(g)\in \{0\}\cup[\tau,M]\quad\text{a.s.}
\]

for a fixed \(\tau>0\), and put

\[
\pi_b=\mathbb P\{h_b(g)>0\},\qquad
\pi=\sum_{b=1}^k p_b\pi_b.
\]

Write

\[
v_b(g)=m_b+\lambda^{-1/2}g,
\qquad
B_G(z)=zI_q-F_G(z).
\]

The Stieltjes-transform convention is

\[
S_\mu(z)=\int_{\mathbb R}\frac{1}{x-z}\,\mu(dx).
\]

### Theorem 1.1 — zero-atom right-outlier theorem

If \(\pi=0\), then \(D=0\) and \(M_d=0\) almost surely. In this case

\[
\nu_G=\delta_0,\qquad S_G(z)=-z^{-1},\qquad F_G(z)=0,
\]

and every assertion below is trivial.

Assume henceforth that \(\pi>0\). Then the following hold.

#### (a) Bulk law and zero atom

The empirical spectral distribution of

\[
M_d=\frac1nA_dDA_d^\top
\]

converges weakly, in probability and on the natural product coupling almost surely, to the probability measure \(\nu_G\) whose Stieltjes transform is the physical solution of

\[
1+zS_G(z)
=
\phi\sum_{b=1}^k p_b
\mathbb E\!\left[
\frac{S_G(z)h_b(g)}
{\lambda\phi+S_G(z)h_b(g)}
\right].
\tag{1.1}
\]

Moreover,

\[
\nu_G(\{0\})=(1-\phi\pi)_+.
\tag{1.2}
\]

Let

\[
\lambda_+(G)=\sup\operatorname{supp}\nu_G.
\]

#### (b) Effective matrix and absence of hidden poles

For every compact \(K\subset(\lambda_+(G),\infty)\),

\[
\inf_{\substack{z\in K\\b\in[k]\\g:\,h_b(g)>0}}
\left|\lambda\phi+S_G(z)h_b(g)\right|>0
\]

after replacing the pointwise infimum over \(g\) by the essential infimum. Hence

\[
F_G(z)
=
\lambda\phi\sum_{b=1}^k p_b
\mathbb E\!\left[
\frac{h_b(g)}
{\lambda\phi+S_G(z)h_b(g)}
v_b(g)v_b(g)^\top
\right]
\tag{1.3}
\]

is real analytic on \((\lambda_+(G),\infty)\).

#### (c) Outlier counting on compact right intervals

Let \(I=[a,b]\) satisfy

\[
\lambda_+(G)<a<b<\infty,
\qquad
\det B_G(a)\ne0,
\qquad
\det B_G(b)\ne0.
\]

Then

\[
\#\{\text{eigenvalues of }M_d\text{ in }I\}
=
\#\{z\in I:\det B_G(z)=0\}
\tag{1.4}
\]

with probability tending to one. Eigenvalues and zeros are counted with algebraic and analytic multiplicity, respectively.

#### (d) Right-root multiplicity

For every root \(z_*>\lambda_+(G)\),

\[
m_*:=\operatorname{ord}_{z_*}\det B_G(z)
=
\dim\ker B_G(z_*).
\tag{1.5}
\]

In particular, every right root has finite multiplicity, and the sum of all right-root multiplicities is at most \(q\).

#### (e) Existence and convergence of empirical outliers

If \(z_*>\lambda_+(G)\) is a root of multiplicity \(m_*\), then for every sufficiently small fixed \(\delta>0\),

\[
\#\{\sigma(M_d)\cap(z_*-\delta,z_*+\delta)\}=m_*
\tag{1.6}
\]

with probability tending to one. Every eigenvalue in this interval converges in probability to \(z_*\).

#### (f) No spurious right outliers

For every \(\epsilon>0\), there is a deterministic \(K<\infty\) such that

\[
\mathbb P\{\|M_d\|\le K\}\longrightarrow1
\]

and, with

\[
Z_{\epsilon,K}
=
\{z\in[\lambda_+(G)+\epsilon,K]:\det B_G(z)=0\},
\]

\[
\sup_{\substack{\lambda_j(M_d)>\lambda_+(G)+\epsilon}}
\operatorname{dist}(\lambda_j(M_d),Z_{\epsilon,K})
\xrightarrow{\mathbb P}0.
\tag{1.7}
\]

If \(Z_{\epsilon,K}=\varnothing\), the assertion means that with probability tending to one there is no eigenvalue above \(\lambda_+(G)+\epsilon\).

#### (g) Simple-root eigenvectors

Suppose \(z_*\) is a simple root. Let \(z_d\to z_*\) be the unique associated empirical eigenvalue and let \(u_d\) be a unit eigenvector. Put

\[
r_d=L_d^\top u_d.
\]

Then

\[
\|B_G(z_d)r_d\|=o_{\mathbb P}(1),
\tag{1.8}
\]

and

\[
\left|
\|r_d\|^2-\langle r_d,\partial_zF_G(z_d)r_d\rangle-1
\right|
=o_{\mathbb P}(1).
\tag{1.9}
\]

If \(e_*\) is either unit vector spanning \(\ker B_G(z_*)\), define

\[
r_*=
\frac{e_*}
{\sqrt{\langle e_*,B_G'(z_*)e_*\rangle}}.
\tag{1.10}
\]

After choosing the sign by \(\langle r_d,e_*\rangle\ge0\),

\[
r_d\xrightarrow{\mathbb P}r_*.
\tag{1.11}
\]

Equivalently,

\[
B_G(z_*)r_*=0,
\qquad
\|r_*\|^2-\langle r_*,F_G'(z_*)r_*\rangle=1.
\tag{1.12}
\]

#### (h) Multiple roots: spectral-projection statement

Let \(z_*\) have multiplicity \(m_*>1\), and choose \(\delta>0\) so that the closed interval

\[
[z_*-\delta,z_*+\delta]
\]

contains no other effective root and does not meet \(\operatorname{supp}\nu_G\). Let

\[
\Pi_d=\mathbf 1_{(z_*-\delta,z_*+\delta)}(M_d)
\]

be the full-space spectral projection. Put

\[
K_*=\ker B_G(z_*),\qquad P_*=\operatorname{Proj}_{K_*},
\]

and

\[
J_*=
\left.P_*B_G'(z_*)P_*\right|_{K_*}.
\tag{1.13}
\]

Then \(J_*\) is positive definite, \(\operatorname{rank}\Pi_d=m_*\) with probability tending to one, and

\[
\left\|
L_d^\top\Pi_dL_d
-
Q_*
\right\|
\xrightarrow{\mathbb P}0,
\qquad
Q_*:=P_*J_*^{-1}P_*.
\tag{1.14}
\]

If \(U_d\in\mathbb R^{d\times m_*}\) is any orthonormal basis of
\(\operatorname{ran}\Pi_d\) and \(R_d=L_d^\top U_d\), then

\[
R_dR_d^\top\xrightarrow{\mathbb P}Q_*.
\tag{1.15}
\]

Consequently, after subsequences and arbitrary right rotations in
\(O(m_*)\), every limit \(R\) satisfies

\[
\operatorname{ran}R=K_*,
\qquad
RR^\top=Q_*,
\qquad
R^\top B_G'(z_*)R=I_{m_*}.
\tag{1.16}
\]

No convergence of individual eigenvectors is asserted.

#### (i) Exact rank and kernel

For every finite \(d\), almost surely,

\[
\operatorname{rank}(M_d)=\min(d,N_{\mathrm{active}}),
\tag{1.17}
\]

where

\[
N_{\mathrm{active}}=\sum_{\ell=1}^n\mathbf 1_{\{D_{\ell\ell}>0\}}.
\]

Therefore,

\[
\dim\ker M_d=d-\min(d,N_{\mathrm{active}})
\tag{1.18}
\]

almost surely and

\[
\frac1d\dim\ker M_d
\longrightarrow
(1-\phi\pi)_+
\tag{1.19}
\]

almost surely. These exact zero eigenvalues constitute the atom (1.2); they are not positive outliers.

---

## 2. Complete model and notation

For each \(d\), let

\[
B_d=[x_1^{(d)},\ldots,x_C^{(d)},\mu_1^{(d)},\ldots,\mu_k^{(d)}]
\in\mathbb R^{d\times q},
\qquad
B_d^\top B_d=G,
\]

and let \(L_d\in\mathbb R^{d\times q}\) have orthonormal columns with

\[
L_d^\top B_d=\sqrt G.
\]

No inverse of \(G\) or \(\sqrt G\) will be used. In particular, \(G\) may be rank deficient and the unused columns of \(L_d\) may point outside \(\operatorname{span}B_d\).

For class \(b\), let \(m_b=L_d^\top\mu_b^{(d)}\), the corresponding column of \(\sqrt G\). A sample is

\[
Y_\ell
=
L_d\bigl(m_{b_\ell}+\lambda^{-1/2}g_\ell\bigr)
+
\lambda^{-1/2}L_d^\perp w_\ell,
\]

where

\[
b_\ell\sim\operatorname{Cat}(p_1,\ldots,p_k),\quad
g_\ell\sim N(0,I_q),\quad
w_\ell\sim N(0,I_{d-q})
\]

are mutually independent over all \(\ell\). Define

\[
T_\ell=h_{b_\ell}(g_\ell),\qquad
I_\ell=\mathbf 1_{\{T_\ell>0\}},
\qquad
N_d=\sum_{\ell=1}^n I_\ell.
\]

After a column permutation,

\[
A_d=[A_{+,d}\ A_{0,d}],
\qquad
D=\begin{bmatrix}D_{+,d}&0\\0&0\end{bmatrix},
\]

where \(D_{+,d}\) is \(N_d\times N_d\) and

\[
\tau I\preceq D_{+,d}\preceq MI.
\]

The exact identity driving the proof is

\[
M_d
=
\frac1nA_{+,d}D_{+,d}A_{+,d}^\top
=
\frac{N_d}{n}\widehat M_d,
\qquad
\widehat M_d
=
\frac1{N_d}A_{+,d}D_{+,d}A_{+,d}^\top.
\tag{2.1}
\]

The inactive columns disappear algebraically. They are never inverted and never enter a Schur complement.

---

## 3. Current literature and novelty audit

### 3.1 Audit date and search scope

The literature search was carried out through **20 July 2026**. Searches covered:

1. the exact SolveAll title;
2. the current versions and citations of arXiv:2502.15655;
3. singular or Bernoulli diagonal weights in weighted covariance matrices;
4. variance laws with an atom at zero;
5. spiked covariance with missing observations;
6. anisotropic local laws for singular weighted covariance matrices;
7. ReLU Hessian and Gauss–Newton outliers;
8. gated and truncated Gaussian covariance matrices;
9. finite-rank deformations of singular sample covariance matrices;
10. pseudoinverse linearizations;
11. 2026 and July 2026 preprints.

The search used arXiv, PMLR/COLT proceedings, the source paper’s bibliography and citation links, and the SolveAll listing. Absence from these searches is not a proof of novelty.

### 3.2 Primary source

The current source is:

> Gérard Ben Arous, Reza Gheissari, Jiaoyang Huang, and Aukosh Jagannath,  
> “Local geometry of high-dimensional mixture models: Effective spectral theory and dynamical transitions,”  
> arXiv:2502.15655v3, revised 22 January 2026.

The source proves the bulk law under its coupling assumption and proves outlier/eigenvector equations under an additional non-degeneracy assumption excluding mass near zero. It explicitly states that ReLU is excluded because the derivative vanishes on a half-line and that zero entries must be handled separately before the full-rank method is applied.

### 3.3 Closest pre-existing zero-weight result

The closest primary source located is:

> Filip Kovačević, Yihan Zhang, and Marco Mondelli,  
> “Spectral Estimators for Multi-Index Models: Precise Asymptotics and Optimal Weak Recovery,”  
> arXiv:2502.01583; Proceedings of COLT 2025, PMLR 291.

Their Assumption (A5) requires only that the preprocessing function be bounded and not identically zero:

\[
T\ \text{bounded},\qquad \mathbb P\{T(y)=0\}<1.
\]

Thus their theory already permits a positive atom at zero. They prove limits of the top signal-bearing eigenvalues and eigenspace overlaps, including multiplicity, for centered Gaussian multi-index spectral estimators.

This means that the broad statement

> “self-coupled spectral outlier theory with exact zero preprocessing weights is new”

would be false.

Their model is nevertheless not the theorem proved here: it is centered Gaussian, uses a different finite-rank signal parameterization and determinant, and addresses the leading signal eigenvalues rather than every compact interval outside the bulk of the noncentered Gaussian-mixture model.

### 3.4 Other relevant 2026 sources

Two technically relevant 2026 works located were:

* Zhou Fan, Renyuan Ma, Elliot Paquette, and Zhichao Wang,  
  “Anisotropic local law for non-separable sample covariance matrices,”  
  arXiv:2602.17960.  
  This develops general local laws for non-separable sample covariance vectors, including nonlinear tilts, but does not state the present self-coupled finite-rank zero-atom determinant theorem.

* Andrea Montanari and Basil Saeed,  
  “Variational Formulas for the Spectrum of Block Wishart Matrices,”  
  arXiv:2606.27774.  
  This gives bulk-edge and logarithmic-potential formulas for block-Wishart models; it is not an outlier/eigenspace theorem for the present coupled mixture model.

Searches of missing-observation covariance papers, ordinary spiked/separable covariance papers, ReLU Hessian papers, and truncated-Gaussian inference papers produced models that did not match the self-coupled column-weight problem.

### 3.5 Novelty conclusion

The defensible conclusion is:

*The exact theorem in Section 1 was not located in the primary literature searched through 20 July 2026. Broad novelty is not claimed, because Kovačević–Zhang–Mondelli already allow exact zero preprocessing weights in a related self-coupled Gaussian multi-index model, and the primary source itself indicates the correct active-column idea.*

---

## 4. Reconstruction of the existing invertible-\(D\) theorem

### 4.1 Source theorem

For fixed summary statistics, the source considers

\[
\frac1nADA^\top
\]

with \(D_{\ell\ell}\) coupled to the low-dimensional projection of column \(Y_\ell\). Its Theorem 1.10 gives the limiting bulk under the coupling assumption. Theorem 1.11 gives exact eigenvalue counts outside the bulk and projected-eigenvector equations when the law of \(D_{\ell\ell}\) is compactly supported and has no mass approaching zero.

The scaled form used in the proof is

\[
H_d=\frac{\lambda}{d}ADA^\top.
\]

If \(\widetilde S\) is its bulk Stieltjes transform and \(T=D_{\ell\ell}\), the fixed-point equation is

\[
1+z\widetilde S(z)
=
c\,\mathbb E\!\left[
\frac{\widetilde S(z)T}{1+\widetilde S(z)T}
\right],
\qquad c=\lim\frac nd,
\tag{4.1}
\]

and the finite-dimensional matrix is

\[
\widetilde F_c(z)
=
\lambda c\,\mathbb E\!\left[
\frac{T}{1+\widetilde S(z)T}VV^\top
\right].
\tag{4.2}
\]

### 4.2 Where \(D^{-1}\) occurs

The source proof uses \(D^{-1}\) in four places.

| Source location | Use of \(D^{-1}\) | Replacement here |
|---|---|---|
| Weighted-Wishart linearization and local law, Sections 2.4–2.5 | Lower-right linearization block \( -D^{-1}\) | Apply only to \(D_+\), for which \(D_+^{-1}\) exists and \(\|D_+^{-1}\|\le\tau^{-1}\) |
| Characteristic determinant, Section 2.10 | Schur complement of the active weighted-Wishart block | Same Schur complement on active coordinates |
| Eigenvector equation, Section 2.11 | Relation between the primal eigenvector and linearization vector | Same relation with \(D_+\) |
| Norm/derivative identity, Section 2.12 | Derivative of the active Schur complement | Same identity with \(D_+\) |

The bulk proof precedes these inversions and does not require \(D^{-1}\).

### 4.3 Marked invertible-weight extension

The active conditional distribution is not an ordinary Gaussian mixture. The precise extension needed is therefore the following.

#### Proposition 4.1 — invertible weighted covariance with arbitrary fixed-dimensional marks

Let \(m_d/d\to c\in(0,\infty)\). Let \((T_i,V_i)_{i\le m_d}\) be i.i.d., with

\[
T_i\in[\tau,M]\quad\text{a.s.},\qquad
V_i\in\mathbb R^q,\qquad
\mathbb E\|V_i\|^r<\infty\ \text{for every }r<\infty.
\]

Let \(W_i\sim N(0,I_{d-q})\) be i.i.d. and independent of all marks. Define

\[
Y_i=LV_i+\lambda^{-1/2}L^\perp W_i
\]

and

\[
\widehat M_d=\frac1{m_d}\sum_{i=1}^{m_d}T_iY_iY_i^\top.
\]

Then the source bulk, outlier-count, and projected-eigenvector theorem holds with

\[
1+zs_c(z)
=
c\,\mathbb E\!\left[
\frac{s_c(z)T}{\lambda c+s_c(z)T}
\right],
\tag{4.3}
\]

and

\[
F_c(z)
=
\lambda c\,\mathbb E\!\left[
\frac{T}{\lambda c+s_c(z)T}
VV^\top
\right].
\tag{4.4}
\]

The convergence is locally uniform on deterministic compact subsets of the complement of the limiting bulk. The characteristic determinants converge locally uniformly, preserving analytic multiplicity. The compressed resolvents converge uniformly on contours, yielding the spectral-projection statement of Section 13.

#### Proof

Write

\[
\sqrt{\frac{\lambda}{d}}Y_i
=
L\left(\sqrt{\frac{\lambda}{d}}V_i\right)
+
L^\perp\left(\frac{W_i}{\sqrt d}\right).
\]

This is exactly the decomposition in the source’s Section 2.6, except that the \(q\)-dimensional row mark is not required to be Gaussian.

1. **Weighted-Wishart bulk.**  
   The orthogonal block is an i.i.d. Gaussian matrix independent of the diagonal \(T\). The source’s weighted-Wishart local law and no-outlier theorem depend only on the bounded, gapped empirical law of \(T\) and this independence.

2. **Strong convergence of the empirical law of \(T\).**  
   Weak convergence follows from the strong law. Hausdorff convergence of empirical supports follows because the compact support of the law has a finite \(\epsilon\)-net of balls of positive probability; the probability that a given ball is missed is exponentially small in \(m_d\). Borel–Cantelli gives the required strong support convergence.

3. **Reduced matrix.**  
   The source’s reduced matrix is

   \[
   F_d(z)
   =
   R^\top T(I+\widetilde S_d(z)T)^{-1}R,
   \]

   where the \(i\)-th row of \(R\) is \(\sqrt{\lambda/d}\,V_i^\top\). Thus

   \[
   F_d(z)
   =
   \frac{\lambda}{d}
   \sum_{i=1}^{m_d}
   \frac{T_iV_iV_i^\top}
   {1+\widetilde S_d(z)T_i}.
   \tag{4.5}
   \]

4. **What changes in source Lemmas 2.16–2.19.**  
   Lemma 2.16 uses a fourth-moment strong law for the row marks; all moments of \(V\) suffice. Lemma 2.17 is explicitly a triangular-array i.i.d. strong-law and equicontinuity argument; again, all moments suffice. The only place where the source identifies the expectation by the Gaussian-mixture formula is Lemma 2.18. Here that calculation is replaced directly by

   \[
   \mathbb EF_d(z)
   \longrightarrow
   \lambda c\,
   \mathbb E\!\left[
   \frac{T}{1+\widetilde S(z)T}VV^\top
   \right].
   \]

   Dominated convergence supplies the analogue of Lemma 2.19.

5. **Schur complement.**  
   Since \(T\ge\tau\), the source linearization with \(T^{-1}\) is valid without alteration. The random directions built from \(R\) are independent of the Gaussian orthogonal block, exactly as required by the source anisotropic deterministic equivalent.

6. **Root count and eigenvectors.**  
   The characteristic determinant converges uniformly on compacta to
   \(\det(zI-\widetilde F_c(z))\). The argument principle preserves analytic multiplicity. The source’s differentiated Schur-complement identity gives the eigenvector normalization. Uniform convergence on a contour gives the additional projection theorem.

Rescaling \(H_d=(\lambda c)\widehat M_d\) converts (4.1)–(4.2) to (4.3)–(4.4). This proves the proposition. \(\square\)

The proposition is not a new local law. It is a direct audit of which hypotheses the source proof actually uses after its Gaussian orthogonal block has been isolated.

---

## 5. Bulk law with the zero atom

The source’s bulk theorem already does not assume invertibility, so the zero atom is covered at the level of weak empirical spectral convergence. The active reduction also verifies the normalization and gives a second derivation.

Let \(\mathbb P_+\) be the active mark law:

\[
\mathbb P_+(b,dg)
=
\frac{p_b\mathbf 1_{\{h_b(g)>0\}}\gamma_q(dg)}{\pi},
\tag{5.1}
\]

where \(\gamma_q\) is standard Gaussian measure. Under \(\mathbb P_+\), set

\[
T=h_b(g),\qquad V=v_b(g).
\]

Let

\[
c=\phi\pi.
\]

For the active matrix \(\widehat M_d\), Proposition 4.1 gives a bulk transform \(s_+\) satisfying

\[
1+xs_+(x)
=
c\,\mathbb E_+\!\left[
\frac{s_+(x)T}{\lambda c+s_+(x)T}
\right].
\tag{5.2}
\]

Define

\[
S(z)=\frac1\pi s_+\!\left(\frac z\pi\right).
\tag{5.3}
\]

Since

\[
\mathbb E_+[f]
=
\frac1\pi
\sum_b p_b
\mathbb E[
\mathbf 1_{\{h_b(g)>0\}}f(b,g)],
\]

substitution into (5.2) yields

\[
1+zS(z)
=
\phi\sum_b p_b
\mathbb E\!\left[
\frac{S(z)h_b(g)}
{\lambda\phi+S(z)h_b(g)}
\right].
\]

The inactive terms vanish because their numerator is zero, not because an inverse of zero has been taken.

By uniqueness of the physical Stieltjes branch,

\[
\nu_G=(x\mapsto\pi x)_\#\nu_+,
\tag{5.4}
\]

where \(\nu_+\) is the active bulk.

### Atom at zero

Let \(m_0=\nu_G(\{0\})\). For \(t>0\),

\[
tS_G(-t)\longrightarrow m_0.
\tag{5.5}
\]

The exact finite-dimensional nullity proved in Section 6 and weak convergence imply

\[
m_0\ge(1-\phi\pi)_+.
\tag{5.6}
\]

If \(m_0>0\), then \(S_G(-t)\to\infty\), and dominated convergence in (1.1) gives

\[
1-m_0=\phi\pi.
\]

Thus \(m_0=1-\phi\pi\). If \(\phi\pi\ge1\), a positive \(m_0\) would imply
\(1-m_0=\phi\pi\ge1\), impossible. Therefore

\[
m_0=(1-\phi\pi)_+.
\]

At \(\phi\pi=1\), the support may meet zero, but there is no atom.

---

## 6. Exact kernel and active-rank theorem

### Lemma 6.1 — conditional absolute continuity

Conditioned on \(I_\ell=1\), the pair \((b_\ell,g_\ell)\) has law (5.1), and \(w_\ell\) remains an independent standard Gaussian.

Indeed, the activity event depends only on \((b_\ell,g_\ell)\), so the conditional joint law factorizes as

\[
\frac{p_b\mathbf 1_{\{h_b(g)>0\}}\gamma_q(dg)}{\pi}
\otimes
\gamma_{d-q}(dw).
\tag{6.1}
\]

For every active class, the conditional law of \(g\) has a density with respect to Lebesgue measure. The affine orthogonal map

\[
(g,w)\mapsto
L_d(m_b+\lambda^{-1/2}g)
+\lambda^{-1/2}L_d^\perp w
\]

therefore gives an absolutely continuous law on \(\mathbb R^d\).

### Lemma 6.2 — active columns are in general linear position

Independent vectors in \(\mathbb R^d\) with absolutely continuous laws are in general linear position almost surely. Inductively, conditional on the first \(r<d\) active columns, their span is a proper linear subspace and hence has Lebesgue measure zero; the next active column does not belong to that span almost surely.

Thus

\[
\operatorname{rank}(A_{+,d})=\min(d,N_d)
\]

almost surely.

Since \(D_{+,d}^{1/2}\) is invertible,

\[
\operatorname{rank}(M_d)
=
\operatorname{rank}(A_{+,d}D_{+,d}^{1/2})
=
\min(d,N_d)
\]

almost surely.

Finally, \(N_d\sim\operatorname{Binomial}(n,\pi)\). Hoeffding’s inequality gives

\[
\mathbb P\left(\left|\frac{N_d}{n}-\pi\right|>\eta\right)
\le 2e^{-2n\eta^2}.
\]

Since \(n\asymp d\), Borel–Cantelli gives \(N_d/n\to\pi\) almost surely. Hence

\[
\frac1d\dim\ker M_d
=
1-\min\left(1,\frac{N_d}{d}\right)
\longrightarrow
(1-\phi\pi)_+
\]

almost surely.

---

## 7. Deterministic zero-atom effective equations

The active finite-dimensional matrix is

\[
F_+(x)
=
\lambda c\,
\mathbb E_+\!\left[
\frac{T}{\lambda c+s_+(x)T}
VV^\top
\right].
\tag{7.1}
\]

Because the deterministic limiting relation is \(M_d\sim\pi\widehat M_d\), define

\[
F(z)=\pi F_+\!\left(\frac z\pi\right).
\tag{7.2}
\]

Using \(c=\phi\pi\), \(s_+(z/\pi)=\pi S_G(z)\), and (5.1),

\[
\begin{aligned}
F(z)
&=
\pi\lambda\phi\pi
\mathbb E_+\!\left[
\frac{T}
{\lambda\phi\pi+\pi S_G(z)T}
VV^\top
\right]\\
&=
\lambda\phi
\sum_{b=1}^k p_b
\mathbb E\!\left[
\frac{h_b(g)}
{\lambda\phi+S_G(z)h_b(g)}
v_b(g)v_b(g)^\top
\right].
\end{aligned}
\]

This is exactly \(F_G(z)\).

The determinant scales as

\[
\det B_G(z)
=
\det\!\left(zI_q-\pi F_+(z/\pi)\right)
=
\pi^q
\det\!\left((z/\pi)I_q-F_+(z/\pi)\right).
\tag{7.3}
\]

Thus active and original roots correspond bijectively under \(z=\pi x\), with identical analytic multiplicities.

The argument never conditions the active \(g\) back to an ordinary Gaussian law. Its truncated or reweighted distribution is retained in \(\mathbb E_+\).

### Rank-deficient \(G\)

No step uses \(G^{-1}\). The extra coordinates of \(g\) associated with arbitrary columns of \(L_d\) are simply components of the fixed-dimensional mark \(V\). This also covers gates depending on those extra coordinates, even though such gates need not be functions only of the linearly dependent columns of \(B_d\).

### Hidden-pole check

For the active law, \(T\in[\tau,M]\). The source weighted-Wishart analysis gives, on every compact set outside the active bulk,

\[
\operatorname*{ess\,inf}_{T}
|\,\lambda c+s_+(x)T\,|>0.
\]

Using (5.3), this is equivalent to the denominator bound in Theorem 1.1(b). Inactive terms have denominator \(\lambda\phi\). Hence the analytic determinant has no unaccounted pole on any right-outlier contour.

---

## 8. Right-edge and support stability

No \(\epsilon\)-regularization is needed.

From (5.4),

\[
\operatorname{supp}\nu_G
=
\pi\,\operatorname{supp}\nu_+,
\qquad
\lambda_+(G)=\pi\lambda_{+,+}.
\tag{8.1}
\]

This is exact deterministic dilation, not a conclusion inferred from weak convergence.

At finite dimension,

\[
M_d=\alpha_d\widehat M_d,
\qquad
\alpha_d=\frac{N_d}{n}\xrightarrow{\mathrm{a.s.}}\pi.
\tag{8.2}
\]

Thus every active empirical eigenvalue is multiplied by the same scalar \(\alpha_d\). Fixed positive gaps between an interval endpoint, the bulk, and neighboring roots remain positive for all sufficiently large \(d\).

### Fixed-\(\epsilon\) regularization, for comparison

Let

\[
D_\epsilon=D+\epsilon P_0,
\qquad
P_0=\operatorname{diag}(\mathbf 1_{\{D_{\ell\ell}=0\}}).
\]

Then

\[
M_{d,\epsilon}-M_d
=
\frac{\epsilon}{n}A_dP_0A_d^\top
\]

and

\[
\|M_{d,\epsilon}-M_d\|
\le
\epsilon\frac{\|A_d\|^2}{n}
=O_{\mathbb P}(\epsilon).
\tag{8.3}
\]

This validates the perturbation warm-up. It does not by itself establish support-edge or multiplicity stability as \(\epsilon\downarrow0\). The active reduction supersedes that route.

---

## 9. Analytic effective-root stability

For \(z>\lambda_+(G)\),

\[
S_G'(z)
=
\int\frac{1}{(x-z)^2}\,\nu_G(dx)>0.
\tag{9.1}
\]

Differentiating (1.3),

\[
F_G'(z)
=
-\lambda\phi S_G'(z)
\sum_b p_b
\mathbb E\!\left[
\frac{h_b(g)^2}
{(\lambda\phi+S_G(z)h_b(g))^2}
v_b(g)v_b(g)^\top
\right]
\preceq0.
\tag{9.2}
\]

Therefore

\[
B_G'(z)=I_q-F_G'(z)\succeq I_q.
\tag{9.3}
\]

Consequences:

1. \(B_G(z_2)-B_G(z_1)\succeq(z_2-z_1)I_q\) for \(z_2>z_1>\lambda_+\).
2. Every ordered eigenvalue of \(B_G(z)\) is strictly increasing.
3. Each ordered eigenvalue can cross zero at most once.
4. The total right-root multiplicity is at most \(q\).
5. Right roots are isolated.

### Analytic multiplicity

Let \(z_*\) be a root and \(K_*=\ker B_G(z_*)\), \(\dim K_*=m\). In the orthogonal decomposition \(K_*\oplus K_*^\perp\),

\[
B_G(z_*+t)
=
\begin{bmatrix}
tJ_*+O(t^2)&tC+O(t^2)\\
tC^\top+O(t^2)&B_{22}+O(t)
\end{bmatrix},
\]

where \(B_{22}\) is invertible and

\[
J_*=\left.P_*B_G'(z_*)P_*\right|_{K_*}\succ0.
\]

The Schur complement on \(K_*\) is

\[
tJ_*+O(t^2).
\]

Hence

\[
\det B_G(z_*+t)
=
\det(B_{22})\,t^m\det(J_*)+O(t^{m+1}),
\]

which proves (1.5).

Local uniform convergence of the empirical characteristic determinant to \(\det B_G\) on a contour now permits the argument principle, or equivalently Rouché’s theorem, to preserve this multiplicity.

---

## 10. Universal empirical outlier-count proof

### 10.1 Conditional law given the active sample size

For any deterministic active index set \(J\), conditioned on

\[
\{I_\ell=1:\ell\in J\},
\qquad
\{I_\ell=0:\ell\notin J\},
\]

the active columns are independent and distributed according to (6.1). Conditional on \(N_d=m\), the unordered active columns have exactly the law of \(m\) i.i.d. active samples. Their positions are uniform and irrelevant to \(A_+D_+A_+^\top\).

### 10.2 Random-index transfer lemma

Let \(r_{d,m}\in[0,1]\) be a failure probability for the \(m\)-sample active model. Suppose

\[
r_{d,m_d}\to0
\]

for every deterministic sequence \(m_d/d\to c\). If \(N_d/d\to c\) in probability, then

\[
\mathbb E\,r_{d,N_d}\to0.
\tag{10.1}
\]

To prove this, choose \(\eta_d\downarrow0\) with

\[
\mathbb P\{|N_d/d-c|>\eta_d\}\to0.
\]

If the supremum of \(r_{d,m}\) over \(|m/d-c|\le\eta_d\) did not tend to zero, a subsequence \(m_d/d\to c\) would contradict the deterministic-sequence hypothesis.

### 10.3 Applying the marked theorem

For every deterministic \(m_d/d\to c=\phi\pi\), Proposition 4.1 gives exact active eigenvalue counts on fixed admissible intervals. It also gives the same result for endpoint sequences converging to admissible endpoints, because uniform determinant convergence and the no-outlier theorem leave fixed root-free bands around those endpoints.

For the original interval \(I=[a,b]\),

\[
\#\{\sigma(M_d)\cap[a,b]\}
=
\#\left\{
\sigma(\widehat M_d)
\cap
\left[\frac a{\alpha_d},\frac b{\alpha_d}\right]
\right\},
\qquad
\alpha_d=\frac{N_d}{n}.
\tag{10.2}
\]

For every deterministic \(m_d/d\to c\), one has \(m_d/n_d\to\pi\), so the active interval endpoints converge to \(a/\pi\) and \(b/\pi\). By (7.3), the number of active roots in that interval equals the number of target roots in \([a,b]\), with multiplicity.

The random-index lemma removes the conditioning on \(N_d\). This proves (1.4).

---

## 11. No-spurious-right-outlier proof

First,

\[
0\preceq M_d\preceq \frac{M}{n}A_dA_d^\top,
\]

so

\[
\|M_d\|
\le
M\frac{\|A_d\|^2}{n}.
\tag{11.1}
\]

Write \(A_d=Z_d+\mathcal M_d\), where \(Z_d\) has i.i.d. \(N(0,\lambda^{-1})\) entries and the columns of \(\mathcal M_d\) belong to the finite set of means. Then

\[
\frac{\|Z_d\|}{\sqrt n}=O_{\mathbb P}(1),
\qquad
\frac{\|\mathcal M_d\|}{\sqrt n}
\le
\max_b\|\mu_b\|=O(1).
\]

Hence \(\|M_d\|=O_{\mathbb P}(1)\), giving a deterministic \(K\).

Second, \(F_G(z)\) is bounded for large \(z\) and

\[
F_G(z)\longrightarrow
\sum_b p_b\mathbb E[h_b(g)v_b(g)v_b(g)^\top]
\qquad (z\to+\infty).
\]

Thus \(zI-F_G(z)\) is positive definite for all sufficiently large \(z\), so all effective right roots are bounded.

Fix \(\epsilon>0\) and a small \(\delta>0\). The complement in
\([\lambda_++\epsilon,K]\) of the \(\delta\)-neighborhoods of the finitely many effective roots is a finite union of compact root-free intervals. The count theorem gives zero empirical eigenvalues in each such interval with probability tending to one.

Roots lying strictly below \(\lambda_++\epsilon\) have a fixed positive gap from the threshold and their empirical eigenvalues cannot cross that gap with nonvanishing probability. A root exactly at the threshold belongs to \(Z_{\epsilon,K}\). Therefore (1.7) follows.

The existence and convergence assertion (1.6) follows by applying the count theorem to an isolating interval and then to arbitrarily smaller isolating intervals.

---

## 12. Simple-root eigenvector proof

For the active model, the source Schur-complement proof, with Proposition 4.1’s mark replacement, yields uniformly near an isolated root \(x_*=z_*/\pi\),

\[
\|(x_dI-F_+(x_d))r_d\|=o_{\mathbb P}(1),
\tag{12.1}
\]

and

\[
\left|
\|r_d\|^2-\langle r_d,F_+'(x_d)r_d\rangle-1
\right|
=o_{\mathbb P}(1).
\tag{12.2}
\]

Multiplication of a matrix by \(\alpha_d=N_d/n\) changes its eigenvalues but not its eigenvectors. The deterministic scaling relation is

\[
F_G(z)=\pi F_+(z/\pi),
\qquad
F_G'(z)=F_+'(z/\pi).
\tag{12.3}
\]

Since \(\alpha_d\to\pi\), local uniformity of the deterministic equivalents converts (12.1)–(12.2) into (1.8)–(1.9).

For a simple root, \(\ker B_G(z_*)\) is one-dimensional by (1.5). Equation (1.8) forces every subsequential limit of \(r_d\) into that kernel. Equation (1.9) fixes its magnitude because \(B_G'(z_*)\succ0\). The sign convention then gives the full convergence (1.11).

---

## 13. Multiple-root spectral-projection theorem

Let \(\Gamma\) be a positively oriented contour enclosing \(z_*\) and no other effective root or bulk point. The active Schur-complement argument gives the compressed-resolvent convergence

\[
\sup_{z\in\Gamma}
\left\|
L_d^\top(M_d-zI)^{-1}L_d
+
B_G(z)^{-1}
\right\|
\xrightarrow{\mathbb P}0.
\tag{13.1}
\]

The sign is due to the convention \((M_d-zI)^{-1}\).

The spectral projection is

\[
\Pi_d
=
-\frac1{2\pi i}
\oint_\Gamma(M_d-zI)^{-1}\,dz.
\tag{13.2}
\]

Combining (13.1)–(13.2),

\[
L_d^\top\Pi_dL_d
\longrightarrow
\frac1{2\pi i}\oint_\Gamma B_G(z)^{-1}\,dz.
\tag{13.3}
\]

The block expansion in Section 9 gives

\[
B_G(z_*+t)^{-1}
=
\frac1tP_*J_*^{-1}P_*+O(1),
\]

so the residue in (13.3) is

\[
Q_*=P_*J_*^{-1}P_*.
\]

This proves (1.14). The root-count theorem gives \(\operatorname{rank}\Pi_d=m_*\). Since

\[
L_d^\top\Pi_dL_d
=
(L_d^\top U_d)(L_d^\top U_d)^\top
=
R_dR_d^\top,
\]

(1.15) follows. The matrix \(Q_*\) is positive definite on \(K_*\), hence its range is exactly \(K_*\); the remaining statements in (1.16) follow by compactness and a right orthogonal rotation.

This is the correct replacement for individual eigenvector convergence at a repeated root.

---

## 14. ReLU-gate corollary

Assume

\[
h_b(g)=a_b(g)\mathbf 1_{\{\ell_b(g)>0\}},
\]

where \(\ell_b\) is a nonconstant affine function and

\[
\tau\le a_b(g)\le M
\quad\text{on }\{\ell_b(g)>0\}.
\]

Since \(\ell_b(g)\) is a nondegenerate one-dimensional Gaussian,

\[
0<\mathbb P\{\ell_b(g)>0\}<1.
\]

Thus \(h_b(g)\in\{0\}\cup[\tau,M]\), and Theorem 1.1 applies.

For the pure gate,

\[
h_b(g)=\mathbf 1_{\{\ell_b(g)>0\}},
\]

the matrix is the half-space-gated empirical second moment

\[
M_d
=
\frac1n
\sum_{\ell=1}^n
\mathbf 1_{\{\ell_{b_\ell}(g_\ell)>0\}}
Y_\ell Y_\ell^\top.
\tag{14.1}
\]

### Exact neural-network interpretation

Consider one ReLU unit

\[
f_w(Y)=a\,\sigma(w^\top Y),
\qquad
\sigma(t)=t_+,
\]

with a fixed output coefficient \(a\). At a parameter \(w\) for which no sample satisfies \(w^\top Y_\ell=0\),

\[
\nabla_w f_w(Y_\ell)
=
a\,\mathbf 1_{\{w^\top Y_\ell>0\}}Y_\ell.
\]

The \(w\)-\(w\) Jacobian-Gram or Gauss–Newton block is therefore

\[
\frac1n\sum_{\ell=1}^n
\nabla_wf_w(Y_\ell)\nabla_wf_w(Y_\ell)^\top
=
\frac{a^2}{n}
\sum_{\ell=1}^n
\mathbf 1_{\{w^\top Y_\ell>0\}}
Y_\ell Y_\ell^\top.
\tag{14.2}
\]

For squared loss and a fixed deterministic \(w\), Gaussian data satisfy
\(w^\top Y_\ell\ne0\) for every finite sample almost surely. The activation pattern is then locally constant, \(\nabla_w^2 f_w(Y_\ell)=0\), and the classical \(w\)-\(w\) Hessian block equals (14.2).

This statement does **not** cover:

* a data-dependent parameter at a ReLU kink;
* a whole training trajectory without uniform margin control;
* cross-neuron or cross-layer Hessian blocks;
* non-Gauss–Newton residual terms when the network output has nonzero second derivatives in the block under study;
* a generalized Hessian unless it is separately defined and analyzed.

---

## 15. Reproducible computational checks and benchmark warm-ups

The computations are diagnostics, not proof. They use master seed `20260720`.

### 15.1 Warm-up 9.1 — independent Bernoulli thinning

Let \(h\sim\operatorname{Bernoulli}(\pi)\) independently of the columns. Then

\[
M_d
=
\frac{N_d}{n}
\left(\frac1{N_d}A_+A_+^\top\right),
\qquad
\frac{N_d}{d}\to c:=\phi\pi.
\]

The continuous bulk edges are

\[
\lambda_\pm
=
\frac{(1\pm\sqrt c)^2}{\lambda\phi}
=
\frac{\pi}{\lambda}
\left(1\pm\frac1{\sqrt c}\right)^2.
\tag{15.1}
\]

The zero mass is \((1-c)_+\). The fixed-point equation becomes

\[
1+zS(z)=\frac{\phi\pi S(z)}{\lambda\phi+S(z)},
\]

or

\[
zS(z)^2+
(1+\lambda\phi z-\phi\pi)S(z)
+\lambda\phi=0.
\tag{15.2}
\]

This confirms the normalization by \(n\), not \(N_d\).

### 15.2 Warm-up 9.2 — centered pure gate

Let \(Y=\lambda^{-1/2}Z\), \(Z\sim N(0,I_d)\), and

\[
h=\mathbf 1_{\{\langle \ell,Z\rangle>0\}}
\]

for a unit vector \(\ell\). Conditional on \(ZZ^\top\), the only preimages are \(Z\) and \(-Z\), with equal Gaussian probability. The gate takes complementary values on those two points. Hence

\[
\mathbb P\{h=1\mid ZZ^\top\}=\frac12,
\]

so \(h\) is independent of \(YY^\top\). The matrix has exactly the same law as independent Bernoulli thinning with \(\pi=1/2\), and

\[
\lambda_\pm=
\frac{(1\pm\sqrt{\phi/2})^2}{\lambda\phi},
\qquad
\nu_G(\{0\})=(1-\phi/2)_+.
\tag{15.3}
\]

### 15.3 Warm-up 9.3 — noncentered scalar gate

Let \(g\sim N(0,1)\),

\[
h(g)=\mathbf 1_{\{a+bg>0\}},
\qquad b\ne0,
\]

and put

\[
\delta=\frac a{|b|},\qquad
s_b=\operatorname{sign}(b),\qquad
\pi=\Phi(\delta),\qquad
\kappa=\frac{\varphi(\delta)}{\Phi(\delta)}.
\]

Then

\[
\mathbb E[g\mid h=1]=s_b\kappa,
\qquad
\mathbb E[g^2\mid h=1]=1-\delta\kappa,
\tag{15.4}
\]

and

\[
\mathbb E[hg]=s_b\varphi(\delta),
\qquad
\mathbb E[hg^2]=\pi-\delta\varphi(\delta).
\tag{15.5}
\]

For \(v=m+\lambda^{-1/2}g\),

\[
F_G(z)
=
\frac{\lambda\phi}{\lambda\phi+S_G(z)}
\left[
\pi m^2+
\frac{2ms_b\varphi(\delta)}{\sqrt\lambda}
+
\frac{\pi-\delta\varphi(\delta)}{\lambda}
\right].
\tag{15.6}
\]

Let

\[
c=\phi\pi,\qquad
\beta=\lambda\mathbb E[v^2\mid h=1]
=
\lambda m^2+2\sqrt\lambda\,m s_b\kappa+1-\delta\kappa.
\tag{15.7}
\]

The scalar determinant equation gives the standard spiked-covariance criterion

\[
\beta>1+\frac1{\sqrt c},
\tag{15.8}
\]

and, in the supercritical case,

\[
z_{\rm out}
=
\frac{\pi}{\lambda}\,
\beta\left(1+\frac1{c(\beta-1)}\right).
\tag{15.9}
\]

### 15.4 Warm-up 9.4 — fixed-\(\epsilon\) regularization

For fixed \(\epsilon>0\), define

\[
h_{b,\epsilon}(g)
=
\begin{cases}
h_b(g),&h_b(g)>0,\\
\epsilon,&h_b(g)=0.
\end{cases}
\]

Then

\[
h_{b,\epsilon}\in[\min(\tau,\epsilon),\max(M,\epsilon)]
\]

and the source invertibility assumption holds. Its bulk and effective matrix are obtained by replacing \(h_b\) by \(h_{b,\epsilon}\) in (1.1) and (1.3).

### 15.5 Warm-ups 9.5–9.6

The exact perturbation identity and norm bound are (8.3). The exact active rank is (1.17), proved in Section 6.

### 15.6 Numerical outputs

The supplied script produced:

| Check | Representative result |
|---|---:|
| Bernoulli thinning, \(d=320,n=640,\pi=0.4,\lambda=1.5\) | \(N_{\rm active}=254\), numerical rank \(254\), exact predicted rank \(254\) |
| Same model | empirical zero mass \(0.20625\), limit \(0.2\) |
| Same model | top eigenvalue \(1.1641\), predicted edge \(1.1963\) |
| Stieltjes solver | fixed-point residual \(2.39\times10^{-16}\) |
| Centered pure gate | top eigenvalue \(1.9728\), predicted edge \(2\) |
| Noncentered gate \(m=2,a=0,b=1,\phi=2,\lambda=1\) | predicted outlier \(4.6653\), simulated values \(4.48\)–\(4.87\) |
| Scalar determinant check | residual \(1.62\times10^{-10}\) |
| Regularization identity | errors below \(1.1\times10^{-17}\) |
| Two independent constructions | covariance operator difference \(1.93\times10^{-15}\) |

Files:

* `zero_atom_checks.py` — main simulation and plotting script;
* `verify_zero_atom_results.py` — independent deterministic assertions;
* `zero_atom_results.json` — parameters, package versions, seeds, and numerical diagnostics;
* `requirements-zero-atom.txt` — package requirements;
* four PNG diagnostic plots.

---

## 16. Adversarial audit report — fresh serial pass

No multiagent or external-auditor tool was exposed in this environment. Accordingly, the audit below is a distinct serial pass performed after the proof was drafted, using the exact theorem, source theorem, candidate proof, and invoked lemmas; it is not represented as an audit by a separate human or agent.

### 16.1 Approach registry

#### A1. Active-column conditioning

* **Exact proposed lemma:** Conditional on activity, active marks are i.i.d. with law (5.1), while the orthogonal Gaussian noise remains independent.
* **Assumptions:** Activity is measurable in \((b,g)\); \(\pi>0\).
* **Conclusion:** \(M_d=(N_d/n)\widehat M_d\) with \(D_+\in[\tau,M]\).
* **Dependence:** No \(\epsilon\); finite-\(d\) identity; asymptotic ratio \(N_d/d\to\phi\pi\).
* **Advancement:** Removes singularity exactly.
* **Fastest falsification:** Check whether conditioning changes the \(w\)-law or introduces dependence across active columns.
* **Evidence:** Conditional density factorization (6.1).
* **Known obstruction:** Active \(g\) is truncated and is not an ordinary Gaussian mixture.
* **Status:** **PROVED.**
* **Next obligation:** Extend the source proof to arbitrary fixed-dimensional marks.

#### A2. Marked extension of the source theorem

* **Exact proposed lemma:** Proposition 4.1.
* **Assumptions:** \(T\in[\tau,M]\), all moments of \(V\), \(W\) Gaussian and independent.
* **Conclusion:** Same local determinant, counts, and eigenvector equations with mark expectation.
* **Dependence:** Uniform on compact spectral sets at positive distance from the active bulk; no \(\epsilon\).
* **Advancement:** Handles the truncated active law.
* **Fastest falsification:** Locate a source lemma using Gaussian integration by parts in \(V\), rather than only in \(W\).
* **Evidence:** Source Lemmas 2.16–2.19 and Sections 2.10–2.12; only the expectation-identification lemma changes.
* **Known obstruction:** Would fail for growing-dimensional marks without new uniform moment control.
* **Status:** **PROVED.**
* **Next obligation:** Random active sample size.

#### A3. Random-index transfer

* **Exact proposed lemma:** Equation (10.1).
* **Assumptions:** Deterministic-sequence convergence for every \(m_d/d\to c\); \(N_d/d\to c\).
* **Conclusion:** Conditional results transfer to random \(N_d\).
* **Dependence:** No spectral-gap degradation beyond the fixed admissible interval.
* **Advancement:** Removes conditioning.
* **Fastest falsification:** Construct a triangular failure array large only on a typical random subsequence.
* **Evidence:** Supremum-on-shrinking-window contradiction.
* **Known obstruction:** None.
* **Status:** **PROVED.**
* **Next obligation:** Deterministic scaling equations.

#### A4. Exact dilation and support edge

* **Exact proposed lemma:** \(\nu_G=(x\mapsto\pi x)_\#\nu_+\) and \(F_G(z)=\pi F_+(z/\pi)\).
* **Assumptions:** \(\pi>0\).
* **Conclusion:** Exact equations, edge, roots, and multiplicities.
* **Dependence:** No \(\epsilon\); no weak-support inference.
* **Advancement:** Eliminates the support-stability bottleneck.
* **Fastest falsification:** Substitute into the fixed-point equation and check every factor of \(\pi,\phi,\lambda\).
* **Evidence:** Algebra in Sections 5 and 7.
* **Known obstruction:** None.
* **Status:** **PROVED.**
* **Next obligation:** Analytic multiplicity.

#### A5. Analytic determinant and root multiplicity

* **Exact proposed lemma:** \(B_G'(z)\succeq I\) and analytic multiplicity equals \(\dim\ker B_G(z_*)\).
* **Assumptions:** Nonnegative weights and a right spectral point.
* **Conclusion:** At most \(q\) right roots; repeated roots are controlled.
* **Dependence:** Uniform on compact right sets; denominators separated from zero.
* **Advancement:** Preserves multiplicity.
* **Fastest falsification:** Check the sign of \(S_G'(z)\) and of the derivative of the denominator.
* **Evidence:** Equations (9.1)–(9.3) and the Schur expansion.
* **Known obstruction:** The Loewner monotonicity need not survive signed weights.
* **Status:** **PROVED.**
* **Next obligation:** Empirical count and projections.

#### A6. Spectral projection

* **Exact proposed lemma:** Equation (1.14).
* **Assumptions:** Isolated root and a contour separated from the bulk.
* **Conclusion:** Convergence of the whole outlier subspace with the derivative metric.
* **Dependence:** Inverse powers of the fixed contour gap, but no \(d\)-dependent gap.
* **Advancement:** Correct treatment of multiple roots.
* **Fastest falsification:** Verify the sign in the compressed resolvent and compute the residue.
* **Evidence:** Equations (13.1)–(13.3).
* **Known obstruction:** None for fixed isolated roots.
* **Status:** **PROVED.**
* **Next obligation:** None for the main theorem.

#### A7. Epsilon regularization

* **Exact proposed lemma:** \(\|M_{d,\epsilon}-M_d\|\le C\epsilon\) with high probability.
* **Assumptions:** Bounded means and Gaussian noise.
* **Conclusion:** Matrix perturbation is small.
* **Dependence:** Linear in \(\epsilon\), uniform in \(d\).
* **Advancement:** Useful diagnostic only.
* **Fastest falsification:** Compute \(\|A\|^2/n\).
* **Evidence:** Equation (8.3) and simulation.
* **Known obstruction:** Does not itself prove limiting support-edge or root-multiplicity stability.
* **Status:** **SUPERSEDED.**
* **Next obligation:** None; active reduction avoids the obstruction.

#### A8. Moore–Penrose or generalized Schur complement

* **Exact proposed lemma:** Replace \(D^{-1}\) by \(D^\dagger\) without extra factors.
* **Assumptions:** Singular \(D\).
* **Conclusion sought:** Direct singular linearization.
* **Dependence:** Potential zero-mode factors.
* **Advancement:** Would avoid deleting columns.
* **Fastest falsification:** Compare determinants after splitting active and inactive coordinates.
* **Evidence:** The split shows inactive factors must be removed explicitly.
* **Known obstruction:** A naive pseudoinverse loses determinant factors and zero modes.
* **Status:** **SUPERSEDED.**
* **Next obligation:** None.

#### A9. Direct singular anisotropic local law

* **Exact proposed lemma:** A local law for the singular full linearization.
* **Assumptions:** Coupled zero weights.
* **Conclusion sought:** Direct projected resolvent.
* **Dependence:** Strong local estimates in \(d\) and spectral scale.
* **Advancement:** Stronger than necessary.
* **Fastest falsification:** Compare technical burden with active reduction.
* **Evidence:** No additional theorem is needed.
* **Known obstruction:** Reproves a major local-law result without payoff.
* **Status:** **BLOCKED / unnecessary.**
* **Next obligation:** None for the main theorem.

#### A10. Counterexample search

* **Exact proposed failure mechanisms:** \(\phi\pi<1\), a new hard edge, active/inactive boundary outliers, conditioning corrections, roots escaping to infinity.
* **Assumptions:** Scalar and two-dimensional gated models.
* **Conclusion:** None of these mechanisms violates the theorem.
* **Dependence:** Analytic and computational checks.
* **Advancement:** Tests the unchanged determinant.
* **Fastest falsification:** Independent Bernoulli and centered half-space gates.
* **Evidence:** Sections 5, 9, 11, and 15.
* **Known obstruction:** Numerical checks cannot establish a theorem.
* **Status:** **DISPROVED as counterexamples; computationally corroborated.**
* **Next obligation:** None.

### 16.2 Proof dependency graph

```text
Zero-atom right-outlier theorem — PROVED
|
+-- Source invertible-weight theorem — KNOWN
|
+-- Source bulk theorem permits zero weights — KNOWN
|
+-- Active conditional law — PROVED
|
+-- Marked invertible-weight extension — PROVED
|   |
|   +-- Active empirical weight law and support convergence — PROVED
|   +-- Reduced-matrix uniform law — PROVED
|   +-- Active Schur complement — PROVED
|
+-- Exact active-rank and kernel theorem — PROVED
|
+-- Exact deterministic dilation — PROVED
|   |
|   +-- Stieltjes equation — PROVED
|   +-- Effective matrix equation — PROVED
|   +-- Right-edge identity — PROVED
|   +-- Derivative identity — PROVED
|
+-- Analytic root multiplicity — PROVED
|
+-- Random-index empirical count transfer — PROVED
|
+-- No-spurious-right-outlier theorem — PROVED
|
+-- Simple-root eigenvectors — PROVED
|
+-- Multiple-root spectral projections — PROVED
|
+-- ReLU-gate corollary — PROVED
|
+-- Current literature audit — KNOWN as of 20 July 2026
|
+-- Numerical checks — COMPUTATIONAL
```

No necessary node remains computational, conjectured, blocked, or false.

### 16.3 Fresh serial adversarial audit

The first invalid inference in the initially tempting proof was:

> “Conditioned on activity, the active columns remain an ordinary Gaussian mixture.”

This is false. Conditioning truncates or reweights \(g\). The proof was repaired by retaining the exact active mark law (5.1) and proving Proposition 4.1.

The completed proof was then audited against the requested failure modes.

1. **Invalid inverse:** Every inverse is applied only to \(D_+\), whose spectrum lies in \([\tau,M]\).
2. **Incorrect conditioning:** The exact truncated law is used; no Gaussian-mixture substitution occurs.
3. **Lost normalization:** The factor \(N_d/n\to\pi\) is retained and creates the \(\phi\), not \(\phi\pi\), in the final denominator.
4. **Zero atom versus zero eigenvalues:** Exact nullity, limiting atom, small positive spectrum, and right outliers are treated separately.
5. **Weak support reasoning:** The right edge follows from exact pushforward (8.1), not weak convergence.
6. **Nonuniform regularization:** Regularization is not used in the proof.
7. **Incorrect Weyl transfer:** Counts come from the analytic determinant and argument principle; projections come from contour resolvents.
8. **Bulk-edge roots:** The theorem is only for \(z_*>\lambda_+\), not \(z_*=\lambda_+\).
9. **Multiple roots:** Only invariant-subspace and projection convergence is stated.
10. **Rank-deficient \(G\):** No inverse of \(G\) is used; extra \(L\)-coordinates are allowed.
11. **Stieltjes branch:** The active covariance model identifies the physical branch.
12. **Hidden poles:** Compact right contours inherit the active denominator separation.
13. **ReLU differentiability:** The neural interpretation is restricted to a fixed non-kink parameter or to the Gauss–Newton/Jacobian-Gram block.
14. **False independence:** Independence is asserted only in the centered pure-gate warm-up, where global sign symmetry proves it.
15. **Roots escaping to infinity:** \(F_G(z)\) remains bounded while \(zI_q\) diverges.
16. **Literature mismatch:** The Kovačević–Zhang–Mondelli result is attributed and distinguished; broad novelty is not claimed.

No fatal gap was found in the main theorem after these repairs. The optional signed-weight, continuous-small-ball, and trajectory-uniform extensions remain outside this resolution.

---

## References

1. G. Ben Arous, R. Gheissari, J. Huang, and A. Jagannath,  
   *Local geometry of high-dimensional mixture models: Effective spectral theory and dynamical transitions*, arXiv:2502.15655v3, 2026.  
   https://arxiv.org/abs/2502.15655

2. F. Kovačević, Y. Zhang, and M. Mondelli,  
   *Spectral Estimators for Multi-Index Models: Precise Asymptotics and Optimal Weak Recovery*, COLT 2025, PMLR 291; arXiv:2502.01583.  
   https://proceedings.mlr.press/v291/kovacevic25a.html

3. Z. Fan, R. Ma, E. Paquette, and Z. Wang,  
   *Anisotropic local law for non-separable sample covariance matrices*, arXiv:2602.17960, 2026.  
   https://arxiv.org/abs/2602.17960

4. A. Montanari and B. Saeed,  
   *Variational Formulas for the Spectrum of Block Wishart Matrices*, arXiv:2606.27774, 2026.  
   https://arxiv.org/abs/2606.27774
