---
id: "SR-202611210022442313144108519"
title: "Runtime PR232 gap-analysis"
type: SpecReview
analysis: gap-analysis
scope: "agent-ix/filament-contract-runtime; Cargo.toml, Cargo.lock, measurement/exact-panic/Cargo.toml, tools/kernel-api-check/Cargo.toml, tests/exact_outcome_consumer.rs; QSL-2757"
review_set: subset
relationships:
  - target: ix://agent-ix/filament-contract-runtime
    type: references
---

## Summary

Ticket QSL-2757; PR filament-contract-runtime#232; frozen head 7418b09f62196f43f5691aa87b6cec9b8e4b87c7 against 284cb6df9e2c917deba987d952e47e5ffc384ca1. Independent static review; exact model id unavailable. No builds, Cargo tests, runtime reruns, source edits or commits performed.

## Verdict

**FAIL** — Inherited 74 untagged obligations prevent repository-wide assurance PASS; bounded reverse-gap inspection remains incomplete. No PR232-introduced gap identified.

## Findings

| ID | Severity | Summary | Refs |
| --- | --- | --- | --- |
| FND-001 | high | The current local-only computed matrix reports 74 inherited untagged obligations, so repository-wide traceability assurance remains unmet; no new gap is introduced by PR232. | spec/core/non-functional/NFR-001-no-std-footprint.md:47 |

## Coverage

Reconciliation: quire matrix 0.52.0 (engine 0.62.2), explicit repository scope; no run evidence read. 178 engine obligation rows: 62 tagged, 42 method-without-symbol, 74 untagged; zero tagged-by-ignored-test. These are obligations including metrics, not test execution counts. Matrix command exit 0; strict matrix exit 1 as expected for gaps. The five-file diff changes no spec criterion or trace marker, so all gap counts are inherited and the two consumer binders survive; no baseline rerun was needed or performed.

Plan completion: not assessed

Raw matrix/coverage and source inventory are retained beside this artifact. The ordinary local-only coverage excludes make spec's declared external authoritative monitor test input. Therefore untagged monitor rows do not alone prove missing implementation or missing external tests. Inspection/measurement obligations likewise cannot be equated with absent tests. Full per-public-symbol reverse reconciliation remains incomplete under this bounded prerequisite dispatch: inventory covers the unchanged source tree, and subsystem registry ownership was inspected (core identity/verdict/observation/operators, accounting/snapshot, proptest, scalar/expression residue and monitor). Changed dependency identity maps to FR-275-AC-3/5/9; changed closed consumer vocabulary maps to FR-006-AC-3 and retained outcome behavior to FR-006-AC-1. No newly unowned behavior was identified. No repository-wide zero-untraced-behavior claim is made.

Source/test TODO, FIXME, todo! and unimplemented! scan has zero hits; the changed consumer and measurement population were directly inspected. Zero new source stubs, test stubs, skips, test removal, gate narrowing, or coverage inflation identified. Whole-source semantic reconciliation was not requested and is skipped. The retained expression port/end-state debt and legacy branch pin policy are unchanged; no assurance PASS is inferred from the source-clean prerequisite. Inherited assurance finding requires ROOT's bounded disposition under the authorized minimal wave, without representing ARCH as approving specific counts.

## Verification Evidence

ROOT supplied Titan service evidence, not independently rerun: source a0df4061 host exact all-targets check exit 0; runtime lib 8, five integrations 41, kernel API lib 2/doc 5 = 56 passed, 0 failed/ignored. Installed +1.98.1 thumbv7em-none-eabi exact-panic all-target check and documented deployment build exit 0. Qualification-only follow-up 7418b09 exact_outcome_consumer executed both tests, 2 passed/0 failed/ignored/filtered, including authoritative 66-point equality; total 58. Final current-main all-target compiler checks, isolated fixed b68 FSL analyze/root checks and match-head merge freshness belong to ROOT after custody. Full gates, feature sweep, proofs/Kani, benchmarks and installs excluded by dispatch.

Static git diff --check and rustfmt --check --edition 2021 tests/exact_outcome_consumer.rs both exit 0. No applicable AssuranceProfile was found. Spec/plan review methods do not apply because no spec/plan file changed. Optional semantic gap pass skipped.

Tool provenance on terra: /home/peter/.npm-global/bin/quire 0.52.0 (engine 0.62.2); /home/peter/.npm-global/bin/quoin 0.36.8; spec-artifacts-process@v0.36.0. These differ from the supplied release notice; reported to ROOT. No fallback binaries used.

## Examined Scope

```json
[
  {
    "id": "FR-004-AC-1",
    "path": "spec/accounting/functional/FR-004-campaign-accounting.md",
    "role": "examined",
    "excerpt": "Mixed outcome sequences produce the specified four counters."
  },
  {
    "id": "FR-004-AC-2",
    "path": "spec/accounting/functional/FR-004-campaign-accounting.md",
    "role": "examined",
    "excerpt": "Counter overflow saturates and never panics or wraps."
  },
  {
    "id": "FR-004-AC-4",
    "path": "spec/accounting/functional/FR-004-campaign-accounting.md",
    "role": "examined",
    "excerpt": "Allocation-free immutable snapshots retain exact identity and all counters after subsequent report recording; imported snapshots cannot resume a mutable report."
  },
  {
    "id": "FR-004-AC-5",
    "path": "spec/accounting/functional/FR-004-campaign-accounting.md",
    "role": "examined",
    "excerpt": "JSON transport round-trips real mixed reports and refuses independently authored malformed, incomplete, duplicate, unsupported or inconsistent data."
  },
  {
    "id": "FR-004-AC-6",
    "path": "spec/accounting/functional/FR-004-campaign-accounting.md",
    "role": "examined",
    "excerpt": "Conservative at-limit inspection distinguishes representable values from potentially saturated counts/totals without inventing overflow history."
  },
  {
    "id": "FR-004-AC-7",
    "path": "spec/accounting/functional/FR-004-campaign-accounting.md",
    "role": "examined",
    "excerpt": "Byte/identity/depth limits fail boundedly without partial output; allocator/process failure is not mislabeled as semantic refusal."
  },
  {
    "id": "FR-004-AC-8",
    "path": "spec/accounting/functional/FR-004-campaign-accounting.md",
    "role": "examined",
    "excerpt": "A verdict whose requirement or revision differs from the report's increments no counter, leaves a prior snapshot unchanged, and returns an `IdentityMismatch` carrying both identities; a report that recorded a mismatch has the same counters as one that never saw the verdict."
  },
  {
    "id": "FR-004-AC-9",
    "path": "spec/accounting/functional/FR-004-campaign-accounting.md",
    "role": "examined",
    "excerpt": "Encoded snapshots emit `schemaVersion`, `requirement`, `revision`, `counterSemantics`, `counts` in that order, with `accepted`, `rejected`, `failed`, `discarded` in that order inside `counts`; byte-for-byte comparison of encoded output observes this order."
  },
  {
    "id": "FR-004-AC-10",
    "path": "spec/accounting/functional/FR-004-campaign-accounting.md",
    "role": "examined",
    "excerpt": "An unknown top-level or `counts` member is refused at its key before its value is read. In `src/snapshot_json.rs`, the unknown-key arm of `FieldVisitor::visit_str` must return an error before `SnapshotSeed` or `CountsSeed` can call `next_value` or `next_value_seed` for that member; neither visitor may consume an unknown value with `IgnoredAny` or an equivalent skip/decode path."
  },
  {
    "id": "FR-004-AC-11",
    "path": "spec/accounting/functional/FR-004-campaign-accounting.md",
    "role": "examined",
    "excerpt": "The decoder validates each member without materializing an intermediate generic JSON value tree."
  },
  {
    "id": "FR-004-AC-12",
    "path": "spec/accounting/functional/FR-004-campaign-accounting.md",
    "role": "examined",
    "excerpt": "Parser scratch on the `decode_campaign_snapshot` path remains bounded proportionally to the input cap of `MAX_BYTES` (65536 bytes), including escaped-string scratch and owned decoded identities; no input can cause scratch allocation to grow without a bound derived from that cap."
  },
  {
    "id": "FR-001-AC-1",
    "path": "spec/core/functional/FR-001-verdict-observation.md",
    "role": "examined",
    "excerpt": "The three verdicts remain distinct through construction and pattern matching."
  },
  {
    "id": "FR-001-AC-2",
    "path": "spec/core/functional/FR-001-verdict-observation.md",
    "role": "examined",
    "excerpt": "Every verdict carries requirement, revision, execution-point, and observation identity."
  },
  {
    "id": "FR-001-AC-4",
    "path": "spec/core/functional/FR-001-verdict-observation.md",
    "role": "examined",
    "excerpt": "The five clause outcomes \u2014 passed, failed, rejected, not-evaluated, undefined \u2014 are distinct through construction and pattern matching, and a failed or rejected clause retains its typed code, clause identity and optional borrowed detail."
  },
  {
    "id": "FR-002-AC-1",
    "path": "spec/core/functional/FR-002-safe-operators.md",
    "role": "examined",
    "excerpt": "Truth-table tests cover all short-circuit and total operators."
  },
  {
    "id": "FR-002-AC-2",
    "path": "spec/core/functional/FR-002-safe-operators.md",
    "role": "examined",
    "excerpt": "Evaluation-count tests prove the distinct operand evaluation contracts."
  },
  {
    "id": "FR-002-AC-3",
    "path": "spec/core/functional/FR-002-safe-operators.md",
    "role": "examined",
    "excerpt": "Boundary tests and Kani harnesses cover every definedness helper family."
  },
  {
    "id": "FR-002-AC-4",
    "path": "spec/core/functional/FR-002-safe-operators.md",
    "role": "examined",
    "excerpt": "`CheckedInteger` is implemented for exactly the twelve built-in integer types, each member agrees with the primitive `checked_*` operation, and the trait cannot be implemented outside the crate."
  },
  {
    "id": "interface-001-AC-1",
    "path": "spec/core/functional/interface-001-runtime-api.md",
    "role": "examined",
    "excerpt": "The runtime shall define no `filament_contract_runtime::exact` module."
  },
  {
    "id": "interface-001-AC-2",
    "path": "spec/core/functional/interface-001-runtime-api.md",
    "role": "examined",
    "excerpt": "The runtime shall not re-export, by `pub use`, alias, wrapper or feature, any item that `filament-exact`, `filament-semantic-value` or the evaluation leaf crate exports."
  },
  {
    "id": "interface-001-AC-3",
    "path": "spec/core/functional/interface-001-runtime-api.md",
    "role": "examined",
    "excerpt": "Where the upstream `filament-exact` crate exports an item name, the runtime shall contain no public item definition with that name."
  },
  {
    "id": "interface-001-AC-4",
    "path": "spec/core/functional/interface-001-runtime-api.md",
    "role": "examined",
    "excerpt": "The runtime shall expose no item named in the `kernel.consumed` lists of the `exact` contract block at any `filament_contract_runtime` path, whether defined or re-exported there."
  },
  {
    "id": "interface-001-AC-5",
    "path": "spec/core/functional/interface-001-runtime-api.md",
    "role": "examined",
    "excerpt": "The runtime shall define none of `Value`, `ValueType`, `Outcome`, `Refusal`, `Undefined`, `BoundViolation`, `Meter`, `ChargePoint`, `Incomplete`, `ScalarLimits`, `NodeKey`, `Origin` or `Location` (the `named_kernel_types` list): an explicit per-type instance of interface-001-AC-3."
  },
  {
    "id": "interface-001-AC-6",
    "path": "spec/core/functional/interface-001-runtime-api.md",
    "role": "examined",
    "excerpt": "The runtime's library source shall not call a `NodeKey` constructor."
  },
  {
    "id": "interface-001-AC-7",
    "path": "spec/core/functional/interface-001-runtime-api.md",
    "role": "examined",
    "excerpt": "The runtime shall not define `Frame`, `Body`, `CheckedPackage`, `Evaluation` or `plan_call` in its own source (FR-275; no exception, no expiry)."
  },
  {
    "id": "interface-001-AC-8",
    "path": "spec/core/functional/interface-001-runtime-api.md",
    "role": "examined",
    "excerpt": "The runtime shall define the `negotiate_*` predicates AD-016 WP7 selects (today: `negotiate_integer_division`, `negotiate_ieee`) and the requirement, capability and disposition types they take and return in its own source."
  },
  {
    "id": "interface-001-AC-9",
    "path": "spec/core/functional/interface-001-runtime-api.md",
    "role": "examined",
    "excerpt": "While a residue `exact` operation exists in the runtime, an operation the correspondence table above maps to a `filament-exact` operation shall call the `filament-exact` operation the table maps it to."
  },
  {
    "id": "interface-001-AC-10",
    "path": "spec/core/functional/interface-001-runtime-api.md",
    "role": "examined",
    "excerpt": "The runtime shall define every item the `core_items` list names in its `verdict`, `observation` and `accounting` modules."
  },
  {
    "id": "interface-001-AC-11",
    "path": "spec/core/functional/interface-001-runtime-api.md",
    "role": "examined",
    "excerpt": "The runtime shall depend on `filament-exact` and `filament-semantic-value` only through the `exact` feature."
  },
  {
    "id": "interface-001-AC-13",
    "path": "spec/core/functional/interface-001-runtime-api.md",
    "role": "examined",
    "excerpt": "While the `exact` feature is enabled and the `std` feature is disabled, the runtime shall build for `thumbv7em-none-eabi` at the Rust version that `compatibility.msrv` declares."
  },
  {
    "id": "interface-001-AC-14",
    "path": "spec/core/functional/interface-001-runtime-api.md",
    "role": "examined",
    "excerpt": "The runtime's normal, build and dev dependency graphs shall include no crate from the `agent-ix/filament-spec-language` Git repository."
  },
  {
    "id": "interface-001-AC-15",
    "path": "spec/core/functional/interface-001-runtime-api.md",
    "role": "examined",
    "excerpt": "Where the `exact` feature is disabled, the runtime's `cfg(kani)` verification module shall reference no `filament_exact` item, so that a default-feature dependent compiles under Kani; the `filament_exact`-dependent IEEE harness and its imports are compiled only under `exact`."
  },
  {
    "id": "NFR-001-AC-1",
    "path": "spec/core/non-functional/NFR-001-no-std-footprint.md",
    "role": "examined",
    "excerpt": "The default feature profile compiles without `std` or an allocator."
  },
  {
    "id": "NFR-001-AC-2",
    "path": "spec/core/non-functional/NFR-001-no-std-footprint.md",
    "role": "examined",
    "excerpt": "The library compiles with no `unsafe` code."
  },
  {
    "id": "NFR-001-AC-3",
    "path": "spec/core/non-functional/NFR-001-no-std-footprint.md",
    "role": "examined",
    "excerpt": "On the root `Cargo.toml` `rust-version` compiler for `thumbv7em-none-eabi`, the fixed-population static-library consumer in `measurement/footprint/` has linked `.text` plus `.rodata` between 500 bytes and 4 KiB and its runtime/harness objects retain no panic-path reference."
  },
  {
    "id": "NFR-001-M-1",
    "path": "spec/core/non-functional/NFR-001-no-std-footprint.md",
    "role": "examined",
    "excerpt": "Unsafe blocks"
  },
  {
    "id": "NFR-001-M-2",
    "path": "spec/core/non-functional/NFR-001-no-std-footprint.md",
    "role": "examined",
    "excerpt": "Linked `.text` + `.rodata`"
  },
  {
    "id": "NFR-002-AC-1",
    "path": "spec/core/non-functional/NFR-002-panic-compatibility-license.md",
    "role": "examined",
    "excerpt": "Valid public evaluation and accounting inputs encounter no intentional panic path."
  },
  {
    "id": "NFR-002-AC-3",
    "path": "spec/core/non-functional/NFR-002-panic-compatibility-license.md",
    "role": "examined",
    "excerpt": "Public core and remaining expression-residue data enums whose evolution affects downstream matching remain non-exhaustive, as the `compile_fail` doctests in `src/observation.rs` and `src/verdict.rs` show. The five runtime-owned scalar enums are closed and exhaustive under AD-004 Q-4."
  },
  {
    "id": "NFR-002-AC-5",
    "path": "spec/core/non-functional/NFR-002-panic-compatibility-license.md",
    "role": "examined",
    "excerpt": "The crate manifest declares `license = \"AGPL-3.0-or-later\"`."
  },
  {
    "id": "NFR-002-AC-6",
    "path": "spec/core/non-functional/NFR-002-panic-compatibility-license.md",
    "role": "examined",
    "excerpt": "The crate manifest declares `publish = false`, disabling registry publication for this package."
  },
  {
    "id": "NFR-002-AC-7",
    "path": "spec/core/non-functional/NFR-002-panic-compatibility-license.md",
    "role": "examined",
    "excerpt": "`make deny` passes its license-policy check for the resolved dependency set."
  },
  {
    "id": "NFR-002-AC-8",
    "path": "spec/core/non-functional/NFR-002-panic-compatibility-license.md",
    "role": "examined",
    "excerpt": "On the declared MSRV and `thumbv7em-none-eabi`, the `exact`-enabled, `std`-disabled TC-206 probe retains calls into the runtime-owned `scalar` negotiators and Boolean connective and the runtime's remaining exact expression surface. The gate reports its artifact and inspected runtime-owned object population and fails if that population is empty, a required call is absent, or any retained runtime-owned object has a relocation to a recognized Rust panic entry point. This is a separate gate from the default NFR-001 footprint and imposes no 4 KiB ceiling on exact."
  },
  {
    "id": "NFR-002-AC-9",
    "path": "spec/core/non-functional/NFR-002-panic-compatibility-license.md",
    "role": "examined",
    "excerpt": "A scratch probe with a reachable runtime-owned panic call produces a recognized panic relocation and makes the exact-profile gate fail; the same gate passes its unmodified probe when no recognized panic relocation is present. Missing build or inspection tools, missing artifacts, and an unparseable relocation report fail closed."
  },
  {
    "id": "NFR-002-AC-10",
    "path": "spec/core/non-functional/NFR-002-panic-compatibility-license.md",
    "role": "examined",
    "excerpt": "The resolved `filament-exact` dependency exposes `NonZeroInteger::try_from(&Integer)` with typed zero-divisor refusal, and its public `exact_div`, `div_rem_truncating` and `div_mod_floor` require an admitted `NonZeroInteger`, not a plain `&Integer`. Direct zero-divisor admission returns `Err`; all three plain-borrow calls fail to compile. An older locked kernel without this contract does not qualify."
  },
  {
    "id": "NFR-002-AC-11",
    "path": "spec/core/non-functional/NFR-002-panic-compatibility-license.md",
    "role": "examined",
    "excerpt": "For a current UID with an OS account entry, the host gate selects its tool home from that account even when caller `HOME` names a different directory."
  },
  {
    "id": "NFR-002-M-1",
    "path": "spec/core/non-functional/NFR-002-panic-compatibility-license.md",
    "role": "examined",
    "excerpt": "Intentional panic sites in library code"
  },
  {
    "id": "NFR-002-M-2",
    "path": "spec/core/non-functional/NFR-002-panic-compatibility-license.md",
    "role": "examined",
    "excerpt": "License policy violations"
  },
  {
    "id": "NFR-002-M-3",
    "path": "spec/core/non-functional/NFR-002-panic-compatibility-license.md",
    "role": "examined",
    "excerpt": "Registry publication enabled"
  },
  {
    "id": "FR-006-AC-1",
    "path": "spec/exact/functional/FR-006-exact-outcomes-and-accounting.md",
    "role": "examined",
    "excerpt": "The four outcome dispositions are distinct; completed `false` is a value. `Refusal` and `Undefined` are closed enums; `Incomplete` is a typed record whose reason uses the closed `LimitKind` and `ChargePoint` enums. The runtime consumes these kernel types directly under FR-275."
  },
  {
    "id": "FR-006-AC-3",
    "path": "spec/exact/functional/FR-006-exact-outcomes-and-accounting.md",
    "role": "examined",
    "excerpt": "Every charge point and limit kind round-trips its QSpec spelling; charges precede work; size counters are high-water, work/result cumulative; the first short counter in field order is reported with the exact denied amount."
  },
  {
    "id": "FR-006-AC-4",
    "path": "spec/exact/functional/FR-006-exact-outcomes-and-accounting.md",
    "role": "examined",
    "excerpt": "An injected denial at any admitted charge point yields `Incomplete` on `work_units` naming that point, with no result units and no partial value."
  },
  {
    "id": "FR-006-AC-6",
    "path": "spec/exact/functional/FR-006-exact-outcomes-and-accounting.md",
    "role": "examined",
    "excerpt": "Inspection identifies [filament-exact FR-096-AC-8](ix://agent-ix/filament-exact/FR-096) as the owner of `Refusal::code()` and `Refusal::cause()` for the twelve kernel refusal causes and `CheckedInvariant`. Under FR-275, RT consumes the typed kernel `Outcome::Refused(Refusal)` directly, with no RT record or code/cause mapping."
  },
  {
    "id": "FR-006-AC-7",
    "path": "spec/exact/functional/FR-006-exact-outcomes-and-accounting.md",
    "role": "examined",
    "excerpt": "Inspection of `src/exact/` finds no host floating-point types, fields, casts or operations in the exact surface, including `f32` and `f64` uses."
  },
  {
    "id": "FR-006-AC-8",
    "path": "spec/exact/functional/FR-006-exact-outcomes-and-accounting.md",
    "role": "examined",
    "excerpt": "With `exact` enabled and `std` disabled, the runtime builds for `thumbv7em-none-eabi` on the supported MSRV through the `build-exact-no-std-msrv` row of `make test-features`."
  },
  {
    "id": "FR-006-AC-9",
    "path": "spec/exact/functional/FR-006-exact-outcomes-and-accounting.md",
    "role": "examined",
    "excerpt": "Every public item exposed through `filament_contract_runtime::exact` is re-exported by `src/exact/mod.rs` from a private child module; child module paths are inaccessible to consumers."
  },
  {
    "id": "FR-006-AC-10",
    "path": "spec/exact/functional/FR-006-exact-outcomes-and-accounting.md",
    "role": "examined",
    "excerpt": "Non-test code in `src/exact/` has no panic site."
  },
  {
    "id": "FR-007-AC-8",
    "path": "spec/exact/functional/FR-007-exact-scalar-families.md",
    "role": "examined",
    "excerpt": "The six rounding spellings are `exact`, `toward-zero`, `toward-positive`, `toward-negative`, `nearest-even` and `nearest-away`, corresponding to the six named `RoundingMode` variants. For positive and negative exact ties, `NearestEven` selects the neighbour with the even coefficient, `NearestAway` selects the neighbour with greater absolute coefficient, `TowardZero` selects the neighbour nearer zero, `TowardPositive` selects the ceiling and `TowardNegative` selects the floor. An omitted spelling is `Exact` and refuses a discarded nonzero digit."
  },
  {
    "id": "FR-007-AC-13",
    "path": "spec/exact/functional/FR-007-exact-scalar-families.md",
    "role": "examined",
    "excerpt": "The runtime's consumed FSV `CompoundUnit` Debug rendering matches a fixed expected string listing every field declared by `CompoundUnitFields`, in declaration order."
  },
  {
    "id": "FR-007-AC-15",
    "path": "spec/exact/functional/FR-007-exact-scalar-families.md",
    "role": "examined",
    "excerpt": "Decimal division with a target coefficient interval `[-100,100]` and scale `0` under `TowardZero`: `(-1, 0) / (-3, 0)` yields coefficient `0` from exact quotient `+1/3`; `(1, 0) / (-3, 0)` yields coefficient `0` with exact value `-1/3` in its loss. Under `NearestAway`, `(-1, 0) / (-2, 0)` has exact `+1/2` and yields coefficient `+1`."
  },
  {
    "id": "FR-007-AC-18",
    "path": "spec/exact/functional/FR-007-exact-scalar-families.md",
    "role": "examined",
    "excerpt": "With a domain admitting residues `1` and `2`, `7 mod 3 = 1`, `-7 mod 3 = 2`, `7 mod -3 = 1` and `-7 mod -3 = 2`, each satisfying `0 <= r < abs(b)` regardless of the selected `div`/`rem` law; `mod` takes no law argument. An out-of-domain `mod` remainder is refused without a value as `ModuloOutOfDomain`."
  },
  {
    "id": "FR-007-AC-19",
    "path": "spec/exact/functional/FR-007-exact-scalar-families.md",
    "role": "examined",
    "excerpt": "Under every `div`/`rem` profile, `div` checks only its exposed quotient and `rem` checks only its exposed remainder against the consumer domain; neither refuses because the unexposed member is outside. `10 div 5` returns `2` in `Int[1,10]` although its remainder is `0`, and `-10 rem -1` returns `0` in `Int[-10,5]` although its quotient is `10`. `-10 div -1` in `Int[-10,5]` refuses without a value as `DivisionOutOfDomain` naming the Quotient member. `9 rem 10` in `Int[0,5]` refuses without a value as `DivisionOutOfDomain` naming the Remainder member although its quotient is `0`."
  },
  {
    "id": "FR-008-AC-3",
    "path": "spec/exact/functional/FR-008-composite-collection-and-equality.md",
    "role": "examined",
    "excerpt": "`construct_collection` charges `collection.element` before running each deferred element and stops at the first non-completing element with no later element run; a completed element outside its declared type returns `CheckedInvariant { cause: CollectionElementNotAdmitted }`; `form_collection` refuses a type-mismatched occurrence before any charge; formation charges membership comparisons, `collection.bound` and `collection.result-retain` in that order, and a set or bag is stored in ascending canonical-key order."
  },
  {
    "id": "FR-008-AC-10",
    "path": "spec/exact/functional/FR-008-composite-collection-and-equality.md",
    "role": "examined",
    "excerpt": "When formation coalesces occurrences, the runtime charges one `collection.member-walk` and one `collection.member-test` per membership comparison for a set, bag or ordered set, and charges neither point for a sequence."
  },
  {
    "id": "FR-008-AC-11",
    "path": "spec/exact/functional/FR-008-composite-collection-and-equality.md",
    "role": "examined",
    "excerpt": "When a collection is retained, the runtime stores a sequence in supplied occurrence order, an ordered set as the first occurrence of each distinct member in first-occurrence order, a set as one occurrence of each distinct member in ascending canonical-key order, and a bag as every occurrence in ascending canonical-key order by multiplicity: equal occurrences are one member whose multiplicity is their number, and each is represented by that member's first-supplied value, as in ix://agent-ix/filament-specification/FR-144 and FR-144-AC-21."
  },
  {
    "id": "FR-008-AC-12",
    "path": "spec/exact/functional/FR-008-composite-collection-and-equality.md",
    "role": "examined",
    "excerpt": "When a retained collection is visited by equality planning or by a further formation, the runtime visits its elements in the order it stored them, for every one of the four kinds."
  },
  {
    "id": "FR-008-AC-4",
    "path": "spec/exact/functional/FR-008-composite-collection-and-equality.md",
    "role": "examined",
    "excerpt": "The type-owned canonical key totally orders every keyed type, ranks `Absent < Null < Present`, fixes set and bag canonical and visiting order, and is evaluated iteratively at a depth that would overflow a recursive host-stack walk."
  },
  {
    "id": "FR-008-AC-13",
    "path": "spec/exact/functional/FR-008-composite-collection-and-equality.md",
    "role": "examined",
    "excerpt": "For an `Option`/`Collection`-nested `ValueType` whose depth exceeds a recursive host-stack walk under the admitted source-size cap, `Clone`, `PartialEq`, `Debug` and `Drop` complete on a small-stack thread and a default-stack child process without host-stack overflow; unequal leaf, collection kind and bound remain unequal, and the shallow compact and alternate `Debug` output matches the derived representation exactly."
  },
  {
    "id": "FR-009-AC-1",
    "path": "spec/exact/functional/FR-009-i13-backend-negotiation.md",
    "role": "examined",
    "excerpt": "For every input slice, both negotiators return exactly one disposition per item in input order, including for the empty slice, and permuting the input permutes the result identically."
  },
  {
    "id": "FR-009-AC-2",
    "path": "spec/exact/functional/FR-009-i13-backend-negotiation.md",
    "role": "examined",
    "excerpt": "A `Mathematical` consumer is `Supported`; a `Finite` consumer is `Supported` exactly when `operand`, `intermediate` and `result` are all present, and `RequiresBound` for each of the seven incomplete bound subsets."
  },
  {
    "id": "FR-009-AC-3",
    "path": "spec/exact/functional/FR-009-i13-backend-negotiation.md",
    "role": "examined",
    "excerpt": "IEEE causes are decided in the order width, operation, rounding, exceptional policy, first failure wins: an item failing two checks reports the earlier cause, and a non-rounding operation with an unsupported rounding direction is not `Unsupported(Rounding(..))`."
  },
  {
    "id": "FR-009-AC-4",
    "path": "spec/exact/functional/FR-009-i13-backend-negotiation.md",
    "role": "examined",
    "excerpt": "`requires_finite_proof` yields `RequiresBound` only when no `unsupported` cause applies; an item that both lacks a capability and needs an undischargeable proof reports the capability cause."
  },
  {
    "id": "FR-009-AC-5",
    "path": "spec/exact/functional/FR-009-i13-backend-negotiation.md",
    "role": "examined",
    "excerpt": "No `IeeeDisposition` is convertible into an `Outcome` variant, as the `compile_fail` doctest on `IeeeDisposition` (`src/scalar/ieee.rs`) shows."
  },
  {
    "id": "FR-010-AC-1",
    "path": "spec/exact/functional/FR-010-injected-charge-denial-seam.md",
    "role": "examined",
    "excerpt": "For every charge point that an RT-owned residue operation can issue through the `filament-exact` meter, an occurrence-1 injected denial returns `Incomplete` with `WorkUnits` and that point; the observed work consumption equals the record's `consumed`, result consumption is zero, and the denied point is absent from the admitted-charge log. [filament-exact FR-358-AC-1](ix://agent-ix/filament-exact/FR-358) owns full meter-state atomicity."
  },
  {
    "id": "FR-010-AC-6",
    "path": "spec/exact/functional/FR-010-injected-charge-denial-seam.md",
    "role": "examined",
    "excerpt": "A 0-based `occurrence` cannot be constructed, so an injected denial can never silently match no charge and degrade into \"no fault injected\"."
  },
  {
    "id": "FR-011-AC-3",
    "path": "spec/exact/functional/FR-011-meter-state-at-a-stop.md",
    "role": "examined",
    "excerpt": "A lazy connective skips its right operand when the left decides the result; for every connective kind and every decided operand pair, its completed result admits exactly one `boolean.result-retain` charge."
  },
  {
    "id": "FR-011-AC-8",
    "path": "spec/exact/functional/FR-011-meter-state-at-a-stop.md",
    "role": "examined",
    "excerpt": "A connective whose right operand stops returns that stop unchanged, admits no `boolean.result-retain` charge and consumes no result unit."
  },
  {
    "id": "FR-012-AC-3",
    "path": "spec/exact/functional/FR-012-carried-compiler-vocabulary.md",
    "role": "examined",
    "excerpt": "`SelectionRefusalCode::ALL` is the eight codes in normative check order, `as_str` yields the lock spelling for each, `from_code` resolves exactly those eight spellings and nothing else, and `PackageRefusalCode::as_str` is `invalid_package`."
  },
  {
    "id": "FR-012-AC-6",
    "path": "spec/exact/functional/FR-012-carried-compiler-vocabulary.md",
    "role": "examined",
    "excerpt": "At the IR-882 step-4 cutover, inspection finds no RT-local `NodeKey`, no RT `from_bytes` or `from_hex` constructor, and no TC-033 parser or round-trip test of those local constructors. RT library code has no `NodeKey` construction or hex decoder."
  },
  {
    "id": "FR-012-AC-7",
    "path": "spec/exact/functional/FR-012-carried-compiler-vocabulary.md",
    "role": "examined",
    "excerpt": "After the R-3 cutover, inspection finds no RT-local `PackageCause`, `PackageRefusal` or `PackageRefusalCode` definition, type alias, public re-export or adapter. The RT consumers of selection and package refusals use FSV's definition types directly; `RevisionMismatch`, `DigestDomainMismatch` and `ByteDigestMismatch` are absent from RT's `invalid_package` surface, while FR-012-AC-3's eight selection spellings and `invalid_package` code remain available from FSV."
  },
  {
    "id": "FR-012-AC-8",
    "path": "spec/exact/functional/FR-012-carried-compiler-vocabulary.md",
    "role": "examined",
    "excerpt": "Inspection finds no RT library or test fixture that constructs a semantic identity from bytes or constituent parts, and no RT-owned digest-domain constant, fixed digest oracle, or replacement identity pin. The producer-origin tests of RT consumers run in `filament-integration` and obtain identities from admitted checked-package values through FSL's read-only lookup; the RT repository carries no copied identity fixture or FSL/IR dependency."
  },
  {
    "id": "FR-273-AC-1",
    "path": "spec/exact/functional/FR-273-exact-function-application.md",
    "role": "examined",
    "excerpt": "`CheckedPackage::call` and `CheckedPackage::evaluate` are called only against a package `PackageDeclarations::check` admitted under `CheckMode::Linked`; a package this crate's `PackageDeclarations::check` rejects is never applied."
  },
  {
    "id": "FR-273-AC-2",
    "path": "spec/exact/functional/FR-273-exact-function-application.md",
    "role": "examined",
    "excerpt": "Declared arity is decided before any per-argument check, each argument's value kind and carried references are validated in parameter order, and all of that precedes the `function.call` charge, which itself precedes the function's body on every `call`."
  },
  {
    "id": "FR-273-AC-3",
    "path": "spec/exact/functional/FR-273-exact-function-application.md",
    "role": "examined",
    "excerpt": "Arity, value-kind and dangling-reference input mismatches, and an unknown function name, each refuse as the matching `InputRefusal` variant before any charge; no `Meter` observes a refused call."
  },
  {
    "id": "FR-273-AC-4",
    "path": "spec/exact/functional/FR-273-exact-function-application.md",
    "role": "examined",
    "excerpt": "A function whose declared operator requirements no registered backend can discharge negotiates `unsupported`, naming the required capability, before any application; the disposition is never an `Outcome` variant, never an `InputRefusal`, and takes no `Meter`."
  },
  {
    "id": "FR-273-AC-6",
    "path": "spec/exact/functional/FR-273-exact-function-application.md",
    "role": "examined",
    "excerpt": "`CheckMode::Kernel` application is out of scope: no test in this requirement's corpus applies a package checked only under `CheckMode::Kernel`."
  },
  {
    "id": "FR-273-AC-7",
    "path": "spec/exact/functional/FR-273-exact-function-application.md",
    "role": "examined",
    "excerpt": "A checked, decreasing function completes 4,096 runtime-managed calls on a 64 KiB native stack when `work_units` suffices; across depths 1, 128 and 4,096, no two generated-body transitions are simultaneously active, and inspection shows the scheduler returns to one loop before invoking the next transition. No depth-specific refusal or incomplete outcome exists."
  },
  {
    "id": "FR-273-AC-8",
    "path": "spec/exact/functional/FR-273-exact-function-application.md",
    "role": "examined",
    "excerpt": "A foreign checked expression, an absent function requested within a checked body, a re-entrant meter borrow, and direct host re-entry into an active checked package carry `ForeignCheckedExpression`, `UnknownCheckedFunction`, `MeterBorrowConflict`, and `PackageReentry` respectively; host re-entry is refused before nested charge, and none is treated as an ordinary input refusal."
  },
  {
    "id": "FR-273-AC-9",
    "path": "spec/exact/functional/FR-273-exact-function-application.md",
    "role": "examined",
    "excerpt": "For an admitted chain of `N` calls whose bodies only request the next call or return a literal, the expected charge vector is `function.call` repeated `N` times and the expected `work_units` spend is `N`. A limit of `N` completes; a limit of `N - 1` returns `Incomplete` at the Nth `function.call`, naming `work_units`, with exactly `N - 1` calls in both the counter and log, and without changing the checked package's static totality verdict."
  },
  {
    "id": "FR-273-AC-10",
    "path": "spec/exact/functional/FR-273-exact-function-application.md",
    "role": "examined",
    "excerpt": "In a nested call with two argument applications and an enclosing application, the charge vector is exactly three `function.call` entries in left argument, right argument, enclosing call order; the enclosing charge precedes parameter binding and body work. With `work_units: 2`, the enclosing charge is denied, the log and counter retain exactly the first two calls, and no enclosing body work occurs."
  },
  {
    "id": "FR-273-AC-11",
    "path": "spec/exact/functional/FR-273-exact-function-application.md",
    "role": "examined",
    "excerpt": "A resumable body transition returns a child-call request while its owned parent state retains live locals and the child-result destination; after the child completes, the runtime resumes that parent with the child's value and does not invoke a second body transition from within the first. A stopped child propagates without resuming the parent."
  },
  {
    "id": "FR-273-AC-12",
    "path": "spec/exact/functional/FR-273-exact-function-application.md",
    "role": "examined",
    "excerpt": "After AD-004 step 5, the RT consumer invokes both an admitted checked input and a CG-generated resumable body through the same FSL-owned evaluation-leaf interface with `std` disabled; for each shared input the outcome or typed refusal, source location and loss, consumed work and ordered charge log equal FSL's std reference. Shared inputs include a completed decimal rounding with a nonempty `ValueLoss::Decimal`, a completed IEEE operation or conversion with a nonempty `ValueLoss::IeeeFlags` or `ValueLoss::IeeeExact`, and an outcome stopped at an executed expression node whose `Evaluation.locati"
  },
  {
    "id": "FR-273-AC-13",
    "path": "spec/exact/functional/FR-273-exact-function-application.md",
    "role": "examined",
    "excerpt": "On a native thread with a 512 KiB stack, the checked decreasing `count(100000)` call through the consumed no_std evaluator and a generated-body call for the same checked input each return `100000` with work limit `w`, where `w` is that run's measured spend; each returns `Incomplete` naming `work_units` at `w-1` with no denied charge in the counter or log, then returns `100000` again at `w`. The ordered charge sequence at all three limits matches the FSL std reference, and no depth refusal or native stack overflow occurs."
  },
  {
    "id": "FR-273-AC-14",
    "path": "spec/exact/functional/FR-273-exact-function-application.md",
    "role": "examined",
    "excerpt": "RT-local identity-free package function parameter/result checks and standalone-expression parameter/result checks preserve admitted types and the original semantic refusal cause, location and order through `try_check_type`. A dedicated allocator test denies actual owner worklist allocation after fixture construction at each of these four consumer positions; the result is the typed native reservation cause, retains `Allocation` with the owner's request unit and amount, publishes no checked result, and returns without aborting or allocating to project the error. An identical retry with allocatio"
  },
  {
    "id": "FR-275-AC-1",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "With `exact` enabled, no public item the runtime defines (in `scalar` or any other module) has the name of an item that `filament-exact` or `filament-semantic-value` exports."
  },
  {
    "id": "FR-275-AC-2",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "No module, alias or feature of the runtime keeps a removed kernel definition reachable; after the IR-882 value-bearing cutover, inspection finds no RT-defined second `Value`, `CheckedEquality` evaluator, pair walker or membership walker, `UnitId` resolver, `EnumShape` registry, `EffectiveId` registry, copy of `UnitTable`, `TypeEnvironment`, `EnumMemberIndex` or `EnumDeclaration`, conversion layer, adapter or old-`Value` re-export. Quantity, enum, reference and checked-equality paths use the FSV owners directly."
  },
  {
    "id": "FR-275-AC-3",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "`filament-exact` is an optional dependency of the runtime, enabled only by the `exact` feature."
  },
  {
    "id": "FR-275-AC-4",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "The optional `filament-exact` and `filament-semantic-value` dependencies use their own `agent-ix` Git repositories with `branch = \"main\"` and no `rev`, `tag`, `path` or committed `[patch]`."
  },
  {
    "id": "FR-275-AC-5",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "`Cargo.lock` holds exactly one entry each for `filament-exact`, `filament-semantic-value`, `quire-canonical` and `quire-canonical-derive`, and, after AD-004 step 5, the FSL-owned evaluation leaf."
  },
  {
    "id": "FR-275-AC-7",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "`deny.toml` admits only the `filament-exact`, `filament-semantic-value` and `quire-canonical` own-repository Git sources and the dev-only `ix-trace-rs` first-party tooling source before AD-004 step 5, then also the FSL-owned evaluation leaf's own-repository Git source; it keeps `unknown-git = \"deny\"` and never admits the FSL Git repository."
  },
  {
    "id": "FR-275-AC-8",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "`make deny` reports cargo-deny's `source-not-allowed` error for the FSL Git repository, and exits non-zero, when a normal, build or dev dependency resolves from it; a licence failure alone does not satisfy this."
  },
  {
    "id": "FR-275-AC-9",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "With `exact` enabled and `std` disabled, the runtime builds for `thumbv7em-none-eabi`. The row `build-exact-no-std-msrv` builds it on the root `Cargo.toml` `rust-version` floor."
  },
  {
    "id": "FR-275-AC-10",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "The dependency graph of `filament-contract-runtime-footprint` for `thumbv7em-none-eabi` contains no `filament-exact`, `filament-semantic-value`, `quire-canonical` or `quire-canonical-derive`, and after AD-004 step 5 contains no evaluation leaf."
  },
  {
    "id": "FR-275-AC-11",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "`make size` measures linked `.text` plus `.rodata` inside NFR-001-AC-3's 500 byte to 4 KiB band."
  },
  {
    "id": "FR-275-AC-12",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "The runtime has no test that compares its output with a second implementation of the kernel or that depends on a crate from the FSL Git repository."
  },
  {
    "id": "FR-275-AC-13",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "The runtime contains no file copied from the FSL repository and no port of FSL code, where a port is code that keeps the FSL authority's item names and order. The residue list is not an allowance: every item on it is a violation of this criterion, which stays unmet while the list is non-empty. The runtime-owned negotiators are not ports."
  },
  {
    "id": "FR-275-AC-14",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "The kernel move deletes no requirement, acceptance criterion or test case."
  },
  {
    "id": "FR-275-AC-15",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "Every matrix row whose evidence leaves the runtime in the kernel move carries a planned status with a stated reason, because the status vocabulary has no \"verified upstream\" status (a planner question, no status is invented)."
  },
  {
    "id": "FR-275-AC-16",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "The runtime has no `filament_contract_runtime::exact` module and no `pub use` of `filament-exact`, `filament-semantic-value` or the evaluation leaf crate; the only items it defines under the `exact` feature are the `scalar` items (the backend negotiators and their types, `evaluate_boolean_short_circuit` and `ShortCircuitConnective`), and no file under `src/exact` exists."
  },
  {
    "id": "FR-275-AC-17",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "Every item the runtime defines under the `exact` feature, other than the `scalar` items, is named in the residue list, and the list records no exception, expiry or approval."
  },
  {
    "id": "FR-275-AC-18",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "The residue list is empty."
  },
  {
    "id": "FR-275-AC-19",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "The runtime defines `negotiate_integer_division`, `negotiate_ieee` and their types in its own source and depends on no FSL crate for them."
  },
  {
    "id": "FR-275-AC-20",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "The runtime's root `Cargo.toml` declares one `rust-version` for all feature profiles; the MSRV and footprint gates read that field as their compiler floor without another fixed version value."
  },
  {
    "id": "FR-275-AC-21",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "`make msrv` and `make size` build with the root `Cargo.toml` `rust-version` compiler; changing that field changes the compiler selected by both gates, and a missing or unavailable declared compiler fails either gate."
  },
  {
    "id": "FR-275-AC-22",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "Inspection of runtime source finds no local definition or alias of FSV's `SemanticGraphCause`, `InvalidSemanticGraph`, or semantic-node term checker, including definitions emitted by macros."
  },
  {
    "id": "FR-275-AC-29",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "After AD-004 step 5, with `exact` enabled and `std` disabled on the root `Cargo.toml` `rust-version`, the RT consumer and a generated-body consumer of the FSL-owned evaluation leaf compile for `thumbv7em-none-eabi` using one lock entry for that leaf; neither consumer resolves the FSL workspace Git source, an RT-local evaluator copy, or a compatibility alias. A host build of the same no_std profile executes the checked-input and generated-body cases of FR-273-AC-12 and AC-13."
  },
  {
    "id": "FR-275-AC-30",
    "path": "spec/exact/functional/FR-275-single-exact-kernel.md",
    "role": "examined",
    "excerpt": "After AD-004 step 5, `make size` still measures the default fixed population at 500 bytes through 4 KiB linked `.text` plus `.rodata` with no evaluation leaf in its graph and no panic relocation. A separate `measurement/evaluator` no_std executable that links RT, the FSL evaluation leaf and one generated-body consumer for `thumbv7em-none-eabi` has its linked ELF path and `.text` plus `.rodata` byte sum reported from `llvm-size -A`. A solitary native FR-273-AC-13 deep-test executable has its peak resident set size reported in bytes from `/usr/bin/time -v`'s `Maximum resident set size` field, wi"
  },
  {
    "id": "FR-277-AC-7",
    "path": "spec/exact/functional/FR-277-checked-equality-evaluation.md",
    "role": "examined",
    "excerpt": "The IR-241 Kani claim remains `plan_equality(left, right).pair_events() == count_of_EqualityPair_charges_from_the_same_real_CheckedEquality::evaluate(left, right, meter)` for both equal and first-head-unequal bounded operands, with the existing exact operand bound and proof ceiling. A plan-only equality or duplicated FSL walker does not satisfy this criterion."
  },
  {
    "id": "FR-277-AC-8",
    "path": "spec/exact/functional/FR-277-checked-equality-evaluation.md",
    "role": "examined",
    "excerpt": "Inspection of the locked FSV `CheckedEquality::evaluate` path shows a direct call to `filament_exact::planned_equality_with_plan` on the evaluated operands and use of that call's Boolean relation; the same call admits the complete 17-event pair schedule through its meter, and RT defines no local `CheckedEquality` or pair walker. A separate kernel call does not establish this criterion."
  },
  {
    "id": "FR-278-AC-1",
    "path": "spec/exact/functional/FR-278-runtime-checked-invariant-causes.md",
    "role": "examined",
    "excerpt": "Every RT checked-package/function invariant producer returns its table cause: unknown name is `UnknownCheckedFunction`, a foreign expression is `ForeignCheckedExpression`, and each meter reborrow is `MeterBorrowConflict`. Runtime-managed calls use explicit frames and `work_units` fuel under RT FR-273; the final carrier has no `CallDepthExceeded` variant, and fuel exhaustion is `Incomplete` with `limit_kind: work_units`, never `CheckedInvariant`."
  },
  {
    "id": "FR-276-AC-1",
    "path": "spec/monitor/functional/FR-276-consume-timed-monitor-plan.md",
    "role": "examined",
    "excerpt": "With a 20-bit 1 MHz counter and zero uncertainty, request at tick 0 (covering `[0, 1)`) and first acknowledgement at 2998, 3000, or 3001 yield respectively definite true (difference in `(2997, 2999)`), indeterminate (`(2999, 3001)`, which straddles the bound 3000) and definite false (`(3000, 3002)`) for the 3 ms obligation; with 2 \u00b5s uncertainty the 2998 case (`(2993, 3003)`) remains indeterminate. No boundary case is decided from a point estimate."
  },
  {
    "id": "FR-276-AC-2",
    "path": "spec/monitor/functional/FR-276-consume-timed-monitor-plan.md",
    "role": "examined",
    "excerpt": "The FSL plan's 22-slot buffer for `once[0 ms, 10 ms] holds(p)` at 2 events/ms on a 1 MHz counter (capacity `ceil(rate x R) + 1` with `R = b + 1 + 2u`, FSL FR-251-AC-2; see AC-12) admits 22 in-window events; the 23rd yields `Incomplete(LimitReached)` naming limit `event_buffer` and setting `monitor.max_event_rate` (the setting key; the capacity is the amount, per FR-251's Overflow rule) (an instance beyond `activation_capacity` is likewise not started and yields `limit` `activation`, setting `monitor.max_activations`), without dropping that event or changing an unrelated obligation. The runtime"
  },
  {
    "id": "FR-276-AC-3",
    "path": "spec/monitor/functional/FR-276-consume-timed-monitor-plan.md",
    "role": "examined",
    "excerpt": "Under a 16-bit counter with maximum gap 100, readings 65530 then 4 advance by 10 (RT passes `on_event` the delta 10); readings 65530 then 65500 make RT call `on_gap` with 65506 and not `on_event`; each instance still open across the fault settles `Failed(ReadingGapExceeded{gap: 65506, max_reading_gap: 100})` with no temporal verdict. A plan whose maximum gap is 65536 is refused before construction."
  },
  {
    "id": "FR-276-AC-4",
    "path": "spec/monitor/functional/FR-276-consume-timed-monitor-plan.md",
    "role": "examined",
    "excerpt": "Changing the counter identity, unit, width, profile or admitted order never reuses the first plan's monitor state or settles its obligation; equal timestamps without admitted order never acquire causality from arrival order."
  },
  {
    "id": "FR-276-AC-5",
    "path": "spec/monitor/functional/FR-276-consume-timed-monitor-plan.md",
    "role": "examined",
    "excerpt": "The step API carries distinct definite, pending, indeterminate, incomplete and failed outcomes with the affected obligation identities; a limit or fault on one obligation does not turn a sibling's state into a verdict or erase its identity."
  },
  {
    "id": "FR-276-AC-6",
    "path": "spec/monitor/functional/FR-276-consume-timed-monitor-plan.md",
    "role": "examined",
    "excerpt": "The complete admitted plan alone builds a monitor after driver preparation objects are dropped. Its checked subject, activation/captures, atom bodies, ordered topology, `State` type and the `init`, `on_event` and `on_watermark` function entries (the plan-root node's dependencies, QSpec FR-487) remain available. Build runs `init` and the monitor's state is its result. Build consumes no event and emits no verdict; a second build has independent state, and neither monitor can be rebound to another plan. No source parse, second clause, callback or RT operator translation completes it."
  },
  {
    "id": "FR-276-AC-7",
    "path": "spec/monitor/functional/FR-276-consume-timed-monitor-plan.md",
    "role": "examined",
    "excerpt": "For each of a foreign atom/operand, missing entry body, changed `init` body, interval/buffer owner, activation binding, uncertainty, counter, counter width, tick unit, maximum event rate, buffer capacity, activation capacity and maximum gap under the original selection (each of uncertainty, counter, tick unit, counter width, gap, rate and capacities is part of the plan-root's identity, QSpec FR-487-AC-6), driver/IR admission refuses without RT initialization; equal numeric subformula IDs under different subjects do not alias. An unsupported entry operation yields `Unsupported`, and RT allocati"
  },
  {
    "id": "FR-276-AC-8",
    "path": "spec/monitor/functional/FR-276-consume-timed-monitor-plan.md",
    "role": "examined",
    "excerpt": "Invalid event/progress inputs, including a missing required admitted value, leave monitor state unchanged with no verdict. An admitted progress assertion can settle a deadline, while a mere counter poll cannot. Executing the admitted program agrees with FSL's reference evaluator on boundary, reversed-operand, false-activation and open/closed-endpoint cases; an RT executor invariant failure returns `Failed`, terminates the monitor and rejects later input."
  },
  {
    "id": "FR-276-AC-9",
    "path": "spec/monitor/functional/FR-276-consume-timed-monitor-plan.md",
    "role": "examined",
    "excerpt": "On the 16-bit target of AC-3 the first admitted reading, whatever its value, passes `on_event` the delta 0 with no gap check and leaves the unwrapped time at `init`'s value; after readings `65530` then `65500` fault, a following reading `65510` is differenced from `65500` (delta 10), not from `65530`. RT calls `on_gap` with the gap 65506: the instance still open across the gap settles `Failed(ReadingGapExceeded{gap: 65506, max_reading_gap: 100})` and is dropped from the state, while an instance already decided before the fault and an instance not yet started are unaffected and settle normally "
  },
  {
    "id": "FR-276-AC-10",
    "path": "spec/monitor/functional/FR-276-consume-timed-monitor-plan.md",
    "role": "examined",
    "excerpt": "With a per-step budget too small for one `on_event`, the call returns `StepResourceStop`, the monitor state is unchanged and the event unconsumed, and the same event under a sufficient budget then executes and gives the outcome it would have given; the result is distinct from a verdict, `Incomplete(LimitReached)`, `Failed(ReadingGapExceeded)` and `ExecutorInvariantFailure` (after which the monitor rejects input), and the monitor accepts the next input after a stop. No test relies on recovery from an allocator out-of-memory."
  },
  {
    "id": "FR-276-AC-11",
    "path": "spec/monitor/functional/FR-276-consume-timed-monitor-plan.md",
    "role": "examined",
    "excerpt": "Build observes event_position 0 from init. With width 16 and maximum gap 100, the baseline event reading 65530 calls on_event(0) and leaves event_position 1; a watermark and poll leave it 1; reading 65500 faults through on_gap and leaves it 1; admitted reading 65510 calls on_event(10) and leaves it 2. The unwrapped exact Integer count is independent of tick time, and State keeps it after activations with no extra field."
  },
  {
    "id": "FR-276-AC-12",
    "path": "spec/monitor/functional/FR-276-consume-timed-monitor-plan.md",
    "role": "examined",
    "excerpt": "For a plan with one bounded buffer and activation capacity 2, take the plan of AC-2 (`once[0 ms, 10 ms] holds(p)`, 2 events/ms = 0.002 per tick, 1 MHz counter, uncertainty 0). FSL FR-251 sets the buffer capacity to `ceil(rate x R) + 1` with the retention `R = b + 1 + 2u = 10000 + 1 + 0 = 10001` ticks, so `ceil(0.002 x 10001) + 1 = ceil(20.002) + 1 = 21 + 1 = 22`; the `buffer` field then holds at most 22 + 1 = 23 elements, the one extra being the operator's summary cell (the formula's `+ 1` is separate slack and the cell is not counted in the capacity). Each case on a fresh monitor: an `on_even"
  },
  {
    "id": "FR-276-AC-13",
    "path": "spec/monitor/functional/FR-276-consume-timed-monitor-plan.md",
    "role": "examined",
    "excerpt": "`Program::try_new` takes only `ProgramParts`. In a dedicated `filament-integration` test binary with producer-admitted `ProgramParts`, whose failing global allocator refuses the first allocation inside `try_new` (the first Layout type check's worklist), construction returns `ProgramRefusal` code `Membership` with the native reservation cause and no Program; refusing the first RT-owned scratch reservation returns code `Storage`; refusing an allocation inside a literal's membership walk returns `Membership` with the native `EnvironmentFailure`. An expression arena nested 20,000 levels deep const"
  },
  {
    "id": "FR-276-AC-14",
    "path": "spec/monitor/functional/FR-276-consume-timed-monitor-plan.md",
    "role": "examined",
    "excerpt": "In the linked `filament-integration` consumer PR, using producer-admitted identities rather than RT-owned fixtures, actual allocator denials inside Layout, function parameter/result and expression type checks return `Membership` with the original native allocation class and `StorageRequest`, without allocating to construct the refusal or returning a Program; allocation-enabled retries admit the same valid parts. Semantic unknown-type and operator-ineligible controls retain the existing `TypeMismatch` behavior and validation precedence. RT-local identity-free private native-error projection con"
  },
  {
    "id": "interface-002-AC-1",
    "path": "spec/monitor/functional/interface-002-monitor-program.md",
    "role": "examined",
    "excerpt": "After construction consumes the preparation parts and one Rc owner drops, another owner retains the complete root key with nested operand keys, selection bytes, all four entry associations, literal bodies and shared nominal declarations. Invalid arena lookups return absent. No monitor execution credit is granted by this construction control."
  },
  {
    "id": "interface-002-AC-2",
    "path": "spec/monitor/functional/interface-002-monitor-program.md",
    "role": "examined",
    "excerpt": "Missing, extra, optional, mistyped or misordered outer State fields (including final required Integer event_position), missing or mistyped on_gap, invalid counter width, a gap outside the declared width, negative uncertainty and a tick unit under another dimension yield the typed construction refusal before any entry executes; width64 with maximum gap u64::MAX remains representable. Activation capacity zero and a positive value above u64::MAX remain retained exactly, while a negative value refuses without a host-width truncation."
  },
  {
    "id": "interface-002-AC-3",
    "path": "spec/monitor/functional/interface-002-monitor-program.md",
    "role": "examined",
    "excerpt": "Duplicate function keys and duplicate expression source locations in one validated execution context refuse `DuplicateKey`; invalid expression edges, direct expression cycles including unreachable arena nodes, and a reachable argument of another function refuse with their distinct typed codes. A finite shared neutral subexpression and distinct inline body paths under the same source node remain admissible; a 20,000-level shared inline arena validates on a 512 KiB native stack without recursive graph descent."
  },
  {
    "id": "interface-002-AC-4",
    "path": "spec/monitor/functional/interface-002-monitor-program.md",
    "role": "examined",
    "excerpt": "Two compatible entry roles may reference the same retained function; construction does not add a distinct-function premise to FR-487."
  },
  {
    "id": "interface-002-AC-5",
    "path": "spec/monitor/functional/interface-002-monitor-program.md",
    "role": "examined",
    "excerpt": "Two functions using the same admitted State parameter node, delta parameter node and parameter-dependent IntegerAdd node admit distinct expression arena addresses when each copy's transitive binding owner is its own `FunctionId`. Both copies retain the original, equal `key` and `body_path` through `Program::expression`; the functions retain their distinct original keys and operand associations."
  },
  {
    "id": "interface-002-AC-6",
    "path": "spec/monitor/functional/interface-002-monitor-program.md",
    "role": "examined",
    "excerpt": "Two copies of one source location with the same derived function owner, two neutral copies, or a neutral and a bound copy refuse `DuplicateKey`. Mixed binding owners do not gain a duplicate-location exception; a reachable foreign argument refuses `ForeignArgument`, and a reachable foreign local or mixed local binding refuses `InvalidBinding`, without changing the source key or body path."
  },
  {
    "id": "interface-003-AC-1",
    "path": "spec/monitor/functional/interface-003-monitor-executor.md",
    "role": "examined",
    "excerpt": "A retained admitted program builds after preparation drops, executes its actual initializer and keeps its complete canonical State and fixed owner. Two builds have independent state slots, consume no event and produce no obligation result."
  },
  {
    "id": "interface-003-AC-2",
    "path": "spec/monitor/functional/interface-003-monitor-executor.md",
    "role": "examined",
    "excerpt": "Zero or insufficient work, stack and scratch limits stop initialization through the resource channel and return no Monitor. A lazy If does not execute its unselected branch; a helper chain spends bounded explicit continuations without Rust recursion."
  },
  {
    "id": "interface-003-AC-3",
    "path": "spec/monitor/functional/interface-003-monitor-executor.md",
    "role": "examined",
    "excerpt": "A dynamically wrong function result or operand reaches the shared conformance boundary and returns its typed failure rather than a false property result. Native limit/storage failures preserve the operating-stop channel."
  },
  {
    "id": "interface-003-AC-4",
    "path": "spec/monitor/functional/interface-003-monitor-executor.md",
    "role": "examined",
    "excerpt": "Replacing operating limits leaves the canonical State and fixed Program unchanged; a failed replacement reservation preserves the old limits. No compatibility default or live rebind is exposed."
  },
  {
    "id": "interface-004-AC-1",
    "path": "spec/monitor/functional/interface-004-monitor-lexical-bindings.md",
    "role": "examined",
    "excerpt": "Missing, duplicate, sparse and foreign local declarations refuse construction, while compact function-qualified bindings retain their original source locations."
  },
  {
    "id": "interface-004-AC-2",
    "path": "spec/monitor/functional/interface-004-monitor-lexical-bindings.md",
    "role": "examined",
    "excerpt": "A selected Let evaluates its value once and returns its scoped body's result; a lazy unselected binding is not activated. A differently annotated local uses shared admission and preserves its native failure."
  },
  {
    "id": "interface-004-AC-3",
    "path": "spec/monitor/functional/interface-004-monitor-lexical-bindings.md",
    "role": "examined",
    "excerpt": "Nested calls and recursive invocations cannot read an outer invocation's local as their own. A bind restores the prior invocation's slot on return, and an inactive read is a typed invariant failure."
  },
  {
    "id": "interface-004-AC-4",
    "path": "spec/monitor/functional/interface-004-monitor-lexical-bindings.md",
    "role": "examined",
    "excerpt": "Binding operands respect the scratch ceiling, including a shadowed outer operand. A stopped invocation clears only touched slots and cannot leak a binding into a subsequent invocation; deep binding chains use the explicit stack."
  },
  {
    "id": "interface-005-AC-1",
    "path": "spec/monitor/functional/interface-005-monitor-boolean-operations.md",
    "role": "examined",
    "excerpt": "Every BooleanNot truth-table row returns the opposite Boolean and both binary truth tables return their independently expected value."
  },
  {
    "id": "interface-005-AC-2",
    "path": "spec/monitor/functional/interface-005-monitor-boolean-operations.md",
    "role": "examined",
    "excerpt": "False And and true Or skip a recursive right operand, while true And and false Or reach its typed operating stop."
  },
  {
    "id": "interface-005-AC-3",
    "path": "spec/monitor/functional/interface-005-monitor-boolean-operations.md",
    "role": "examined",
    "excerpt": "Non-Boolean operand or result annotations refuse construction. Selected work/stack/scratch exhaustion retains its operating-stop channel and does not become a Boolean result."
  },
  {
    "id": "interface-006-AC-1",
    "path": "spec/monitor/functional/interface-006-monitor-tuple-projection.md",
    "role": "examined",
    "excerpt": "A projected canonical State remains valid after temporary projection owners and preparation objects drop; tuple position order determines the selected value."
  },
  {
    "id": "interface-006-AC-2",
    "path": "spec/monitor/functional/interface-006-monitor-tuple-projection.md",
    "role": "examined",
    "excerpt": "Record receivers, missing positions and mismatched result annotations refuse before entry execution."
  },
  {
    "id": "interface-006-AC-3",
    "path": "spec/monitor/functional/interface-006-monitor-tuple-projection.md",
    "role": "examined",
    "excerpt": "Retained projection addresses are charged to scratch; deep projections use the explicit machine, and source keys/body paths remain available without copying a subtree."
  },
  {
    "id": "interface-007-AC-1",
    "path": "spec/monitor/functional/interface-007-monitor-record-projection.md",
    "role": "examined",
    "excerpt": "Repeated reads use the declared member identity and retain the selected canonical value after temporary owners drop."
  },
  {
    "id": "interface-007-AC-2",
    "path": "spec/monitor/functional/interface-007-monitor-record-projection.md",
    "role": "examined",
    "excerpt": "Foreign owners, tuples, absent or optional fields, and mismatched result types refuse before execution."
  },
  {
    "id": "interface-007-AC-3",
    "path": "spec/monitor/functional/interface-007-monitor-record-projection.md",
    "role": "examined",
    "excerpt": "Projection addresses consume scratch and explicit continuations preserve source evidence without subtree copies or repeated declaration scans."
  },
  {
    "id": "interface-008-AC-1",
    "path": "spec/monitor/functional/interface-008-monitor-scalar-operations.md",
    "role": "examined",
    "excerpt": "Arithmetic and all four order relations agree with independent exact expectations, including integers beyond host width and bounded result refusal."
  },
  {
    "id": "interface-008-AC-2",
    "path": "spec/monitor/functional/interface-008-monitor-scalar-operations.md",
    "role": "examined",
    "excerpt": "Explicit native limits apply cumulatively across selected operations; inactive branches do not charge, and denial retains its exact request, native cause and source evidence without a value or temporal verdict."
  },
  {
    "id": "interface-008-AC-3",
    "path": "spec/monitor/functional/interface-008-monitor-scalar-operations.md",
    "role": "examined",
    "excerpt": "Computed values consume scratch; ordinary interpreter stops retain their exact units, and a stopped invocation cannot commit state or contaminate later execution."
  },
  {
    "id": "interface-009-AC-1",
    "path": "spec/monitor/functional/interface-009-monitor-composite-construction.md",
    "role": "examined",
    "excerpt": "Canonical record and tuple construction preserve declaration order and original member/value owners; reversed source member order does not change execution order."
  },
  {
    "id": "interface-009-AC-2",
    "path": "spec/monitor/functional/interface-009-monitor-composite-construction.md",
    "role": "examined",
    "excerpt": "Missing, duplicate, foreign or unknown required members, optional record declarations, wrong result shapes and wrong tuple arity refuse before operand execution."
  },
  {
    "id": "interface-009-AC-3",
    "path": "spec/monitor/functional/interface-009-monitor-composite-construction.md",
    "role": "examined",
    "excerpt": "An earlier stopped operand or bounded membership check prevents later execution; slot storage and native composite retention denials retain their typed operating channels without a partial value or state commit."
  },
  {
    "id": "interface-010-AC-1",
    "path": "spec/monitor/functional/interface-010-monitor-sequence-operations.md",
    "role": "examined",
    "excerpt": "Construction, exact size and flattening preserve duplicates, occurrence order and canonical child ownership; wrong kinds, shapes and lexical slots refuse."
  },
  {
    "id": "interface-010-AC-2",
    "path": "spec/monitor/functional/interface-010-monitor-sequence-operations.md",
    "role": "examined",
    "excerpt": "A noncommutative left fold has an independent expected result, empty input returns its declared identity, lexical captures remain scoped and recursive invocations restore outer bindings."
  },
  {
    "id": "interface-010-AC-3",
    "path": "spec/monitor/functional/interface-010-monitor-sequence-operations.md",
    "role": "examined",
    "excerpt": "Native element/visit/formation/retain charges and explicit work/stack/scratch limits stop before later selected work, retain exact typed evidence, expose no partial value and leave later invocation state clean."
  },
  {
    "id": "interface-010-AC-4",
    "path": "spec/monitor/functional/interface-010-monitor-sequence-operations.md",
    "role": "examined",
    "excerpt": "Map returns the body results and filter returns the true-predicate occurrences, each in occurrence order with duplicates kept, empty input yields an empty result, the item scope nests and restores, and each result equals the equivalent left fold."
  },
  {
    "id": "interface-010-AC-5",
    "path": "spec/monitor/functional/interface-010-monitor-sequence-operations.md",
    "role": "examined",
    "excerpt": "A non-Sequence operand, non-Boolean predicate, mistyped result annotation and invalid item address refuse at construction, and a StepBudget stop during map or filter exposes no partial value."
  },
  {
    "id": "interface-011-AC-1",
    "path": "spec/monitor/functional/interface-011-monitor-unions-and-equality.md",
    "role": "examined",
    "excerpt": "Verified union construction, full-identity case tests and payload reads preserve member/child ownership; foreign, unsealed or malformed bindings refuse and an inactive payload read cannot invent a value."
  },
  {
    "id": "interface-011-AC-2",
    "path": "spec/monitor/functional/interface-011-monitor-unions-and-equality.md",
    "role": "examined",
    "excerpt": "Shared checked equality produces independently expected equal/unequal results for selected ordinary values and retains the original conversion/enum/unit semantics without a replacement status or comparison model."
  },
  {
    "id": "interface-011-AC-3",
    "path": "spec/monitor/functional/interface-011-monitor-unions-and-equality.md",
    "role": "examined",
    "excerpt": "Earlier stopped payloads prevent later execution; native retention/equality shortages and scratch denial retain exact typed evidence without a partial result or state commit."
  },
  {
    "id": "interface-012-AC-1",
    "path": "spec/monitor/functional/interface-012-monitor-entry-dispatch.md",
    "role": "examined",
    "excerpt": "Changed package/clause/subject/occurrence/clock/counter/unit/width/profile/order or invalid required values refuse before entry execution, with state and reading/progress baselines unchanged."
  },
  {
    "id": "interface-012-AC-2",
    "path": "spec/monitor/functional/interface-012-monitor-entry-dispatch.md",
    "role": "examined",
    "excerpt": "Baseline events use delta zero, later admitted readings use the declared modular width, and polls or valid inclusive watermarks never move that reading baseline; regressing or foreign progress cannot settle."
  },
  {
    "id": "interface-012-AC-3",
    "path": "spec/monitor/functional/interface-012-monitor-entry-dispatch.md",
    "role": "examined",
    "excerpt": "A stopped event/watermark is unconsumed, preserves all committed state and allows same-machine lexical/fold re-entry; a source invariant terminates subsequent input and remains distinct from input/resource failures."
  },
  {
    "id": "interface-012-AC-4",
    "path": "spec/monitor/functional/interface-012-monitor-entry-dispatch.md",
    "role": "examined",
    "excerpt": "A completed step returns original canonical Results with its retained program association after preparation drops, preserving foreign-plan qualification without a replacement identity or temporal verdict."
  },
  {
    "id": "FR-003-AC-1",
    "path": "spec/proptest_adapter/functional/FR-003-proptest-adapter.md",
    "role": "examined",
    "excerpt": "Each verdict maps to the corresponding proptest outcome."
  },
  {
    "id": "FR-003-AC-2",
    "path": "spec/proptest_adapter/functional/FR-003-proptest-adapter.md",
    "role": "examined",
    "excerpt": "The adapter is absent unless the opt-in feature is selected, as the feature-off compiler probe and `compile_fail` doctest show."
  },
  {
    "id": "FR-003-AC-3",
    "path": "spec/proptest_adapter/functional/FR-003-proptest-adapter.md",
    "role": "examined",
    "excerpt": "`adapt` records nothing; `adapt_recording` records a matching verdict exactly once and maps it as `adapt` does; a mismatched identity yields a proptest failure naming both identities and leaves the report's counters unchanged."
  },
  {
    "id": "Cargo.toml",
    "path": "Cargo.toml",
    "role": "examined",
    "excerpt": "filament-specification-qualification = { git = \"https://github.com/agent-ix/filament-specification\", rev = \"ac130b973b1815221cc01a86723f79f0007fd11d\" }"
  },
  {
    "id": "Cargo.lock",
    "path": "Cargo.lock",
    "role": "examined",
    "excerpt": "source = \"git+https://github.com/agent-ix/filament-exact?rev=a58474cc105a86f3307a11def3fc001e2459679f#a58474cc105a86f3307a11def3fc001e2459679f\""
  },
  {
    "id": "measurement/exact-panic/Cargo.toml",
    "path": "measurement/exact-panic/Cargo.toml",
    "role": "examined",
    "excerpt": "test = false\nbench = false"
  },
  {
    "id": "tools/kernel-api-check/Cargo.toml",
    "path": "tools/kernel-api-check/Cargo.toml",
    "role": "examined",
    "excerpt": "filament-exact = { git = \"https://github.com/agent-ix/filament-exact\", rev = \"a58474cc105a86f3307a11def3fc001e2459679f\", default-features = false }"
  },
  {
    "id": "tests/exact_outcome_consumer.rs",
    "path": "tests/exact_outcome_consumer.rs",
    "role": "examined",
    "excerpt": "| ChargePoint::ModelCandidate => {}"
  }
]
```

## Dispositions

| FND | outcome | reason |
| --- | --- | --- |
| FND-001 | accepted-no-change | ROOT explicitly accepts the verified unchanged 74 untagged and 42 method-without-symbol obligations within this minimal dependency/consumer prerequisite under ARCH's wave authorization. This is ROOT's bounded decision, not an ARCH per-count waiver. The five-file diff leaves every spec criterion and trace marker unchanged; source changes add only the explicit ModelCandidate arm, preserve both consumer bindings and full authoritative equality, and introduce no new source defect or gap. Whole audit remains FAIL; no engine-backed PASS. |
