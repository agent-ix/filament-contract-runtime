---
id: SR-2026110705000816
title: QSL-2279 runtime PR230 gap-analysis
type: SpecReview
analysis: gap-analysis
scope: agent-ix/filament-contract-runtime; Cargo.toml, Cargo.lock, measurement/exact-panic/Cargo.toml;
  frozen 14e9c18467502add47a1e27e365967ca34356ead
review_set: subset
relationships:
- target: ix://agent-ix/filament-contract-runtime/FR-275
  type: references
- target: ix://agent-ix/filament-contract-runtime/AD-003
  type: references
---

## Summary

Frozen head `14e9c18467502add47a1e27e365967ca34356ead`; base `93e3681ad772971e48c5d2804969e5940b1a131d`. Ticket: QSL-2279. PR: https://github.com/agent-ix/filament-contract-runtime/pull/230.

Only Cargo.toml, Cargo.lock and measurement/exact-panic/Cargo.toml change. All three actual SV-source edges (root optional normal dependency, dev allocator, measurement consumer) select 6e809434d5fd7bde4c5b88ec40cd809efcca595d. The measurement edge formerly requested 1df71c27 with resolved f5c913bd, while the root requested f5c913bd; the two source identities collapse to one. Exact stays b26a8e4c592503fccdc4a0e3d2cce23dd8487616. No dependency is added and no registry package or non-SV Git source changes.

FR-275's one-copy obligation and AD-003's RT boundary own this change. FR-275-AC-4's older branch-main wording is context only; this dispatch explicitly authorizes the existing revision-pin mechanism's ordered pin wave. This review does not grant a specification waiver or claim that AC-4 is fulfilled.

Manual, narrowly scoped gap analysis of the dependency pin only, as dispatched. This is not a full repository gap audit or an engine-backed matrix PASS. No full matrix, reverse ownership inventory or repository-wide stub sweep was performed. Changed files add no runtime behavior, source or tests; their ownership is FR-275 and AD-003.

## Verdict

FAIL: the selected shared owner violates its IEEE collection refusal contract, and the focused exact_type_check_allocation suite fails at this exact head. Acceptance is blocked pending producer/consumer resolution and green focused owner checks. This is not established to be a new pin regression.

## Findings

| ID | Severity | Summary | Refs |
| --- | --- | --- | --- |
| FND-001 | high | Selected semantic-value owner admits IEEE-bearing set/bag declared types contrary to its documented refusal contract; focused RT acceptance fails. | Cargo.toml:37; tests/exact_type_check_allocation.rs:273; tests/exact_type_check_allocation.rs:318 |

## Scope

```yaml
scope:
- id: FR-275-AC-3
  path: spec/exact/functional/FR-275-single-exact-kernel.md
  role: examined
  excerpt: '`filament-exact` is an optional dependency of the runtime, enabled only
    by the `exact` feature.'
- id: FR-275-AC-5
  path: spec/exact/functional/FR-275-single-exact-kernel.md
  role: examined
  excerpt: '`Cargo.lock` holds exactly one entry each for `filament-exact`, `filament-semantic-value`,
    `quire-canonical` and `quire-canonical-derive`, and, after AD-004 step 5, the
    FSL-owned evaluation leaf.'
- id: AD-003
  path: spec/assurance/AD-003-codegen-runtime-seam.md
  role: examined
  excerpt: RT to shared exact/semantic-value leaves | allowed, optional under `exact`
- id: AD-003
  path: spec/assurance/AD-003-codegen-runtime-seam.md
  role: examined
  excerpt: RT to CG, IR or the FSL monorepo | forbidden
- id: Cargo.toml
  path: Cargo.toml
  role: examined
  excerpt: filament-semantic-value = { git = "https://github.com/agent-ix/filament-semantic-value",
    rev = "6e809434d5fd7bde4c5b88ec40cd809efcca595d", optional = true, default-features
    = false }
- id: Cargo.toml:dev-dependencies
  path: Cargo.toml
  role: examined
  excerpt: fsv-failing-allocator = { git = "https://github.com/agent-ix/filament-semantic-value",
    rev = "6e809434d5fd7bde4c5b88ec40cd809efcca595d" }
- id: measurement/exact-panic/Cargo.toml
  path: measurement/exact-panic/Cargo.toml
  role: examined
  excerpt: filament-semantic-value = { git = "https://github.com/agent-ix/filament-semantic-value",
    rev = "6e809434d5fd7bde4c5b88ec40cd809efcca595d", default-features = false }
- id: Cargo.lock
  path: Cargo.lock
  role: examined
  excerpt: source = "git+https://github.com/agent-ix/filament-semantic-value?rev=6e809434d5fd7bde4c5b88ec40cd809efcca595d#6e809434d5fd7bde4c5b88ec40cd809efcca595d"
- id: FR-275-AC-4
  path: spec/exact/functional/FR-275-single-exact-kernel.md
  role: context_only
  excerpt: The optional `filament-exact` and `filament-semantic-value` dependencies
    use their own `agent-ix` Git repositories with `branch = "main"` and no `rev`,
    `tag`, `path` or committed `[patch]`.
- id: measurement/exact-panic/src/lib.rs
  path: measurement/exact-panic/src/lib.rs
  role: examined
  excerpt: use filament_semantic_value::object_closure::ObjectClosure;
- id: FR-273-AC-14
  path: spec/exact/functional/FR-273-exact-function-application.md
  role: examined
  excerpt: RT-local identity-free package function parameter/result checks and standalone-expression
    parameter/result checks preserve admitted types and the original semantic refusal
    cause, location and order through `try_check_type`.
```

## Coverage

Locked metadata supplied by the coder at `/tmp/qsl-2279-runtime-wave2-metadata.json` was inspected, not merely accepted from prose. Its workspace manifest paths name this worktree; direct dependencies and exact/SV/canonical source identities match the current manifests and Cargo.lock. Normal/build traversal from RT reaches exact and SV, then canonical/derive, with no IR, CG, evaluation, observation or FSL-monorepo package and no path returning to RT. Dev and workspace path edges were inspected separately: allocator support is dev-only; measurement/tools point toward RT or its existing shared owner. No committed patch/source substitution is introduced. One lock entry each exists for exact, SV, canonical and canonical-derive; allocator source matches SV.

The measurement source directly supplies SV ObjectClosure to RT evaluate, so aligning its source is necessary for Rust type identity. Upstream checkout HEAD is exactly the requested SV revision; the prior-to-new source diff adds dimension-equivalence projection and private conversion-class state without changing RT's declaration/ObjectClosure consumer signatures or dependency manifest. No new RT adapter, copied code, compatibility layer or tests are needed by the manifest-only change.

`quire check-lock Cargo.lock` and `git diff --check BASE..HEAD` returned 0 independently. Coder-reported fmt check passed; reviewer did not rerun Cargo fmt. Reviewer local metadata reproduction failed with Cargo exit 101 because sandbox denied creating the qualification dependency checkout under /home/peter/.cargo; existing supplied metadata was used explicitly. No build, test, clippy, target sweep or full gate was run locally. The owner exclusively controls the five focused checks: exact+proptest lib check, exact-panic check, exact_type_check_allocation, the exact linked-function test, and proptest_adapter. Their initial results were pending when the static review was written; the Focused owner evidence section below supersedes that status.

This is a bounded RT pin review. Fresh peer-root metadata and a full four-repository architecture acceptance were not performed; the inspected RT closure cannot establish every peer's independent obligation. No applicable AssuranceProfile was found under spec/. No spec/plan edits exist, so spec review and its sub-analyses do not apply. Installed tools: /home/peter/.npm-global/bin/quoin 0.36.8; /home/peter/.npm-global/bin/quire 0.52.0 (engine 0.62.2); spec-artifacts-process v0.36.0. No older binary fallback was used.

Plan completion: not assessed

Existing allocator-denial tests use the real shared allocator and assert native cause/unit/amount, location, no checked result, and successful retry. Nested type and IEEE collection controls assert typed semantic refusal. The linked-function test executes a shared Value/ObjectClosure call and checks the result and FunctionCall charge. These existing tests are relevant owner checks; the owner execution failure is recorded below. Optional semantic full-repository review was not requested.

## Focused owner evidence

The owner reports exact-head lib check (exact,proptest) passed. `exact_type_check_allocation` returned 101: four passed, two failed. `nested_declared_types_and_ieee_sets_and_bags_keep_semantic_parity` panicked at tests/exact_type_check_allocation.rs:273, `ineligible nested type admitted`. `nested_and_ieee_refusals_keep_parameter_before_result_order` failed at line 318: actual `[IllTyped(OperatorIneligible), UndischargedMeasure]`, expected three `IllTyped(OperatorIneligible)` entries followed by `UndischargedMeasure`. Source inspection independently explains these observations. Raw remote owner log: `draco:/private/tmp/qsl-2279-rt14e9-3.log` (not locally read by reviewer).

At the actual selected SV checkout 6e809434, src/declaration.rs:3630-3635, `walk_type_refusal` gates collection refusal on `kind != Sequence && contains_map_walk(element) && contains_ieee_walk(element)`. An Option<Float64> element contains no map, so the IEEE refusal is bypassed. The owner's `try_check_type` documentation at src/declaration.rs:3356-3359 says no set, bag or ordered set has an IEEE-bearing element type. RT's FR-273-AC-14 requires retaining the original semantic refusal cause and order through that checker. RT's tests correctly expose this contract failure; weakening them or treating the admission as intended is unsupported.

`git diff --exit-code f5c913bd4fc8880b45e02e3918e02360c530320c..6e809434d5fd7bde4c5b88ec40cd809efcca595d -- src/declaration.rs src/declaration/membership.rs` returned 0 in the SV checkout. This is a preexisting producer defect, not an established regression caused by this pin. It nevertheless prevents green focused acceptance of the selected source. Fix ownership and coordinated pin resolution stay on this PR/QSL-2279 under the lead; no new ticket or local shim is proposed.

The original native-host exact-panic check returned 101 for allocator/panic/unwinding configuration: its allocator/panic implementation is cfg(target_os = "none"), and Makefile:15,118-119 defines thumbv7em-none-eabi. That command was mis-targeted; it is not recorded as an SV regression. The owner replaced only that check with the repository-defined embedded build using toolchain 1.98.1, profile exact-panic and thumbv7em-none-eabi. Its result and the remaining two integration checks are pending at this review update. No local build/test/clippy was run.

## Disposition pass 1 evidence

Reviewed frozen fix head `b0610afd1526f8bf37849b0b84bf0c9e7d3fc1e2` against `14e9c18467502add47a1e27e365967ca34356ead`. Original Findings and initial review text above are preserved as written. The disposition below supersedes the initial producer-defect conclusion.

Independently read the pinned standard with `git show 247a394:spec/functional/type-model/FR-149-apply-complete-equality-matrix.md`, lines 145-186. It admits Float32/Float64 leaves at any depth in Set, Bag and OrderedSet members using bitIdentical, and explicitly states that a float leaf never makes equality ill_typed. Independently inspected SV PR105's actual diff: it adds the contains_map condition intentionally and tests try_check_type of Set/Bag/OrderedSet float-bearing types as Ok(()). Standard authority and that deliberate producer behavior supersede the stale checker doc comment used in the initial review. No producer-code bug is established by the reported failures.

The fix expands the real RT admission controls: each of Set, Bag and OrderedSet<Option<Float64>> must be admitted at package parameter, package result, standalone-expression parameter and standalone-expression result positions. Those assertions fail if the RT consumer rejects valid types. Separate Option<Sequence<Population>> controls still require OperatorIneligible, one refusal, the original Body/Expression origin and empty path, at all four consumer positions. The mixed package control keeps the precise two-cause vector [IllTyped(OperatorIneligible), UndischargedMeasure], with origin/path assertions. Mixed expression controls preserve population parameter and population result refusal while IEEE collections are admitted. Existing actual allocator-denial tests, error projection and successful retry controls remain unchanged. Trace tags remain FR-273-AC-14/TC-194. This corrects a stale test oracle with positive and negative coverage; it does not relax the shared semantic contract.

The test comment and PR body cite standard FR-149 and SV PR105. Production source, Cargo.toml, Cargo.lock and measurement sources are unchanged after 14e9; no shim, API adapter, new owner dependency or pin change is introduced. The original SR artifacts committed by the coder were verified byte-identical to the original scratch files before appending this disposition. `git diff --check 14e9..b061` returned 0. No local Cargo build/test/clippy ran.

Owner evidence: old-pin controls failed identically (remote logs draco:/private/tmp/qsl-2279-old93e3-1.log and -2.log, not read locally); exact+proptest lib check, linked-function test (1), and proptest adapter tests (5) passed on 14e9. The authorized embedded build on 14e9 passed (exit 0, toolchain 1.98.1, thumbv7em-none-eabi, exact-panic profile); reviewer read /tmp/qsl-2279-rt14e9-terra-embedded.log and confirmed the successful profile completion. Production/measurement bytes are unchanged, so no embedded rerun is requested. The designated owner subsequently returned exact-head b061 exact_type_check_allocation: 6 passed, 0 failed, 0 ignored, 0 filtered, exit 0. Raw remote log: draco:/private/tmp/qsl-2279-rtb061-fix1.log (owner-reported, not read locally).

## Dispositions

| FND | outcome | reason |
| --- | --- | --- |
| FND-001 | rejected | Rejected producer-defect attribution: authoritative standard FR-149 at specification commit 247a394 lines 145-186 admits float leaves at any depth, including Set/Bag/OrderedSet membership by bitIdentical, and says a float leaf never makes equality ill_typed. SV PR105 intentionally added this admission. The reviewer treated stale checker documentation and stale RT expected refusals as authority; that was incorrect. The two focused failures reproduce on the old pin as reported by the owner. Fix-round b0610afd corrects the RT oracle with positive admission controls while retaining nested-population refusal cause, location and order. No producer predicate fix or SV repin is needed. |

## Disposition pass 1 verdict

PASS / mergeable after the lead's final custody checks: FND-001 is rejected with standard-authority evidence; no finding remains open and no new defect was found in the corrected tests. The designated owner returned a green exact_type_check_allocation result (6 passed, exit 0) at b0610afd1526f8bf37849b0b84bf0c9e7d3fc1e2. This bounded review makes no full-repository gap-audit or proof claim.
