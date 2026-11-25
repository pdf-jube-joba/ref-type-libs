# Differential equations

`Euclidean[n].BoundedLipschitzField` represents autonomous vector fields bounded and Lipschitz in maximum norm.
`On[field, initial]` chooses positive time on both sides of the initial time and constructs Picard operators on the closed unit ball of continuous curves centered at the initial value.
The operator returns \(y_0+J(t)-J(0)\).

Completeness, integral norm bounds, and integral-difference estimates prove ball preservation and contraction ratio at most \(1/2\).
Expose the Banach-fixed-point curve as `curve`.

`On[field, initial].step` contains the constructed time width and bounds.
`On[field, initial].Step[step]` performs Picard construction for time widths satisfying those conditions.
`Step.Solution.value` is a real-domain function agreeing with the curve on the constructed interval.
`initialValue` gives the initial value; `continuous` closed-interval continuity; `derivative` coordinatewise \(y'=F(y)\) in the interior.
`initialDerivative` is the initial-time derivative.
`integralEquationUnique` proves uniqueness of Picard integral-equation solutions in this ball.
`solutionUnique` proves uniqueness of continuous ball-valued curves satisfying the ODE/initial value.
Mean-value uniqueness of primitives shows ODE solutions satisfy the integral equation.

`LocalSolution` groups positive radius, real-domain curve, initial value, and open-interval ODE.
`localExistence` proves such solutions exist for arbitrary bounded Lipschitz fields and initial values.
`localUniqueness` proves local solutions agree on a common positive interval.

`Euclidean[n].Smooth[U, field, a].localExistence` proves local existence at points of smooth vector fields on open sets.
Bound continuous partials nearby to obtain Lipschitz constants; extend to bounded Lipschitz fields by coordinate clipping.
Integral bounds keep solutions inside the clipping region for short times, recovering the original ODE.
`Smooth.localUniqueness` is the same agreement theorem for smooth-field local solutions.
`Smooth.Regularity[solution].map` represents arbitrary local solutions as smooth maps from open time intervals into the original open set.
Chain rules and the ODE inductively prove continuous differentiability of every order for smooth functions composed with solutions.
